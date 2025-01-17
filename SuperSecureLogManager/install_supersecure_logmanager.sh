#!/bin/bash
# File: install_supersecure_logmanager.sh

set -e

# Variables
LIB_PATH="/usr/lib/liblogprocessor.so"
CONFIG_PATH="/etc/logmanager.conf"
BINARY_PATH="/usr/local/bin/SuperSecureLogManager"
EXPORT_PATH="/tmp/exported_logs.zip"

# Step 1: Run make clean and then make
echo "Cleaning previous builds..."
make clean

echo "Building the project..."
if ! make; then
    echo "Build failed. Please check for errors."
    exit 1
fi

# Step 2: Copy the shared library to /usr/lib/
echo "Installing liblogprocessor.so to $LIB_PATH"
cp lib/liblogprocessor.so $LIB_PATH

# Step 3: Create the configuration file
echo "Creating configuration file at $CONFIG_PATH"
echo "# Configuration file for SuperSecureLogManager" | sudo tee $CONFIG_PATH > /dev/null
echo "" | sudo tee -a $CONFIG_PATH > /dev/null
echo "# Path to export logs" | sudo tee -a $CONFIG_PATH > /dev/null
echo "export_path=$EXPORT_PATH" | sudo tee -a $CONFIG_PATH > /dev/null

# Step 4: Copy the main binary to /usr/local/bin
echo "Installing SuperSecureLogManager to $BINARY_PATH"
cp build/SuperSecureLogManager $BINARY_PATH

# Step 5: Set SUID permissions on the binary
chown root $BINARY_PATH
chmod u+s $BINARY_PATH

echo "Installation complete. You can now use SuperSecureLogManager by running:"
echo "  $BINARY_PATH"
