def bank_management():
    account_info = {
        'acc_number': '',
        'acc_holder': '',
        'balance': 0.0
    }

    print("Welcome to Simple Bank System")
    account_info['acc_number'] = input("Enter Account Number (10 digits): ").strip()
    account_info['acc_holder'] = input("Enter Account Holder Name: ").strip()
    account_info['balance'] = float(input("Enter Initial Deposit Amount: "))

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        user_choice = input("Enter Your Choice (1-4): ").strip()

        if user_choice == '1':
            show_balance(account_info)
        elif user_choice == '2':
            make_deposit(account_info)
        elif user_choice == '3':
            make_withdrawal(account_info)
        elif user_choice == '4':
            break
        else:
            print("Invalid Choice. Try again.")

    print(f"Thank you for using our bank, {account_info['acc_holder']}.")
    print(f"Final Balance: ${account_info['balance']:,.2f}")

def show_balance(account_info):
    print("----------------------------------")
    print(f"Current Balance for {account_info['acc_number']} is ${account_info['balance']:,.2f}")
    print("----------------------------------")

def make_deposit(account_info):
    try:
        trans_amount = float(input("Enter amount to deposit: "))
        account_info['balance'] += trans_amount
        print("Deposit successful.")
        show_balance(account_info)
    except ValueError:
        print("Invalid amount entered.")

def make_withdrawal(account_info):
    try:
        trans_amount = float(input("Enter amount to withdraw: "))
        if trans_amount > account_info['balance']:
            print("Error: Insufficient Funds!")
            print("Failed to withdraw.")
        else:
            account_info['balance'] -= trans_amount
            print("Withdrawal successful.")
            show_balance(account_info)
    except ValueError:
        print("Invalid amount entered.")

if __name__ == "__main__":
    bank_management()
