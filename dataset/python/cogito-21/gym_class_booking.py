class GymClassBooking:
    def __init__(self):
        self.member_name = ""
        self.class_selection = 0
        self.guest_passes = 0
        self.towel_rental = 'N'
        self.class_fee = 0.0
        self.guest_fee = 0.0
        self.towel_fee = 0.0
        self.total_charge = 0.0

    def get_input(self):
        print("--- FIT-LIFE CLASS BOOKING ---")
        self.member_name = input("Member Name: ")
        
        while True:
            try:
                self.class_selection = int(input("Class (1=Yoga $15, 2=Spin $20, 3=Pilates $25): "))
                if self.class_selection in (1, 2, 3):
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.guest_passes = int(input("Number of Non-Member Guests ($10 ea): "))
                if self.guest_passes >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            self.towel_rental = input("Rent Premium Towel Service ($3)? (Y/N): ").upper()
            if self.towel_rental in ('Y', 'N'):
                break
            print("Please enter Y or N.")

    def calculate_fees(self):
        class_fees = {1: 15.00, 2: 20.00, 3: 25.00}
        self.class_fee = class_fees.get(self.class_selection, 15.00)
        self.guest_fee = self.guest_passes * 10.00
        self.towel_fee = 3.00 if self.towel_rental == 'Y' else 0.00
        self.total_charge = self.class_fee + self.guest_fee + self.towel_fee

    def display_receipt(self):
        print("\n" + "="*40)
        print("           CLASS RESERVATION            ")
        print("="*40)
        print(f"Member: {self.member_name}")
        print("-"*40)
        print(f"Class Base Fee:       ${self.class_fee:.2f}")
        
        if self.guest_passes > 0:
            print(f"Guest Passes ({self.guest_passes}):      ${self.guest_fee:.2f}")
        
        if self.towel_rental == 'Y':
            print(f"Towel Service Option: ${self.towel_fee:.2f}")
        
        print("-"*40)
        print(f"TOTAL CHARGED:        ${self.total_charge:.2f}")
        print("="*40)

def main():
    booking = GymClassBooking()
    booking.get_input()
    booking.calculate_fees()
    booking.display_receipt()

if __name__ == "__main__":
    main()
