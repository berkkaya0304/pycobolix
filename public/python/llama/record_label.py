# RECORD-LABEL - Platinum Tracks Studio
# Converted from COBOL to Python

def main():
    ROOM_RATE = 50.00
    ENG_RATE = 40.00
    MASTER_RATE = 150.00

    print("--- PLATINUM TRACKS STUDIO ---")
    artist_name = input("Artist / Band Name: ")
    studio_hours = float(input("Studio Rental Duration (Hours): "))
    engineer_req = input("Require Sound Engineer ($40/hr)? (Y/N): ").strip().upper()
    mastering_trk = int(input("Number of Tracks to Master ($150 ea): "))

    room_tot = studio_hours * ROOM_RATE
    eng_tot = studio_hours * ENG_RATE if engineer_req == 'Y' else 0.0
    master_tot = mastering_trk * MASTER_RATE
    grand_tot = room_tot + eng_tot + master_tot

    print("")
    print("========================================")
    print("           STUDIO INVOICE               ")
    print("========================================")
    print(f"Artist: {artist_name}")
    print("----------------------------------------")
    print(f"Room Rental ({studio_hours} hrs): ${room_tot:,.2f}")
    if engineer_req == 'Y':
        print(f"Sound Engineer Fee:     ${eng_tot:,.2f}")
    if mastering_trk > 0:
        print(f"Audio Mastering ({mastering_trk}):  ${master_tot:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SESSION COST:     ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
