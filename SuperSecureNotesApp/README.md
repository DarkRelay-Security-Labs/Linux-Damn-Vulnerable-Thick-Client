# SuperSecure Note Maker App

## Overview

The **SuperSecure Note Maker App** is a demonstration application created by **DarkRelay Security Labs**. It is designed to showcase common security vulnerabilities in Linux thick client applications and serve as a platform for learning about improper file permissions and test them.

---

## Installation Steps

### Step 1: Download the Files

Ensure you have the following files:

- `vulnerable_notes.sh` (Note-taking application script)
- `setup_vulnerable_notes.sh` (Setup script for the application)
- `uninstall_vulnerable_notes.sh` (Uninstallation script)

---

### Step 2: Run the Installation Script

1. **SuperSecure Note Maker App:**
   - Grant execution permissions and run the setup script:
     ```bash
     chmod +x setup_vulnerable_notes.sh
     sudo bash setup_vulnerable_notes.sh
     ```
   - This script will:
     - Copy the `vulnerable_notes.sh` script to `/usr/local/bin`.
     - Create a world-writable notes file (`/tmp/notes.txt`) with `666` permissions.

---

## Uninstallation Steps

- Run the uninstall script:
  ```bash
  sudo bash uninstall_vulnerable_notes.sh
  ```
- This will:
  - Remove the application script from `/usr/local/bin`.
  - Delete the notes file (`/tmp/notes.txt`).

---

# Planned Vulnerabilities

The SuperSecure Note Maker App contains deliberate vulnerabilities for learning purposes:

### 1. **World-Writable Files**

- **Notes File (****`/tmp/notes.txt`****):**
  - File permissions are set to `666`, allowing any user to read from and write to the file.
  - Unauthorized users can tamper with the notes or inject malicious content.

### 3. **No Authentication**

- The application does not require any authentication, allowing unrestricted access to sensitive operations.

### 4. **Lack of Input Validation**

- The note-taking app does not sanitize user input, exposing it to potential injection attacks.

---

# Disclaimer

This application is for **educational purposes only**. Do not deploy it in a production environment. Use it responsibly to learn about vulnerabilities and how to mitigate them.

**Created by ****[DarkRelay Security Labs](https://www.darkrelay.com)**
