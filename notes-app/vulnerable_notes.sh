#!/bin/bash

NOTES_FILE="/tmp/notes.txt"

# Function to add a note
add_note() {
    echo "Enter your note:"
    read -r note
    echo "$(date): $note" >> "$NOTES_FILE"
    echo "Note added."
}

# Function to view notes
view_notes() {
    if [[ -f "$NOTES_FILE" ]]; then
        cat "$NOTES_FILE"
    else
        echo "No notes found."
    fi
}

# Main menu
while true; do
    echo "1. Add Note"
    echo "2. View Notes"
    echo "3. Exit"
    read -rp "Choose an option: " choice
    case $choice in
        1) add_note ;;
        2) view_notes ;;
        3) exit 0 ;;
        *) echo "Invalid option." ;;
    esac
done
