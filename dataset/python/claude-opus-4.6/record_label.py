"""
Platinum Tracks Studio - Record Label
Converted from COBOL (record_label.cbl) to Python
"""


def main():
    room_rate = 50.00
    eng_rate = 40.00
    master_rate = 150.00

    print("--- PLATINUM TRACKS STUDIO ---")
    artist_name = input("Artist / Band Name: ")
    studio_hours = float(input("Studio Rental Duration (Hours): "))
    engineer_req = input("Require Sound Engineer ($40/hr)? (Y/N): ").strip().upper()
    mastering_trk = int(input("Number of Tracks to Master ($150 ea): "))

    room_tot = studio_hours * room_rate
    eng_tot = studio_hours * eng_rate if engineer_req == "Y" else 0.0
    master_tot = mastering_trk * master_rate
    grand_tot = room_tot + eng_tot + master_tot

    print()
    print("========================================")
    print("           STUDIO INVOICE               ")
    print("========================================")
    print(f"Artist: {artist_name}")
    print("----------------------------------------")
    print(f"Room Rental ({studio_hours} hrs): ${room_tot:>9,.2f}")
    if engineer_req == "Y":
        print(f"Sound Engineer Fee:     ${eng_tot:>9,.2f}")
    if mastering_trk > 0:
        print(f"Audio Mastering ({mastering_trk}):  ${master_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SESSION COST:     ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
