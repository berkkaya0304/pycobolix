"""
Simple Bank Management System
Converted from COBOL (bank_management.cbl) to Python
"""


def main():
    print("Welcome to Simple Bank System")
    acc_number = input("Enter Account Number (10 digits): ")
    acc_holder = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit Amount: "))

    while True:
        print()
        print("--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        choice = input("Enter Your Choice (1-4): ").strip()

        if choice == "1":
            show_balance(acc_number, balance)
        elif choice == "2":
            balance = make_deposit(balance)
        elif choice == "3":
            balance = make_withdrawal(balance)
        elif choice == "4":
            break
        else:
            print("Invalid Choice. Try again.")

    print(f"Thank you for using our bank, {acc_holder}.")
    print(f"Final Balance: ${balance:>14,.2f}")


def show_balance(acc_number, balance):
    print("----------------------------------")
    print(f"Current Balance for {acc_number} is ${balance:>14,.2f}")
    print("----------------------------------")


def make_deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful.")
    print("----------------------------------")
    print(f"Current Balance: ${balance:>14,.2f}")
    print("----------------------------------")
    return balance


def make_withdrawal(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Error: Insufficient Funds!")
        print("Failed to withdraw.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print("----------------------------------")
        print(f"Current Balance: ${balance:>14,.2f}")
        print("----------------------------------")
    return balance


if __name__ == "__main__":
    main()
