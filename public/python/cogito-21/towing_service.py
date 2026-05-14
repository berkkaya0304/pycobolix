class TowingService:
    def __init__(self):
        self.driver_name = ""
        self.vehicle_type = 0
        self.tow_miles = 0.0
        self.needs_winch = False
        self.hook_fee = 0.0
        self.mile_rate = 0.0
        self.mile_total = 0.0
        self.winch_fee = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- HIGHWAY HERO TOWING ---")
        self.driver_name = input("Motorist: ")
        
        while True:
            try:
                self.vehicle_type = int(input("Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): "))
                if self.vehicle_type in (1, 2, 3):
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                self.tow_miles = float(input("Total Towing Miles: "))
                if self.tow_miles >= 0:
                    break
                print("Miles cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        winch_input = input("Did vehicle require ditch/snow winch-out? (Y/N): ").upper()
        self.needs_winch = winch_input == 'Y'

    def calculate_costs(self):
        if self.vehicle_type == 1:  # Car
            self.hook_fee = 75.00
            self.mile_rate = 3.50
        elif self.vehicle_type == 2:  # Heavy Truck
            self.hook_fee = 125.00
            self.mile_rate = 5.00
        elif self.vehicle_type == 3:  # Motorcycle
            self.hook_fee = 60.00
            self.mile_rate = 3.00
        else:  # Default to Car
            self.hook_fee = 75.00
            self.mile_rate = 3.50

        self.mile_total = self.tow_miles * self.mile_rate
        self.winch_fee = 50.00 if self.needs_winch else 0.0
        self.grand_total = self.hook_fee + self.mile_total + self.winch_fee

    def display_summary(self):
        print("\n" + "=" * 40)
        print("          TOW SERVICE SUMMARY           ")
        print("=" * 40)
        print(f"Motorist: {self.driver_name}")
        print("-" * 40)
        print(f"Base Hookup Fee:     ${self.hook_fee:,.2f}")
        print(f"Mileage ({self.tow_miles:.1f}m):     ${self.mile_total:,.2f}")
        
        if self.needs_winch:
            print(f"Winch-Out Surcharge: ${self.winch_fee:,.2f}")
        
        print("-" * 40)
        print(f"TOTAL TOW BILL:      ${self.grand_total:,.2f}")
        print("=" * 40)

    def run(self):
        self.get_input()
        self.calculate_costs()
        self.display_summary()

if __name__ == "__main__":
    service = TowingService()
    service.run()
