class PhotoStudio:
    def __init__(self):
        self.client_name = ""
        self.session_type = 0
        self.phy_prints = 0
        self.wants_digital = False
        self.sitting_fee = 0.0
        self.print_fee = 0.0
        self.digital_fee = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- LENS APERTURE STUDIO ---")
        self.client_name = input("Client: ")
        
        while True:
            try:
                session_input = input("Session (1=Headshot $99, 2=Family $150, 3=Event $300): ").strip()
                self.session_type = int(session_input)
                if self.session_type in (1, 2, 3):
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                prints_input = input("Physical Prints Wanted ($15 per sheet): ").strip()
                self.phy_prints = int(prints_input)
                if self.phy_prints >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            digital_input = input("USB Drive with Digital Masters ($50)? (Y/N): ").strip().upper()
            if digital_input in ('Y', 'N'):
                self.wants_digital = (digital_input == 'Y')
                break
            print("Please enter Y or N.")

    def calculate_fees(self):
        session_fees = {1: 99.00, 2: 150.00, 3: 300.00}
        self.sitting_fee = session_fees.get(self.session_type, 99.00)
        self.print_fee = self.phy_prints * 15.00
        self.digital_fee = 50.00 if self.wants_digital else 0.00
        self.grand_total = self.sitting_fee + self.print_fee + self.digital_fee

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("          STUDIO INVOICE                ")
        print("=" * 40)
        print(f"Client: {self.client_name}")
        print("-" * 40)
        print(f"Session/Sitting Fee: ${self.sitting_fee:,.2f}")
        
        if self.print_fee > 0:
            print(f"Physical Prints ({self.phy_prints}):  ${self.print_fee:,.2f}")
        
        if self.digital_fee > 0:
            print(f"Digital Masters USB: ${self.digital_fee:,.2f}")
        
        print("-" * 40)
        print(f"TOTAL CHARGED:       ${self.grand_total:,.2f}")
        print("=" * 40)

def main():
    studio = PhotoStudio()
    studio.get_input()
    studio.calculate_fees()
    studio.display_invoice()

if __name__ == "__main__":
    main()
