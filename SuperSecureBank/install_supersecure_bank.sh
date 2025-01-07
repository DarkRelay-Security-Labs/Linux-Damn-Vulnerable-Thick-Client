#!/bin/bash

# Installation script for Banking Transaction Simulator

# Variables
SERVER_SCRIPT="bank_server.py"
CLIENT_SCRIPT="client.py"
SERVICE_FILE="banking.service"
INSTALL_DIR="/usr/local/banking_simulator"
SERVICE_PATH="/etc/systemd/system/banking.service"

# Create installation directory
mkdir -p $INSTALL_DIR

# Copy files to installation directory
cp $SERVER_SCRIPT $INSTALL_DIR/
cp $CLIENT_SCRIPT $INSTALL_DIR/

# Set permissions
chmod +x $INSTALL_DIR/$SERVER_SCRIPT
chmod +x $INSTALL_DIR/$CLIENT_SCRIPT

# Install and enable service
cp $SERVICE_FILE $SERVICE_PATH
sed -i "s|/path/to/bank_server.py|$INSTALL_DIR/bank_server.py|" $SERVICE_PATH
chmod 777 $SERVICE_PATH
systemctl daemon-reload
systemctl enable banking.service
systemctl start banking.service

echo "Creating default account..."
echo '{"123": {"balance": 1000, "passkey": "supersecure"}}' > /var/log/account_data.json
chmod 666 /var/log/account_data.json

echo "Banking Transaction Simulator installed successfully!"
