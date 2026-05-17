class PestControl:
    def __init__(self):
        self.client_name = ""
        self.sq_footage = 0
        self.pest_type = 0
        self.monthly_plan = False
        self.base_sqft = 0.05
        self.area_charge = 0.0
        self.pest_surchg = 0.0
        self.gross_amt = 0.0
        self.sub_discount = 0.0
        self.final_due = 0.0

    def get_input(self):
        print("--- BUG BUSTERS EXTERMINATING ---")
        self.client_name = input("Property Owner: ")
        self.sq_footage = int(input("Square Footage of Property: "))
        print("Pest (1=Insects, 2=Rodent +$50, 3=Termite +$200):")
        self.pest_type = int(input())
        monthly_plan_input = input("Enroll in Monthly Plan (20% Off)? (Y/N): ").upper()
        self.monthly_plan = monthly_plan_input == 'Y'

    def calculate_charges(self):
        self.area_charge = self.sq_footage * self.base_sqft
        
        if self.pest_type == 1:
            self.pest_surchg = 0.0
        elif self.pest_type == 2:
            self.pest_surchg = 50.0
        elif self.pest_type == 3:
            self.pest_surchg = 200.0
        else:
            self.pest_surchg = 0.0

        self.gross_amt = self.area_charge + self.pest_surchg

        if self.monthly_plan:
            self.sub_discount = self.gross_amt * 0.20
        else:
            self.sub_discount = 0.0

        self.final_due = self.gross_amt - self.sub_discount

    def display_invoice(self):
        print("\n" + "="*40)
        print("           SERVICE INVOICE              ")
        print("="*40)
        print(f"Property: {self.client_name} ({self.sq_footage} sqft)")
        print("-"*40)
        print(f"Property Area Charge: ${self.area_charge:,.2f}")
        
        if self.pest_surchg > 0:
            print(f"Target Pest Surcharge: ${self.pest_surchg:,.2f}")
            
        if self.monthly_plan:
            print(f"Service Plan Disc:  -${self.sub_discount:,.2f}")
            
        print("-"*40)
        print(f"TOTAL TREATMENT:      ${self.final_due:,.2f}")
        print("="*40)

def main():
    pest_control = PestControl()
    pest_control.get_input()
    pest_control.calculate_charges()
    pest_control.display_invoice()

if __name__ == "__main__":
    main()
