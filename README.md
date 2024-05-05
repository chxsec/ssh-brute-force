# ssh-brute-force
ssh-brute-force script for use with password protected key -- username brute force tool
# SSH Brute Force Tool

This Python script is designed to perform SSH brute force attacks by trying different usernames against an SSH server.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- `sshpass` (required for password authentication): Install using your package manager (`apt-get`, `yum`, etc.).
## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/chxsec/ssh-brute-force.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ssh-brute-force
    ```

3. Run the script:

    ```bash
    python3 sshbrute.py
    ```

4. Follow the prompts and provide the required information:
    - IP address of the SSH server
    - Path to the private key file
    - Path to the file containing a list of usernames
    - SSH private key passphrase (if required)

5. Wait for the script to complete. If a valid username and password combination is found, the username will be printed to the terminal.

## Disclaimer

This tool is intended for educational and testing purposes only. Unauthorized access to remote systems is illegal and unethical. Use this tool responsibly and only with proper authorization.

## License

This project is licensed under the [MIT License](LICENSE).
