class SportsClub:
    def __init__(self):
        self.registry_fee = 150.00
        self.monthly_fee = 0.0
        self.equip_fee = 0.0
        self.sub_total = 0.0
        self.total_bill = 0.0
        self.member_name = ""
        self.sport_dept = ""
        self.months_mbr = 1
        self.rent_equip = False

    def get_input(self):
        print("--- ELITE SPORTS CLUB REGISTRATION ---")
        self.member_name = input("Member Name: ")
        
        while True:
            self.sport_dept = input("Sport (T=Tennis, G=Golf, S=Swimming): ").upper()
            if self.sport_dept in ['T', 'G', 'S']:
                break
            print("Invalid sport. Please enter T, G, or S.")
        
        while True:
            try:
                self.months_mbr = int(input("Months to prepay (1-12): "))
                if 1 <= self.months_mbr <= 12:
                    break
                print("Please enter a number between 1 and 12.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            equip_input = input("Rent Club Equipment ($30/mo)? (Y/N): ").upper()
            if equip_input in ['Y', 'N']:
                self.rent_equip = (equip_input == 'Y')
                break
            print("Please enter Y or N.")

    def process_registration(self):
        sport_fees = {
            'T': 100.00,
            'G': 250.00,
            'S': 75.00
        }
        self.monthly_fee = sport_fees.get(self.sport_dept, 100.00)
        
        if self.rent_equip:
            self.equip_fee = 30.00
        
        self.sub_total = (self.monthly_fee * self.months_mbr) + (self.equip_fee * self.months_mbr)
        self.total_bill = self.sub_total + self.registry_fee

    def output_invoice(self):
        def format_currency(amount):
            return f"${amount:,.2f}"

        print("\n" + "=" * 40)
        print("           CLUB MEMBERSHIP             ")
        print("=" * 40)
        print(f"Welcome, {self.member_name}")
        print(f"Prepaid Term: {self.months_mbr} months")
        print("-" * 40)
        print(f"One-Time Joining Fee: {format_currency(self.registry_fee)}")
        
        membership_total = self.monthly_fee * self.months_mbr
        print(f"Membership Dues:      {format_currency(membership_total)}")
        
        if self.rent_equip:
            equipment_total = self.equip_fee * self.months_mbr
            print(f"Equipment Rental:     {format_currency(equipment_total)}")
        
        print("-" * 40)
        print(f"TOTAL REGISTRATION:   {format_currency(self.total_bill)}")
        print("=" * 40)

def main():
    club = SportsClub()
    club.get_input()
    club.process_registration()
    club.output_invoice()

if __name__ == "__main__":
    main()
