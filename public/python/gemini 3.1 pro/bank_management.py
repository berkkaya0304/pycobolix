def main():
    print("Welcome to Simple Bank System")
    acc_number = input("Enter Account Number (10 digits): ")
    acc_holder = input("Enter Account Holder Name: ")
    try:
        balance = float(input("Enter Initial Deposit Amount: "))
    except ValueError:
        balance = 0.0
    
    while True:
        print(" ")
        print("--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        user_choice = input("Enter Your Choice (1-4): ").strip()
        
        if user_choice == '1':
            print("----------------------------------")
            print(f"Current Balance for {acc_number} is ${balance:14.2f}")
            print("----------------------------------")
        elif user_choice == '2':
            try:
                trans_amount = float(input("Enter amount to deposit: "))
                balance += trans_amount
                print("Deposit successful.")
                print("----------------------------------")
                print(f"Current Balance for {acc_number} is ${balance:14.2f}")
                print("----------------------------------")
            except ValueError:
                print("Invalid input.")
        elif user_choice == '3':
            try:
                trans_amount = float(input("Enter amount to withdraw: "))
                if trans_amount > balance:
                    print("Error: Insufficient Funds!")
                    print("Failed to withdraw.")
                else:
                    balance -= trans_amount
                    print("Withdrawal successful.")
                    print("----------------------------------")
                    print(f"Current Balance for {acc_number} is ${balance:14.2f}")
                    print("----------------------------------")
            except ValueError:
                print("Invalid input.")
        elif user_choice == '4':
            break
        else:
            print("Invalid Choice. Try again.")

    print(f"Thank you for using our bank, {acc_holder}.")
    print(f"Final Balance: ${balance:14.2f}")

if __name__ == "__main__":
    main()
