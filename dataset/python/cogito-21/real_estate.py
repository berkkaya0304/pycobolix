class MortgageCalculator:
    def __init__(self):
        self.property_address = ""
        self.property_price = 0.0
        self.down_payment_pct = 0.0
        self.down_payment_amt = 0.0
        self.loan_principal = 0.0
        self.interest_rate = 5.50
        self.loan_years = 30
        self.total_interest = 0.0
        self.total_payback = 0.0
        self.total_months = 0
        self.monthly_payment = 0.0
        self.pmi_fee = 0.0

    def get_input(self):
        print("--- MORTGAGE CALCULATOR ---")
        self.property_address = input("Property Address: ")
        self.property_price = float(input("Property Purchase Price ($): "))
        self.down_payment_pct = float(input("Down Payment Percentage (e.g., 20 for 20%): "))
        self.interest_rate = float(input("Interest Rate (e.g., 5.5 for 5.5%): "))
        self.loan_years = int(input("Loan Term (Years): "))

    def process_loan(self):
        self.down_payment_amt = self.property_price * (self.down_payment_pct / 100)
        self.loan_principal = self.property_price - self.down_payment_amt
        
        if self.down_payment_pct < 20:
            self.pmi_fee = (self.loan_principal * 0.01) / 12
            print("*** WARNING: PMI applies (Down Payment < 20%) ***")
        
        self.total_interest = self.loan_principal * (self.interest_rate / 100) * self.loan_years
        self.total_payback = self.loan_principal + self.total_interest
        self.total_months = self.loan_years * 12
        self.monthly_payment = (self.total_payback / self.total_months) + self.pmi_fee

    def format_currency(self, amount):
        return "${:,.2f}".format(amount)

    def print_breakdown(self):
        print("\n=============================================")
        print("        MORTGAGE BREAKDOWN ESTIMATE          ")
        print("=============================================")
        print(f"Address: {self.property_address}")
        print("---------------------------------------------")
        print(f"Purchase Price:   {self.format_currency(self.property_price)}")
        print(f"Down Payment:     -{self.format_currency(self.down_payment_amt)}")
        print(f"Loan Principal:   {self.format_currency(self.loan_principal)}")
        print("---------------------------------------------")
        print(f"Total Interest:   {self.format_currency(self.total_interest)}")
        print(f"Total Repayment:  {self.format_currency(self.total_payback)}")
        print("---------------------------------------------")
        if self.pmi_fee > 0:
            print(f"Monthly PMI Fee:  {self.format_currency(self.pmi_fee)}")
        print(f"EST. MONTHLY PMT: {self.format_currency(self.monthly_payment)}")
        print("=============================================")

def main():
    calculator = MortgageCalculator()
    calculator.get_input()
    calculator.process_loan()
    calculator.print_breakdown()

if __name__ == "__main__":
    main()
