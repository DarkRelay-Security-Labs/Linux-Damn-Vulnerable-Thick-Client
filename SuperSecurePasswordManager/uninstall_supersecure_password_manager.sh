#!/bin/bash
# Uninstallation script for SuperSecurePasswordManager

# Variables
SECRETS_DIR="/var/secrets"
BACKUPS_DIR="/var/backups"
CRON_SCRIPT="/usr/local/bin/cron_backup_super_secure.sh"
LIBRARY_PATH="/usr/local/lib/libencrypt.so"

# Remove cron job
crontab -l | grep -v "$CRON_SCRIPT" | crontab -

# Remove files and directories
rm -rf "$SECRETS_DIR"
rm -rf "$BACKUPS_DIR"
rm -f "$CRON_SCRIPT"
rm -f "$LIBRARY_PATH"
rm -f dummy_encrypt.c

echo "SuperSecurePasswordManager uninstalled successfully!"