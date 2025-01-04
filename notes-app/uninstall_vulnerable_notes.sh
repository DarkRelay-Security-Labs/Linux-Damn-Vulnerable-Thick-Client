#!/bin/bash

# Define variables
APP_SCRIPT="/usr/local/bin/vulnerable_notes.sh"
NOTES_FILE="/tmp/notes.txt"

# Check if the application script exists and remove it
if [ -f "$APP_SCRIPT" ]; then
    echo "Removing application script: $APP_SCRIPT"
    sudo rm "$APP_SCRIPT"
    echo "Application script removed."
else
    echo "Application script not found: $APP_SCRIPT"
fi

# Check if the notes file exists and remove it
if [ -f "$NOTES_FILE" ]; then
    echo "Removing notes file: $NOTES_FILE"
    sudo rm "$NOTES_FILE"
    echo "Notes file removed."
else
    echo "Notes file not found: $NOTES_FILE"
fi

echo "Uninstallation completed."
