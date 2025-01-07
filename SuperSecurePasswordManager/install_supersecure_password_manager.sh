#!/bin/bash
# Installation script for SuperSecurePasswordManager

# Variables
SECRETS_DIR="/var/secrets"
BACKUPS_DIR="/var/backups"
CRON_SCRIPT="cron_backup_super_secure.sh"
LIBRARY_PATH="/usr/local/lib/libencrypt.so"

# Create necessary directories
mkdir -p "$SECRETS_DIR"
mkdir -p "$BACKUPS_DIR"
chmod 777 "$SECRETS_DIR"
chmod 777 "$BACKUPS_DIR"

# Copy dummy library
echo "Creating dummy encryption library..."
echo -e "#include <stdio.h>\n#include <string.h>\n\nchar* encrypt(const char* input) {\n    static char encrypted[256];\n    snprintf(encrypted, sizeof(encrypted), \"encrypted_%s\", input);\n    return encrypted;\n}\n\nchar* decrypt(const char* input) {\n    static char decrypted[256];\n    if (strncmp(input, \"encrypted_\", 10) == 0) {\n        snprintf(decrypted, sizeof(decrypted), \"%s\", input + 10);\n    } else {\n        snprintf(decrypted, sizeof(decrypted), \"%s\", input);\n    }\n    return decrypted;\n}" > dummy_encrypt.c

gcc -shared -fPIC -o "$LIBRARY_PATH" dummy_encrypt.c
chmod 777 "$LIBRARY_PATH"

# Copy cron script
cp "$CRON_SCRIPT" /usr/local/bin/
chmod +x /usr/local/bin/cron_backup_super_secure.sh

# Add cron job
(crontab -l 2>/dev/null; echo "* * * * * /usr/local/bin/cron_backup_super_secure.sh") | crontab -

echo "SuperSecurePasswordManager installed successfully!"