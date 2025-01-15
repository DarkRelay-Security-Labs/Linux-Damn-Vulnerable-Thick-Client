import os
import json
import ctypes

# Constants
SECRETS_FILE = "/var/secrets/passwords.db"
KEY_FILE = "/var/secrets/encryption.key"
LIBRARY_PATH = os.getenv("ENCRYPT_LIB_PATH", "/usr/local/lib/libencrypt.so")
HIJACK_LIB_PATH = "/tmp/libsecure_encrypt.so"

def load_hijack_library():
    if os.path.exists(HIJACK_LIB_PATH):
        try:
            hijack_lib = ctypes.CDLL(HIJACK_LIB_PATH)  # Load .so file from a world-writable location
            print(f"Successfully loaded library from {HIJACK_LIB_PATH}")
        except Exception as e:
            print(f"Failed to load library from {HIJACK_LIB_PATH}: {e}")

# Load encryption library dynamically (vulnerable to LD_PRELOAD injection)
try:
    encrypt_lib = ctypes.CDLL(LIBRARY_PATH)
    encrypt_lib.encrypt.argtypes = [ctypes.c_char_p]
    encrypt_lib.decrypt.argtypes = [ctypes.c_char_p]
    encrypt_lib.encrypt.restype = ctypes.c_char_p
    encrypt_lib.decrypt.restype = ctypes.c_char_p

    load_hijack_library()
except Exception as e:
    print(f"Failed to load encryption library: {e}")
    exit(1)

# Ensure secrets file exists
if not os.path.exists(SECRETS_FILE):
    os.makedirs(os.path.dirname(SECRETS_FILE), exist_ok=True)
    with open(SECRETS_FILE, 'w') as f:
        json.dump({}, f)
os.chmod(SECRETS_FILE, 0o666)  # World-write permissions for demonstration

# Ensure encryption key exists
if not os.path.exists(KEY_FILE):
    key = b"dummy_key_for_demo"  # Using a fixed key for demonstration
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
os.chmod(KEY_FILE, 0o666)  # World-write permissions for demonstration

# Dummy encryption and decryption wrapper for demo
class EncryptionWrapper:
    @staticmethod
    def encrypt(value):
        return encrypt_lib.encrypt(value.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decrypt(value):
        return encrypt_lib.decrypt(value.encode('utf-8')).decode('utf-8')

cipher = EncryptionWrapper()

def load_secrets():
    with open(SECRETS_FILE, 'r') as f:
        return json.load(f)

def save_secrets(secrets):
    with open(SECRETS_FILE, 'w') as f:
        json.dump(secrets, f)

def add_secret():
    secrets = load_secrets()
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = cipher.encrypt(password)
    secrets[website] = {"username": username, "password": encrypted_password}
    save_secrets(secrets)
    print("Secret added successfully.")

def retrieve_secret():
    secrets = load_secrets()
    website = input("Enter website: ")
    if website in secrets:
        username = secrets[website]["username"]
        decrypted_password = cipher.decrypt(secrets[website]["password"])
        print(f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}")
    else:
        print("Secret not found.")

def delete_secret():
    secrets = load_secrets()
    website = input("Enter website: ")
    if website in secrets:
        del secrets[website]
        save_secrets(secrets)
        print("Secret deleted successfully.")
    else:
        print("Secret not found.")

def main():
    while True:
        print("\nSuperSecurePasswordManager")
        print("1. Add Secret")
        print("2. Retrieve Secret")
        print("3. Delete Secret")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_secret()
        elif choice == "2":
            retrieve_secret()
        elif choice == "3":
            delete_secret()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
