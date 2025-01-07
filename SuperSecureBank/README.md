# Setup Guide for SuperSecure Bank

## Overview

The **SuperSecure Bank** is a demonstration application created by **DarkRelay Security Labs**. It is designed to showcase vulnerabilities in Linux thick client setups and provide a platform for learning and practicing exploitation techniques.

---

## Installation Steps

1. **Download the Files**

   - Ensure you have the following files:
     - `bank_server.py`
     - `client.py`
     - `banking.service`
     - `install.sh`
     - `uninstall.sh`

2. **Run the Installation Script**

   - Execute the installation script:
     ```bash
     sudo bash install.sh
     ```
   - The script will:
     - Copy the necessary files to `/usr/local/banking_simulator`.
     - Set up the service file with world-write permissions (`777`).
     - Create a default account (`123` with passkey `supersecure` and balance `1000`).
     - Start the service.

3. **Verify Installation**

   - Check that the service is running:
     ```bash
     systemctl status banking.service
     ```

4. **Start Using the Client**

   - Run the client:
     ```bash
     python3 /usr/local/banking_simulator/client.py
     ```

---

## Uninstallation Steps

1. **Run the Uninstall Script**
   - Execute the uninstall script:
     ```bash
     sudo bash uninstall.sh
     ```
   - This will:
     - Stop and remove the service.
     - Delete the application directory and log files.

---

# README: Planned Vulnerabilities

The Banking Transaction Simulator contains deliberate vulnerabilities for learning purposes:

1. **Service File Permissions**

   - The service file is installed with world-write permissions (`777`), allowing any user to modify it and execute arbitrary code as `root`.

2. **World-Writable Data Files**

   - Account data is stored in `/var/log/account_data.json` with world-write permissions (`666`), enabling unauthorized users to modify balances or passkeys.

3. **Directory Permissions**

   - The installation directory is configured with `777` permissions, allowing unauthorized modifications to application files.

4. **Lack of Input Validation**

   - The server accepts data from the client without rigorous validation, exposing it to potential injection attacks.

5. **Passkey Vulnerabilities**

   - Account passkeys are stored in plaintext, making them susceptible to unauthorized access if the data file is compromised.

---

# Disclaimer

This application is for **educational purposes only**. Do not deploy it in a production environment. Use it responsibly to learn about vulnerabilities and how to mitigate them.

**Created by [DarkRelay Security Labs](https://www.darkrelay.com).**

