# Created by: DarkRelay Security Labs
import requests

# Client Configuration
BASE_URL = 'http://127.0.0.1:8080'

# Start client and interact with server
def interact_with_server():
    while True:
        print("\nBanking Transaction Simulator Client")
        print("1. View Account Balance")
        print("2. Make a Transaction")
        print("3. Open a New Account")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            account = input("Enter Your 3 Digit Account Number: ")
            response = requests.get(f"{BASE_URL}/view?account={account}")
        elif choice == "2":
            account = input("Enter Your 3 Digit Account Number: ")
            passkey = input("Enter Passkey: ")
            amount = input("Enter Amount (use negative for withdrawal): ")
            response = requests.post(f"{BASE_URL}/transaction", json={"account": account, "amount": amount, "passkey": passkey})
        elif choice == "3":
            account = input("Enter New 3 Digit Account Number: ")
            passkey = input("Set a Passkey for the Account: ")
            response = requests.post(f"{BASE_URL}/create_account", json={"account": account, "passkey": passkey})
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if response.status_code in (200, 201):
            print("Server Response:", response.json())
        else:
            print(f"Error: {response.status_code}", response.json())

if __name__ == "__main__":
    interact_with_server()
