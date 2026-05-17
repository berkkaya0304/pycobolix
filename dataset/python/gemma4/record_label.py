from decimal import Decimal, ROUND_HALF_UP

def main():
    # Constants (Fees)
    ROOM_RATE = Decimal('50.00')
    ENG_RATE = Decimal('40.00')
    MASTER_RATE = Decimal('150.00')

    print("--- PLATINUM TRACKS STUDIO ---")
    
    artist_name = input("Artist / Band Name: ")
    
    try:
        studio_hours = Decimal(input("Studio Rental Duration (Hours): "))
        engineer_req = input("Require Sound Engineer ($40/hr)? (Y/N): ").strip().upper()
        mastering_trk = int(input("Number of Tracks to Master ($150 ea): "))
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return

    # Calculations
    room_tot = studio_hours * ROOM_RATE
    eng_tot = Decimal('0.00')
    if engineer_req == 'Y':
        eng_tot = studio_hours * ENG_RATE
    
    master_tot = Decimal(mastering_trk) * MASTER_RATE
    grand_tot = room_tot + eng_tot + master_tot

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n")
    print("========================================")
    print("           STUDIO INVOICE               ")
    print("========================================")
    print(f"Artist: {artist_name}")
    print("----------------------------------------")
    print(f"Room Rental ({studio_hours} hrs): {format_currency(room_tot)}")
    
    if engineer_req == 'Y':
        print(f"Sound Engineer Fee:     {format_currency(eng_tot)}")
    
    if mastering_trk > 0:
        print(f"Audio Mastering ({mastering_trk}):  {format_currency(master_tot)}")
        
    print("----------------------------------------")
    print(f"TOTAL SESSION COST:     {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    main()
