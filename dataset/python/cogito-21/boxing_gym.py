class BoxingGym:
    def __init__(self):
        self.fighter_name = ""
        self.session_type = 0
        self.rent_gloves = False
        self.rent_wraps = False
        self.entry_fee = 0.0
        self.glove_fee = 0.0
        self.wrap_fee = 0.0
        self.total_due = 0.0

    def get_input(self):
        print("--- IRON FIST BOXING GYM ---")
        self.fighter_name = input("Fighter: ")
        
        while True:
            try:
                self.session_type = int(input("Entry (1=Open Gym $15, 2=Class $25, 3=Coach $80): "))
                if self.session_type in [1, 2, 3]:
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        self.rent_gloves = input("Rent Sparring Gloves ($5)? (Y/N): ").upper() == 'Y'
        self.rent_wraps = input("Buy Hand Wraps ($8)? (Y/N): ").upper() == 'Y'

    def calculate_fees(self):
        if self.session_type == 1:
            self.entry_fee = 15.00
        elif self.session_type == 2:
            self.entry_fee = 25.00
        elif self.session_type == 3:
            self.entry_fee = 80.00
        else:
            self.entry_fee = 15.00

        self.glove_fee = 5.00 if self.rent_gloves else 0.0
        self.wrap_fee = 8.00 if self.rent_wraps else 0.0
        self.total_due = self.entry_fee + self.glove_fee + self.wrap_fee

    def display_receipt(self):
        print("\n" + "="*40)
        print("             GYM CHECK-IN               ")
        print("="*40)
        print(f"Name: {self.fighter_name}")
        print("-"*40)
        print(f"Session Access:      ${self.entry_fee:.2f}")
        
        if self.rent_gloves:
            print(f"Glove Rental:        ${self.glove_fee:.2f}")
        if self.rent_wraps:
            print(f"Hand Wraps Purchase: ${self.wrap_fee:.2f}")
            
        print("-"*40)
        print(f"TOTAL BALANCE:       ${self.total_due:.2f}")
        print("="*40)

def main():
    gym = BoxingGym()
    gym.get_input()
    gym.calculate_fees()
    gym.display_receipt()

if __name__ == "__main__":
    main()
