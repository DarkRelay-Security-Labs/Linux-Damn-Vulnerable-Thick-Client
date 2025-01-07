#!/bin/bash

# Uninstallation script for Banking Transaction Simulator

# Variables
INSTALL_DIR="/usr/local/banking_simulator"
SERVICE_PATH="/etc/systemd/system/banking.service"

# Stop and disable the service
systemctl stop banking.service
systemctl disable banking.service

# Remove service file
rm -f $SERVICE_PATH
systemctl daemon-reload

# Remove installation directory
rm -rf $INSTALL_DIR

# Remove persistent data file
rm -f /var/log/account_data.json

echo "Banking Transaction Simulator uninstalled successfully!"
