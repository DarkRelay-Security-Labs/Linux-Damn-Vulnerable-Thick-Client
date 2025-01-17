#!/bin/bash

# Copy the application script to /usr/local/bin
cp vulnerable_notes.sh /usr/local/bin/vulnerable_notes.sh

# Set the script to be executable
chmod +x /usr/local/bin/vulnerable_notes.sh

# Set insecure permissions on the notes file
touch /tmp/notes.txt
chmod 666 /tmp/notes.txt  # Read and write permissions for all users

echo "Vulnerable Note-Taking Application installed."
echo "Run 'vulnerable_notes.sh' to start the application."
