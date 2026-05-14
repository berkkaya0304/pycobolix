class HotelBooking:
    def __init__(self):
        self.guest = ""
        self.season = ""
        self.view_type = 0
        self.nights = 0
        self.base_rate = 0.0
        self.season_mult = 0.0
        self.nightly_rate = 0.0
        self.subtotal = 0.0
        self.taxes = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- SEASIDE RESORT BOOKING ---")
        self.guest = input("Guest Name: ")
        
        while True:
            season = input("Season (P=Peak, O=Off-Peak): ").upper()
            if season in ('P', 'O'):
                self.season = season
                break
            print("Invalid season. Please enter 'P' for Peak or 'O' for Off-Peak.")
        
        while True:
            try:
                view = int(input("Room View (1=Std, 2=Ocean, 3=Suite): "))
                if view in (1, 2, 3):
                    self.view_type = view
                    break
                print("Invalid view type. Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                nights = int(input("Number of Nights: "))
                if nights > 0:
                    self.nights = nights
                    break
                print("Please enter a positive number of nights.")
            except ValueError:
                print("Please enter a valid number.")

    def calculate_stay(self):
        if self.view_type == 1:
            self.base_rate = 150.00
        elif self.view_type == 2:
            self.base_rate = 250.00
        elif self.view_type == 3:
            self.base_rate = 500.00
        else:
            self.base_rate = 150.00

        self.season_mult = 1.5 if self.season == 'P' else 1.0
        self.nightly_rate = self.base_rate * self.season_mult
        self.subtotal = self.nightly_rate * self.nights
        self.taxes = self.subtotal * 0.125
        self.grand_total = self.subtotal + self.taxes

    def print_confirmation(self):
        print("\n" + "=" * 36)
        print("       BOOKING CONFIRMATION         ")
        print("=" * 36)
        print(f"Guest:  {self.guest}")
        print(f"Nights: {self.nights}")
        print("-" * 36)
        print(f"Est. Nightly Rate: ${self.nightly_rate:,.2f}")
        print(f"Room Subtotal:     ${self.subtotal:,.2f}")
        print(f"Taxes (12.5%):     ${self.taxes:,.2f}")
        print("-" * 36)
        print(f"TOTAL STAY COST:   ${self.grand_total:,.2f}")
        print("=" * 36)

    def run(self):
        self.get_input()
        self.calculate_stay()
        self.print_confirmation()

if __name__ == "__main__":
    booking = HotelBooking()
    booking.run()
