class CarDealership:
    def __init__(self):
        self.buyer_name = ""
        self.base_model = 0
        self.trim_level = 0
        self.down_payment = 0.0
        self.loan_months = 0
        self.base_price = 0.0
        self.trim_upcharge = 0.0
        self.total_veh_price = 0.0
        self.financed_amt = 0.0
        self.interest_rate = 0.05
        self.total_interest = 0.0
        self.total_payback = 0.0
        self.monthly_payment = 0.0

    def get_input(self):
        print("--- PLATINUM AUTO SALES ---")
        self.buyer_name = input("Buyer Name: ")
        
        while True:
            try:
                self.base_model = int(input("Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): "))
                if self.base_model in [1, 2, 3]:
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.trim_level = int(input("Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): "))
                if self.trim_level in [1, 2, 3]:
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.down_payment = float(input("Down Payment Amount ($): "))
                if self.down_payment >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.loan_months = int(input("Loan Term (Months): "))
                if self.loan_months > 0:
                    break
                print("Please enter a positive number of months.")
            except ValueError:
                print("Please enter a valid number.")

    def price_calc(self):
        if self.base_model == 1:
            self.base_price = 25000.00
        elif self.base_model == 2:
            self.base_price = 35000.00
        elif self.base_model == 3:
            self.base_price = 45000.00
        else:
            self.base_price = 25000.00

        if self.trim_level == 1:
            self.trim_upcharge = 0.0
        elif self.trim_level == 2:
            self.trim_upcharge = 5000.00
        elif self.trim_level == 3:
            self.trim_upcharge = 10000.00
        else:
            self.trim_upcharge = 0.0

        self.total_veh_price = self.base_price + self.trim_upcharge

    def finance_calc(self):
        self.financed_amt = self.total_veh_price - self.down_payment
        if self.financed_amt < 0:
            self.financed_amt = 0.0
        
        self.total_interest = self.financed_amt * self.interest_rate * (self.loan_months / 12)
        self.total_payback = self.financed_amt + self.total_interest
        self.monthly_payment = self.total_payback / self.loan_months if self.loan_months > 0 else 0.0

    def output_sheet(self):
        print("\n" + "=" * 40)
        print("       VEHICLE PURCHASE SHEET           ")
        print("=" * 40)
        print(f"Buyer: {self.buyer_name}")
        print("-" * 40)
        print(f"Base Price:       ${self.base_price:,.2f}")
        print(f"Trim Upcharge:    ${self.trim_upcharge:,.2f}")
        print(f"Total Vehicle:    ${self.total_veh_price:,.2f}")
        print("-" * 40)
        print(f"Down Payment:    -${self.down_payment:,.2f}")
        print(f"Amount Financed:  ${self.financed_amt:,.2f}")
        print("-" * 40)
        print(f"EST. MONTHLY PMT: ${self.monthly_payment:,.2f}")
        print("=" * 40)

    def run(self):
        self.get_input()
        self.price_calc()
        self.finance_calc()
        self.output_sheet()

if __name__ == "__main__":
    dealer = CarDealership()
    dealer.run()
