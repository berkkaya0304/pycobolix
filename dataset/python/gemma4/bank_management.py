from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("Welcome to Simple Bank System")
    
    acc_number = input("Enter Account Number (10 digits): ")
    acc_holder = input("Enter Account Holder Name: ")
    
    try:
        balance = Decimal(input("Enter Initial Deposit Amount: "))
    except Exception:
        balance = Decimal('0.00')

    user_choice = 'Y'
    
    while user_choice != '4':
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        user_choice = input("Enter Your Choice (1-4): ")

        if user_choice == '1':
            show_balance(acc_number, balance)
        elif user_choice == '2':
            balance = make_deposit(balance)
        elif user_choice == '3':
            balance = make_withdrawal(balance)
        elif user_choice == '4':
            continue
        else:
            print("Invalid Choice. Try again.")

    print(f"Thank you for using our bank, {acc_holder}.")
    print(f"Final Balance: {format_currency(balance)}")

def show_balance(acc_number, balance):
    print("----------------------------------")
    print(f"Current Balance for {acc_number} is {format_currency(balance)}")
    print("----------------------------------")

def make_deposit(balance):
    try:
        amount = Decimal(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful.")
        show_balance("N/A", balance) # Simplified for logic flow
    except Exception:
        print("Invalid amount entered.")
    return balance

def make_withdrawal(balance):
    try:
        amount = Decimal(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Error: Insufficient Funds!")
            print("Failed to withdraw.")
        else:
            balance -= amount
            print("Withdrawal successful.")
            show_balance("N/A", balance)
    except Exception:
        print("Invalid amount entered.")
    return balance

if __name__ == "__main__":
    main()
