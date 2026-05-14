class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.account_holder = ""
        self.balance = 0.0

    def format_balance(self):
        return f"${self.balance:,.2f}"

    def show_balance(self):
        print("----------------------------------")
        print(f"Current Balance for {self.account_number} is {self.format_balance()}")
        print("----------------------------------")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")
        self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient Funds!")
            print("Failed to withdraw.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            self.show_balance()

def main():
    account = BankAccount()
    
    print("Welcome to Simple Bank System")
    account.account_number = input("Enter Account Number (10 digits): ")
    account.account_holder = input("Enter Account Holder Name: ")
    account.balance = float(input("Enter Initial Deposit Amount: "))
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        choice = input("Enter Your Choice (1-4): ")
        
        if choice == '1':
            account.show_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == '4':
            break
        else:
            print("Invalid Choice. Try again.")
    
    print(f"Thank you for using our bank, {account.account_holder}.")
    print(f"Final Balance: {account.format_balance()}")

if __name__ == "__main__":
    main()
