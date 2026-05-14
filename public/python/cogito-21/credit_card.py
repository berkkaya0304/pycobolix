class CreditCardStatement:
    def __init__(self):
        self.card_number = ""
        self.cardholder = ""
        self.prev_balance = 0.0
        self.new_charges = 0.0
        self.payments_made = 0.0
        self.apr_rate = 19.99
        self.unpaid_bal = 0.0
        self.interest_chg = 0.0
        self.new_balance = 0.0
        self.min_payment = 0.0

    def get_input(self):
        print("--- CREDIT CARD STATEMENT GEN ---")
        self.card_number = input("Card Number: ")
        self.cardholder = input("Cardholder Name: ")
        self.prev_balance = float(input("Previous Statement Balance: "))
        self.payments_made = float(input("Payments Made This Cycle: "))
        self.new_charges = float(input("New Purchase Charges: "))

    def calculate_statement(self):
        self.unpaid_bal = self.prev_balance - self.payments_made
        
        if self.unpaid_bal > 0:
            self.interest_chg = self.unpaid_bal * (self.apr_rate / 100 / 12)
        
        self.new_balance = self.unpaid_bal + self.new_charges + self.interest_chg
        
        self.min_payment = self.new_balance * 0.03
        if self.min_payment < 35.00 and self.new_balance >= 35.00:
            self.min_payment = 35.00
        elif self.new_balance < 35.00:
            self.min_payment = self.new_balance

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def print_statement(self):
        print("\n=========================================")
        print("       MONTHLY ACCOUNT STATEMENT         ")
        print("=========================================")
        print(f"Card: **** **** **** {self.card_number[-4:]}")
        print(f"Name: {self.cardholder}")
        print("-----------------------------------------")
        print(f"Previous Balance:     {self.format_currency(self.prev_balance)}")
        print(f"Payments / Credits: -{self.format_currency(self.payments_made)}")
        print(f"New Purchases:      +{self.format_currency(self.new_charges)}")
        print(f"Interest Charged:   +{self.format_currency(self.interest_chg)}")
        print("-----------------------------------------")
        print(f"NEW BALANCE:         {self.format_currency(self.new_balance)}")
        print(f"MINIMUM PAYMENT DUE: {self.format_currency(self.min_payment)}")
        print("=========================================")

def main():
    statement = CreditCardStatement()
    statement.get_input()
    statement.calculate_statement()
    statement.print_statement()

if __name__ == "__main__":
    main()
