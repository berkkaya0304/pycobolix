def main():
    print("--- BIG KAHUNA SURF SHACK ---")
    surfer_name = input("Name: ")
    try:
        board_rentals = int(input("Surfboards to Rent ($15/hr): "))
    except ValueError:
        board_rentals = 0
    try:
        wetsuits = int(input("Wetsuits to Rent ($10/hr): "))
    except ValueError:
        wetsuits = 0
    try:
        hours_rent = int(input("Rental Duration (Hours): "))
    except ValueError:
        hours_rent = 1
    wants_lesson = input("Add 1-Hour Beginner Lesson ($45)? (Y/N): ").strip().upper() == 'Y'

    board_rt = 15.00
    suit_rt = 10.00
    lesson_fee = 45.00

    b_tot = (board_rentals * board_rt) * hours_rent
    s_tot = (wetsuits * suit_rt) * hours_rent

    l_tot = lesson_fee if wants_lesson else 0.0

    grand_tot = b_tot + s_tot + l_tot

    print("\n========================================")
    print("             SURF RENTALS               ")
    print("========================================")
    print(f"Cowabunga, {surfer_name}!")
    print(f"Renting for {hours_rent:02d} hours.")
    print("----------------------------------------")
    
    if board_rentals > 0:
        print(f"Surfboards ({board_rentals:02d}):       ${b_tot:6.2f}")
        
    if wetsuits > 0:
        print(f"Wetsuits ({wetsuits:02d}):         ${s_tot:6.2f}")
        
    if wants_lesson:
        print(f"Beginner Lesson:      ${l_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL WAVES COST:     ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
