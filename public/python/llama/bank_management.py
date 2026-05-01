# BANK-MANAGEMENT - Simple Bank System
# Converted from COBOL to Python

def show_balance(acc_number, balance):
    print("----------------------------------")
    print(f"Current Balance for {acc_number} is ${balance:,.2f}")
    print("----------------------------------")

def main():
    print("Welcome to Simple Bank System")
    acc_number = input("Enter Account Number (10 digits): ")
    acc_holder = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit Amount: "))

    user_choice = ''
    while user_choice != '4':
        print("")
        print("--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        user_choice = input("Enter Your Choice (1-4): ").strip()

        if user_choice == '1':
            show_balance(acc_number, balance)
        elif user_choice == '2':
            trans_amount = float(input("Enter amount to deposit: "))
            balance += trans_amount
            print("Deposit successful.")
            show_balance(acc_number, balance)
        elif user_choice == '3':
            trans_amount = float(input("Enter amount to withdraw: "))
            if trans_amount > balance:
                print("Error: Insufficient Funds!")
                print("Failed to withdraw.")
            else:
                balance -= trans_amount
                print("Withdrawal successful.")
                show_balance(acc_number, balance)
        elif user_choice == '4':
            break
        else:
            print("Invalid Choice. Try again.")

    print(f"Thank you for using our bank, {acc_holder}.")
    print(f"Final Balance: ${balance:,.2f}")

if __name__ == "__main__":
    main()
