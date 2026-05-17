class PotteryClass:
    def __init__(self):
        self.student_name = ""
        self.clay_lbs = 0.0
        self.ticket_type = 0
        self.kiln_firing = 0
        self.studio_fee = 0.0
        self.clay_fee = 0.0
        self.kiln_fee = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- CLAY CREATIONS STUDIO ---")
        self.student_name = input("Student Name: ").strip()
        
        while True:
            try:
                ticket = int(input("Session (1=Drop-In $35, 2=Member $0): ").strip())
                if ticket in (1, 2):
                    self.ticket_type = ticket
                    break
                print("Please enter 1 or 2")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                clay = float(input("Clay Required (Lbs, $2.50/lb): ").strip())
                if clay >= 0:
                    self.clay_lbs = clay
                    break
                print("Please enter a non-negative number")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                kiln = int(input("Items to Kiln Fire/Glaze ($5.00 ea): ").strip())
                if kiln >= 0:
                    self.kiln_firing = kiln
                    break
                print("Please enter a non-negative integer")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def calculate_costs(self):
        self.studio_fee = 35.00 if self.ticket_type == 1 else 0.0
        self.clay_fee = self.clay_lbs * 2.50
        self.kiln_fee = self.kiln_firing * 5.00
        self.grand_total = self.studio_fee + self.clay_fee + self.kiln_fee

    def display_receipt(self):
        print("\n" + "="*40)
        print("            STUDIO WORKSHOP             ")
        print("="*40)
        print(f"Maker: {self.student_name}")
        print("-"*40)
        print(f"Studio Access Fee:  ${self.studio_fee:7.2f}")
        
        if self.clay_lbs > 0:
            print(f"Clay ({self.clay_lbs} lbs):      ${self.clay_fee:7.2f}")
        
        if self.kiln_firing > 0:
            print(f"Kiln Firing ({self.kiln_firing}):   ${self.kiln_fee:7.2f}")
        
        print("-"*40)
        print(f"TOTAL COST:         ${self.grand_total:7.2f}")
        print("="*40)

def main():
    pottery = PotteryClass()
    pottery.get_input()
    pottery.calculate_costs()
    pottery.display_receipt()

if __name__ == "__main__":
    main()
