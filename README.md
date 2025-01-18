# Linux-Damn-Vulnerable-Thick-Client

A Thick client app collection for Linux, designed to be vulnerable by design! a.k.a. Linux-Damn-Vulnerable-Thick-Client or Linux-Thick-Client-GOAT. This collection of applications is intended to be utilized independently by the community and serves as a supplementary project for our Linux thick client penetration testing course. Details of the course are available at: [https://www.darkrelay.com/challenge-page/linux-thick-client-penetration-testing-course](https://www.darkrelay.com/challenge-page/linux-thick-client-penetration-testing-course)

---

## Disclaimer

Warning! You are about to engage with DarkRelay's Linux Damn Vulnerable Thick Client Project! The purpose of this project is to educate individuals on Thick client vulnerabilities and common misconfigurations. If you use this project for malicious purposes or if your system is compromised through the use of this project, DarkRelay does not hold any responsibility! DarkRelay or its contributors will not be responsible for misuse of this project.

If you have more questions, please reach out to us via [get-started](https://www.darkrelay.com/get-started) or email us at: info@darkrelay.com.

---

## Planned Vulnerabilities

The applications in this project are intentionally designed with vulnerabilities for educational purposes. Below is a consolidated list of planned vulnerabilities across the included applications:

### 1. **SuperSecure Bank App**

- **Service File Permissions**: The service file is installed with world-write permissions (`777`), allowing any user to modify it and execute arbitrary code as `root`.
- **World-Writable Data Files**: Account data is stored in `/var/log/account_data.json` with `666` permissions, enabling unauthorized modification of balances or passkeys.
- **Lack of Input Validation**: The server accepts data from the client without proper validation, making it vulnerable to injection attacks.
- **Passkey Vulnerabilities**: Passkeys are stored in plaintext, exposing them to unauthorized access if the data file is compromised.

### 2. **SuperSecure Log Manager**

- **SUID/SGID Misconfiguration**: The application binary `SuperSecureLogManager` is installed with the SUID bit set, allowing users to execute privileged operations such as exporting logs from `/var/log`, leading to potential privilege escalation.
- **.SO Hijacking**: The application dynamically loads the `liblogprocessor.so` library, and attackers can replace or hijack it to execute arbitrary code with elevated privileges.

### 3. **SuperSecure Note Maker App**

- **World-Writable Files**: The notes file (`/tmp/notes.txt`) is created with `666` permissions, allowing any user to read and write to it, enabling unauthorized tampering or malicious content injection.
- **No Authentication**: The application does not require authentication, granting unrestricted access to sensitive operations.
- **Lack of Input Validation**: User input is not sanitized, exposing the app to potential injection attacks.

### 4. **SuperSecure Password Manager**

- **LD_PRELOAD Injection**: The application dynamically loads an encryption library using `ctypes.CDLL`, with the path specified via the `ENCRYPT_LIB_PATH` environment variable, making it vulnerable to replacement.
- **Cron Job Misconfiguration**: The `cron_backup_super_secure.sh` script is writable by all users, allowing tampering and potential execution of malicious commands.
- **World-Writable Files**: The secrets file (`/var/secrets/passwords.db`) and backup file (`/var/backups/passwords.bak`) have world-write permissions, allowing unauthorized access or modifications.

---

## Contributing to the Project

Please open a pull request with your changes and drop a mail to info@darkrelay.com requesting approval.

---

## Licensing

This project is available under the [Apache 2.0 license](./LICENSE).

---

## Follow Us for More

- [DarkRelay on LinkedIn](https://www.linkedin.com/company/darkrelay)
- [DarkRelay on X](https://x.com/darkrelaylabs)
- [DarkRelay on YouTube](https://www.youtube.com/@darkrelay)
- [DarkRelay on Instagram](https://www.instagram.com/darkrelay/)

Additionally, DarkRelay Security Labs offers a range of cybersecurity training programs, including courses on exploit development, which cover topics like fuzzing applications, device drivers, and bypassing memory protection features on various platforms. These courses are designed to enhance your skills in areas such as stack and heap overflows, format string bugs, and more. You can explore their training offerings here: [darkrelay.com/academy](https://www.darkrelay.com/academy)

Engaging with these resources can significantly improve your understanding of heap overflows and other critical security vulnerabilities, equipping you with the knowledge to effectively address such issues in real-world scenarios.
