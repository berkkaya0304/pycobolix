def main():
    print("--- PLATINUM TRACKS STUDIO ---")
    artist_name = input("Artist / Band Name: ")
    try:
        studio_hours = float(input("Studio Rental Duration (Hours): "))
    except ValueError:
        studio_hours = 0.0
    engineer_req = input("Require Sound Engineer ($40/hr)? (Y/N): ").strip().upper() == 'Y'
    try:
        mastering_trk = int(input("Number of Tracks to Master ($150 ea): "))
    except ValueError:
        mastering_trk = 0

    room_rate = 50.00
    eng_rate = 40.00
    master_rate = 150.00

    room_tot = studio_hours * room_rate

    eng_tot = 0.0
    if engineer_req:
        eng_tot = studio_hours * eng_rate

    master_tot = mastering_trk * master_rate
    grand_tot = room_tot + eng_tot + master_tot

    print("\n========================================")
    print("           STUDIO INVOICE               ")
    print("========================================")
    print(f"Artist: {artist_name}")
    print("----------------------------------------")
    print(f"Room Rental ({studio_hours:.1f} hrs): ${room_tot:6.2f}")
    
    if engineer_req:
        print(f"Sound Engineer Fee:     ${eng_tot:6.2f}")
        
    if mastering_trk > 0:
        print(f"Audio Mastering ({mastering_trk:02d}):  ${master_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL SESSION COST:     ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
