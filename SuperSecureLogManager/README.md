# SuperSecure Log Manager

## Overview

The **SuperSecure Log Manager** is a demonstration application created by **DarkRelay Security Labs**. It is designed to showcase common security vulnerabilities in Linux thick client applications, including **SUID/SGID misconfigurations**, and **.SO hijacking**. This platform serves as a learning tool to understand and exploit these vulnerabilities.

---

## Installation Steps

### Step 1: Download the Files

Ensure you have the following files:

- `install_supersecure_logmanager.sh` (Installation script)
- `uninstall_supersecure_logmanager.sh` (Uninstallation script)
- Source files and Makefile for building the application.

---

### Step 2: Run the Installation Script

1. **Build and Install SuperSecure Log Manager:**
   - Grant execution permissions and run the installation script:
     ```bash
     chmod +x install_supersecure_logmanager.sh
     sudo bash install_supersecure_logmanager.sh
     ```
   - This script will:
     - Build the application using `make`.
     - Copy the shared library `liblogprocessor.so` to `/usr/lib/`.
     - Create the configuration file `/etc/logmanager.conf` with default settings.
     - Copy the binary `SuperSecureLogManager` to `/usr/local/bin/`.
     - Set the binary as SUID root to allow privilege escalation demonstrations.

---

## Uninstallation Steps

- Run the uninstall script:
  ```bash
  sudo bash uninstall_supersecure_logmanager.sh
  ```
- This will:
  - Remove the application binary from `/usr/local/bin/`.
  - Remove the shared library from `/usr/lib/`.
  - Delete the configuration file `/etc/logmanager.conf`.

---

# Planned Vulnerabilities

The SuperSecure Log Manager contains deliberate vulnerabilities for educational purposes:

### 1. **SUID/SGID Misconfiguration**

- The application binary `SuperSecureLogManager` is installed with the SUID bit set.
- Allows users to execute privileged operations such as exporting logs from `/var/log`.
- Improper validation can lead to privilege escalation.

### 2. **.SO Hijacking**

- The application dynamically loads the `liblogprocessor.so` library.
- The loader searches directories specified in the `RPATH` or `RUNPATH` or `LD_LIBRARY_PATH`.
- Attackers can replace or hijack this library to execute arbitrary code with elevated privileges.

---

# Disclaimer

This application is for **educational purposes only**. Do not deploy it in a production environment. Use it responsibly to learn about vulnerabilities and how to mitigate them.

**Created by [DarkRelay Security Labs](https://www.darkrelay.com)**
