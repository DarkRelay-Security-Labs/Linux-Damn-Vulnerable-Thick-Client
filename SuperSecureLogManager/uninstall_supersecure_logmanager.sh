# File: uninstall_supersecure_logmanager.sh

#!/bin/bash
set -e

echo "Cleaning builds..."
make clean

# Variables
LIB_PATH="/usr/lib/liblogprocessor.so"
CONFIG_PATH="/etc/logmanager.conf"
BINARY_PATH="/usr/local/bin/SuperSecureLogManager"

# Step 1: Remove the binary from /usr/local/bin/
echo "Removing SuperSecureLogManager from $BINARY_PATH"
rm -rf $BINARY_PATH

# Step 2: Remove the shared library from /usr/lib/
echo "Removing liblogprocessor.so from $LIB_PATH"
rm -rf $LIB_PATH

# Step 3: Remove the configuration file
echo "Removing configuration file $CONFIG_PATH"
rm -rf $CONFIG_PATH

echo "Uninstallation complete. SuperSecureLogManager has been removed."
