# Created by: DarkRelay Security Labs

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 8080  # Port to listen on
TRANSACTION_LOG = '/var/log/transactions.log'
PERSISTENT_FILE = '/var/log/account_data.json'
ACCOUNTS = {}

# Ensure transaction log exists
if not os.path.exists(TRANSACTION_LOG):
    os.makedirs(os.path.dirname(TRANSACTION_LOG), exist_ok=True)
    with open(TRANSACTION_LOG, 'w') as f:
        f.write("Transaction Log:\n")

# Ensure persistent data file exists and has write permissions for all
if not os.path.exists(PERSISTENT_FILE):
    with open(PERSISTENT_FILE, 'w') as f:
        json.dump({}, f)
os.chmod(PERSISTENT_FILE, 0o666)  # u, g, o write permissions

# Load accounts from persistent storage
if os.path.exists(PERSISTENT_FILE):
    with open(PERSISTENT_FILE, 'r') as f:
        ACCOUNTS = json.load(f)

class BankingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/view?"):
            account = self.path.split("?")[1].split("=")[1]
            if account in ACCOUNTS:
                balance = ACCOUNTS[account]["balance"]
                self._send_response(200, {"account": account, "balance": balance})
            else:
                self._send_response(404, {"error": "Account not found"})
        else:
            self._send_response(404, {"error": "Invalid endpoint"})

    def do_POST(self):
        if self.path == "/transaction":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                account = data.get("account")
                amount = float(data.get("amount"))
                passkey = data.get("passkey")
                if account in ACCOUNTS and ACCOUNTS[account]["passkey"] == passkey:
                    ACCOUNTS[account]["balance"] += amount
                    with open(TRANSACTION_LOG, 'a') as log:
                        log.write(f"Account: {account}, Amount: {amount}\n")
                    self._update_persistent_data()
                    self._send_response(200, {"message": "Transaction successful", "account": account, "new_balance": ACCOUNTS[account]["balance"]})
                elif account not in ACCOUNTS:
                    self._send_response(404, {"error": "Account not found"})
                else:
                    self._send_response(403, {"error": "Invalid passkey"})
            except Exception as e:
                self._send_response(400, {"error": str(e)})
        elif self.path == "/create_account":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                account = data.get("account")
                passkey = data.get("passkey")
                if account in ACCOUNTS:
                    self._send_response(400, {"error": "Account already exists"})
                else:
                    ACCOUNTS[account] = {"balance": 0, "passkey": passkey}
                    with open(TRANSACTION_LOG, 'a') as log:
                        log.write(f"New Account Created: {account}\n")
                    self._update_persistent_data()
                    self._send_response(201, {"message": "Account created successfully", "account": account})
            except Exception as e:
                self._send_response(400, {"error": str(e)})
        else:
            self._send_response(404, {"error": "Invalid endpoint"})

    def _send_response(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _update_persistent_data(self):
        with open(PERSISTENT_FILE, 'w') as f:
            json.dump(ACCOUNTS, f)

# Start the server
def start_server():
    server = HTTPServer((HOST, PORT), BankingHandler)
    print(f"Server running on http://{HOST}:{PORT}...")
    server.serve_forever()

if __name__ == "__main__":
    start_server()
