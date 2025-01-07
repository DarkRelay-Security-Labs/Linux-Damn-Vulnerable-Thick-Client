#!/bin/bash
# Backup secrets file
BACKUP_FILE="/var/backups/passwords.bak"
SECRETS_FILE="/var/secrets/passwords.db"

if [ -f "$SECRETS_FILE" ]; then
    cp "$SECRETS_FILE" "$BACKUP_FILE"
    chmod 666 "$BACKUP_FILE"  # World-write permissions for demonstration
    echo "Backup completed successfully."
else
    echo "Secrets file not found."
fi