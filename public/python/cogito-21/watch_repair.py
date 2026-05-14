class WatchRepair:
    def __init__(self):
        self.client_name = ""
        self.watch_brand = ""
        self.fix_battery = False
        self.fix_strap = False
        self.fix_polish = False
        self.is_luxury = False
        self.batt_fee = 0.0
        self.strap_fee = 0.0
        self.polish_fee = 0.0
        self.sub_total = 0.0
        self.luxury_surcharge = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- TIC-TOCK WATCH REPAIR ---")
        self.client_name = input("Client: ")
        self.watch_brand = input("Watch Brand: ")
        luxury_input = input("Is this a luxury timepiece (+25%)? (Y/N): ").upper()
        self.is_luxury = luxury_input == 'Y'
        battery_input = input("Replace Battery ($20)? (Y/N): ").upper()
        self.fix_battery = battery_input == 'Y'
        strap_input = input("Replace/Fix Strap ($35)? (Y/N): ").upper()
        self.fix_strap = strap_input == 'Y'
        polish_input = input("Surface Polish ($45)? (Y/N): ").upper()
        self.fix_polish = polish_input == 'Y'

    def calculate_fees(self):
        if self.fix_battery:
            self.batt_fee = 20.0
        if self.fix_strap:
            self.strap_fee = 35.0
        if self.fix_polish:
            self.polish_fee = 45.0

        self.sub_total = self.batt_fee + self.strap_fee + self.polish_fee

        if self.is_luxury:
            self.luxury_surcharge = self.sub_total * 0.25

        self.grand_total = self.sub_total + self.luxury_surcharge

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("            SERVICE TICKET              ")
        print("=" * 40)
        print(f"Client: {self.client_name}")
        print(f"Brand:  {self.watch_brand}")
        print("-" * 40)

        if self.fix_battery:
            print(f"Battery Service:    ${self.batt_fee:>6.2f}")
        if self.fix_strap:
            print(f"Strap Replacement:  ${self.strap_fee:>6.2f}")
        if self.fix_polish:
            print(f"Polishing Service:  ${self.polish_fee:>6.2f}")

        print("-" * 40)
        if self.is_luxury:
            print(f"Luxury Brand Fee:   ${self.luxury_surcharge:>6.2f}")
            print("-" * 40)

        print(f"TOTAL SERVICE COST: ${self.grand_total:>6.2f}")
        print("=" * 40)

def main():
    repair = WatchRepair()
    repair.get_input()
    repair.calculate_fees()
    repair.display_invoice()

if __name__ == "__main__":
    main()
