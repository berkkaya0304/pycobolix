class StudioSession:
    def __init__(self):
        self.artist_name = ""
        self.studio_hours = 0.0
        self.wants_engineer = False
        self.mastering_tracks = 0
        self.room_rate = 50.00
        self.engineer_rate = 40.00
        self.mastering_rate = 150.00

    def get_input(self):
        print("--- PLATINUM TRACKS STUDIO ---")
        self.artist_name = input("Artist / Band Name: ")
        
        while True:
            try:
                self.studio_hours = float(input("Studio Rental Duration (Hours): "))
                if self.studio_hours <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        engineer_input = input("Require Sound Engineer ($40/hr)? (Y/N): ").upper()
        self.wants_engineer = engineer_input == 'Y'
        
        while True:
            try:
                self.mastering_tracks = int(input("Number of Tracks to Master ($150 ea): "))
                if self.mastering_tracks < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def calculate_costs(self):
        room_total = self.studio_hours * self.room_rate
        engineer_total = self.studio_hours * self.engineer_rate if self.wants_engineer else 0
        mastering_total = self.mastering_tracks * self.mastering_rate
        grand_total = room_total + engineer_total + mastering_total
        return room_total, engineer_total, mastering_total, grand_total

    def display_invoice(self):
        room_total, engineer_total, mastering_total, grand_total = self.calculate_costs()
        
        print("\n" + "=" * 40)
        print("           STUDIO INVOICE               ")
        print("=" * 40)
        print(f"Artist: {self.artist_name}")
        print("-" * 40)
        print(f"Room Rental ({self.studio_hours} hrs): ${room_total:,.2f}")
        
        if self.wants_engineer:
            print(f"Sound Engineer Fee:     ${engineer_total:,.2f}")
        
        if self.mastering_tracks > 0:
            print(f"Audio Mastering ({self.mastering_tracks}):  ${mastering_total:,.2f}")
        
        print("-" * 40)
        print(f"TOTAL SESSION COST:     ${grand_total:,.2f}")
        print("=" * 40)

def main():
    session = StudioSession()
    session.get_input()
    session.display_invoice()

if __name__ == "__main__":
    main()
