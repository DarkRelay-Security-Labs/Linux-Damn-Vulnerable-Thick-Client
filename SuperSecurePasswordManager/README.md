# SuperSecurePasswordManager

## Overview
The **SuperSecurePasswordManager** is a demonstration application created by **DarkRelay Security Labs**. It is designed to showcase vulnerabilities in Linux thick client setups and provide a platform for learning and practicing exploitation techniques.

## Key Functionalities
1. **Add Secret**: Encrypt and store a new secret with associated website, username, and password.
2. **Retrieve Secret**: Decrypt and retrieve the website, username, and password for a stored secret.
3. **Delete Secret**: Remove a stored secret by specifying the associated website.
4. **Backup Secrets**: Periodic backup of secrets via a cron job.

## Vulnerabilities
1. **LD_PRELOAD Injection**:
   - The application loads an encryption library dynamically using `ctypes.CDLL`.
   - The library path is set via the `ENCRYPT_LIB_PATH` environment variable, making it vulnerable to replacement.
2. **Cron Job Misconfiguration**:
   - `cron_backup_super_secure.sh` is writable by all users, allowing tampering.
3. **World-Writable Files**:
   - Secrets file (`/var/secrets/passwords.db`) and backup file (`/var/backups/passwords.bak`) have world-write permissions.

## Installation
Run the `install_supersecure_password_manager.sh` script with appropriate privileges:
```bash
sudo bash install_supersecure_password_manager.sh
```

## Exploiting LD_PRELOAD
1. **Create a Malicious Library**
   - Download the `exploit_ld_preload.c` code:

2. **Compile the Exploit Library**
   ```bash
   gcc -shared -fPIC -o malicious_lib.so exploit_ld_preload.c
   ```

3. **Run the Application with LD_PRELOAD**
   ```bash
   LD_PRELOAD=./malicious_lib.so python3 super_secure_password_manager.py
   ```

4. **Verify the Exploit**
   - Check the `/tmp/ld_preload_exploit_indicator` file for logs:
     ```bash
     cat /tmp/ld_preload_exploit_indicator
     ```

     Example Expected Output:
     ```
     LD_PRELOAD: Malicious library loaded successfully
     LD_PRELOAD: encrypt function called
     LD_PRELOAD: decrypt function called
     ```

## Uninstallation
Remove the application using the `uninstall_supersecure_password_manager.sh` script:
```bash
sudo bash uninstall_supersecure_password_manager.sh
```

## Disclaimer
This application is for **educational purposes only**. Use it responsibly to learn about vulnerabilities and their mitigations.

**Created by DarkRelay Security Labs.**