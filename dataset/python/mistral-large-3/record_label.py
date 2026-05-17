def record_label():
    # Studio info
    artist_name = input("--- PLATINUM TRACKS STUDIO ---\nArtist / Band Name: ").ljust(20)[:20]
    studio_hours = float(input("Studio Rental Duration (Hours): "))
    engineer_req = input("Require Sound Engineer ($40/hr)? (Y/N): ").upper()
    mastering_trk = int(input("Number of Tracks to Master ($150 ea): "))

    # Fees
    room_rate = 50.00
    eng_rate = 40.00
    master_rate = 150.00

    # Calculate totals
    room_tot = studio_hours * room_rate
    eng_tot = studio_hours * eng_rate if engineer_req == 'Y' else 0.0
    master_tot = mastering_trk * master_rate
    grand_tot = room_tot + eng_tot + master_tot

    # Display invoice
    print("\n========================================")
    print("           STUDIO INVOICE               ")
    print("========================================")
    print(f"Artist: {artist_name.strip()}")
    print("----------------------------------------")
    print(f"Room Rental ({studio_hours:.1f} hrs):     ${room_tot:,.2f}")

    if engineer_req == 'Y':
        print(f"Sound Engineer Fee:     ${eng_tot:,.2f}")

    if mastering_trk > 0:
        print(f"Audio Mastering ({mastering_trk}):      ${master_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL SESSION COST:     ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    record_label()
