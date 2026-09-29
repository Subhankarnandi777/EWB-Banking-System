import random
from datetime import datetime


# ============================================================
# BANKING SYSTEM
# Python With AI - Day 9 Mini Project
# ============================================================


# Dictionary to store all bank accounts
accounts = {}


# ============================================================
# 1. GENERATE ACCOUNT NUMBER
# ============================================================

def generate_account_number():
    """
    Generates a unique 8-digit account number.
    Uses the random module.
    """

    while True:
        account_number = str(random.randint(10000000, 99999999))

        if account_number not in accounts:
            return account_number


# ============================================================
# 2. CREATE ACCOUNT
# ============================================================

def create_account():

    print("\n")
    print("=" * 50)
    print("              CREATE ACCOUNT")
    print("=" * 50)

    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    phone = input("Enter your phone number: ").strip()

    while not phone.isdigit() or len(phone) != 10:
        print("Please enter a valid 10-digit phone number.")
        phone = input("Enter your phone number: ").strip()

    # PIN creation
    while True:

        pin = input("Create a 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    # Generate account number
    account_number = generate_account_number()

    # Store account information
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    print("\n" + "=" * 50)
    print("       ACCOUNT CREATED SUCCESSFULLY")
    print("=" * 50)

    print("Account Holder :", name)
    print("Phone Number   :", phone)
    print("Account Number :", account_number)
    print("Initial Balance: ₹0")

    print("\nIMPORTANT:")
    print("Please remember your Account Number and PIN.")


# ============================================================
# 3. LOGIN
# ============================================================

def login():

    print("\n")
    print("=" * 50)
    print("                    LOGIN")
    print("=" * 50)

    account_number = input("Enter Account Number: ").strip()
    pin = input("Enter PIN: ").strip()

    # Check account
    if account_number not in accounts:
        print("\nAccount not found.")
        return

    # Check PIN
    if accounts[account_number]["pin"] != pin:
        print("\nIncorrect PIN.")
        return

    print("\nLogin successful!")
    print(
        "Welcome,",
        accounts[account_number]["name"]
    )

    # Open account menu
    account_menu(account_number)


# ============================================================
# 4. CHECK BALANCE
# ============================================================

def check_balance(account_number):

    print("\n")
    print("=" * 50)
    print("                 ACCOUNT BALANCE")
    print("=" * 50)

    balance = accounts[account_number]["balance"]

    print("Account Number :", account_number)
    print("Account Holder :", accounts[account_number]["name"])
    print("Current Balance: ₹", balance)


# ============================================================
# 5. DEPOSIT MONEY
# ============================================================

def deposit(account_number):

    print("\n")
    print("=" * 50)
    print("                  DEPOSIT MONEY")
    print("=" * 50)

    amount = input("Enter amount to deposit: ").strip()

    # Check if amount is a number
    if not amount.isdigit():
        print("\nPlease enter a valid amount.")
        return

    amount = int(amount)

    # Amount validation
    if amount <= 0:
        print("\nAmount must be greater than ₹0.")
        return

    # Add money
    accounts[account_number]["balance"] += amount

    # Get current date and time
    time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # Create transaction record
    transaction = (
        time
        + " | Deposit | ₹"
        + str(amount)
        + " | Balance: ₹"
        + str(accounts[account_number]["balance"])
    )

    # Store transaction
    accounts[account_number]["transactions"].append(
        transaction
    )

    print("\nDeposit successful!")
    print("Deposited Amount: ₹", amount)
    print(
        "New Balance: ₹",
        accounts[account_number]["balance"]
    )


# ============================================================
# 6. WITHDRAW MONEY
# ============================================================

def withdraw(account_number):

    print("\n")
    print("=" * 50)
    print("                 WITHDRAW MONEY")
    print("=" * 50)

    amount = input("Enter amount to withdraw: ").strip()

    # Check if amount is a number
    if not amount.isdigit():
        print("\nPlease enter a valid amount.")
        return

    amount = int(amount)

    # Amount validation
    if amount <= 0:
        print("\nAmount must be greater than ₹0.")
        return

    # Check balance
    if amount > accounts[account_number]["balance"]:
        print("\nInsufficient balance.")
        print(
            "Available Balance: ₹",
            accounts[account_number]["balance"]
        )
        return

    # Deduct amount
    accounts[account_number]["balance"] -= amount

    # Get current time
    time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # Create transaction
    transaction = (
        time
        + " | Withdrawal | ₹"
        + str(amount)
        + " | Balance: ₹"
        + str(accounts[account_number]["balance"])
    )

    # Store transaction
    accounts[account_number]["transactions"].append(
        transaction
    )

    print("\nWithdrawal successful!")
    print("Withdrawn Amount: ₹", amount)
    print(
        "Remaining Balance: ₹",
        accounts[account_number]["balance"]
    )


# ============================================================
# 7. TRANSFER MONEY
# ============================================================

def transfer(account_number):

    print("\n")
    print("=" * 50)
    print("                 TRANSFER MONEY")
    print("=" * 50)

    receiver = input(
        "Enter receiver Account Number: "
    ).strip()

    # Check receiver account
    if receiver not in accounts:
        print("\nReceiver account not found.")
        return

    # Prevent transferring to own account
    if receiver == account_number:
        print("\nYou cannot transfer money to your own account.")
        return

    amount = input(
        "Enter amount to transfer: "
    ).strip()

    # Check amount
    if not amount.isdigit():
        print("\nPlease enter a valid amount.")
        return

    amount = int(amount)

    # Check amount
    if amount <= 0:
        print("\nAmount must be greater than ₹0.")
        return

    # Check sender balance
    if amount > accounts[account_number]["balance"]:
        print("\nInsufficient balance.")
        print(
            "Available Balance: ₹",
            accounts[account_number]["balance"]
        )
        return

    # Deduct from sender
    accounts[account_number]["balance"] -= amount

    # Add to receiver
    accounts[receiver]["balance"] += amount

    # Current date and time
    time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # Sender transaction
    sender_transaction = (
        time
        + " | Transfer to "
        + receiver
        + " | ₹"
        + str(amount)
        + " | Balance: ₹"
        + str(accounts[account_number]["balance"])
    )

    # Receiver transaction
    receiver_transaction = (
        time
        + " | Received from "
        + account_number
        + " | ₹"
        + str(amount)
        + " | Balance: ₹"
        + str(accounts[receiver]["balance"])
    )

    # Store sender transaction
    accounts[account_number]["transactions"].append(
        sender_transaction
    )

    # Store receiver transaction
    accounts[receiver]["transactions"].append(
        receiver_transaction
    )

    print("\nTransfer successful!")
    print("Transferred Amount: ₹", amount)
    print("Receiver Account :", receiver)
    print(
        "Remaining Balance: ₹",
        accounts[account_number]["balance"]
    )


# ============================================================
# 8. TRANSACTION HISTORY
# ============================================================

def transaction_history(account_number):

    print("\n")
    print("=" * 70)
    print("                    TRANSACTION HISTORY")
    print("=" * 70)

    transactions = accounts[account_number]["transactions"]

    # Check whether transactions exist
    if len(transactions) == 0:

        print("No transactions found.")

    else:

        for transaction in transactions:
            print(transaction)


# ============================================================
# 9. CHANGE PIN
# ============================================================

def change_pin(account_number):

    print("\n")
    print("=" * 50)
    print("                    CHANGE PIN")
    print("=" * 50)

    # Current PIN
    old_pin = input("Enter current PIN: ").strip()

    # Verify old PIN
    if old_pin != accounts[account_number]["pin"]:
        print("\nIncorrect current PIN.")
        return

    # New PIN
    new_pin = input("Enter new 4-digit PIN: ").strip()

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("\nPIN must contain exactly 4 digits.")
        return

    # Confirm PIN
    confirm_pin = input(
        "Confirm new 4-digit PIN: "
    ).strip()

    if new_pin != confirm_pin:
        print("\nPIN confirmation does not match.")
        return

    # Change PIN
    accounts[account_number]["pin"] = new_pin

    print("\nPIN changed successfully!")


# ============================================================
# 10. LOGOUT
# ============================================================

def logout():

    print("\n")
    print("=" * 50)
    print("              LOGGED OUT SUCCESSFULLY")
    print("=" * 50)


# ============================================================
# 11. ACCOUNT MENU
# ============================================================

def account_menu(account_number):

    while True:

        print("\n")
        print("=" * 50)
        print("                 ACCOUNT MENU")
        print("=" * 50)

        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        # Check balance
        if choice == "1":

            check_balance(account_number)

        # Deposit
        elif choice == "2":

            deposit(account_number)

        # Withdraw
        elif choice == "3":

            withdraw(account_number)

        # Transfer
        elif choice == "4":

            transfer(account_number)

        # Transaction history
        elif choice == "5":

            transaction_history(account_number)

        # Change PIN
        elif choice == "6":

            change_pin(account_number)

        # Logout
        elif choice == "7":

            logout()
            break

        # Invalid option
        else:

            print(
                "\nInvalid choice."
                " Please select between 1 and 7."
            )


# ============================================================
# 12. MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("             WELCOME TO BANKING SYSTEM")
        print("=" * 50)

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        # Create account
        if choice == "1":

            create_account()

        # Login
        elif choice == "2":

            login()

        # Exit
        elif choice == "3":

            print("\n")
            print("=" * 50)
            print(" Thank you for using the Banking System!")
            print("=" * 50)

            break

        # Invalid option
        else:

            print(
                "\nInvalid choice."
                " Please select 1, 2, or 3."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()