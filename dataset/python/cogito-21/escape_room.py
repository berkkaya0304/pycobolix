class EscapeRoom:
    def __init__(self):
        self.group_name = ""
        self.num_players = 0
        self.difficulty = 0
        self.is_weekend = False
        self.base_ticket = 25.00
        self.diff_surcharge = 0.00
        self.ticket_price = 0.00
        self.room_total = 0.00
        self.weekend_fee = 0.00
        self.final_bill = 0.00

    def get_input(self):
        print("--- ENIGMA ESCAPE ROOMS ---")
        self.group_name = input("Group/Team Name: ")
        
        while True:
            try:
                self.num_players = int(input("Number of Players: "))
                if self.num_players <= 0:
                    print("Please enter a positive number of players.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.difficulty = int(input("Room Difficulty (1=Easy, 2=Med, 3=Hard +$5): "))
                if self.difficulty not in [1, 2, 3]:
                    print("Please enter 1, 2, or 3 for difficulty.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number (1, 2, or 3).")
        
        while True:
            weekend_input = input("Is booking on Weekend (Fri-Sun)? (Y/N): ").upper()
            if weekend_input in ['Y', 'N']:
                self.is_weekend = (weekend_input == 'Y')
                break
            print("Please enter Y or N.")

    def calculate_costs(self):
        if self.difficulty == 3:
            self.diff_surcharge = 5.00
        
        self.ticket_price = self.base_ticket + self.diff_surcharge
        self.room_total = self.num_players * self.ticket_price
        
        if self.is_weekend:
            self.weekend_fee = 20.00
        
        self.final_bill = self.room_total + self.weekend_fee

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("          BOOKING CONFIRMATION          ")
        print("=" * 40)
        print(f"Team: {self.group_name} ({self.num_players} players)")
        print("-" * 40)
        print(f"Price Per Ticket:    ${self.ticket_price:.2f}")
        print(f"Base Room Charge:    ${self.room_total:,.2f}")
        
        if self.weekend_fee > 0:
            print(f"Weekend Premium:     ${self.weekend_fee:.2f}")
        
        print("-" * 40)
        print(f"TOTAL AMOUNT DUE:    ${self.final_bill:,.2f}")
        print("=" * 40)

def main():
    booking = EscapeRoom()
    booking.get_input()
    booking.calculate_costs()
    booking.display_receipt()

if __name__ == "__main__":
    main()
