def surf_shop():
    print("--- BIG KAHUNA SURF SHACK ---")
    surfer_name = input("Name: ")
    board_rentals = int(input("Surfboards to Rent ($15/hr): "))
    wetsuits = int(input("Wetsuits to Rent ($10/hr): "))
    hours_rent = int(input("Rental Duration (Hours): "))
    lesson_add = input("Add 1-Hour Beginner Lesson ($45)? (Y/N): ").upper()
    
    wants_lesson = lesson_add == 'Y'
    
    board_rate = 15.00
    suit_rate = 10.00
    lesson_fee = 45.00
    
    b_tot = (board_rentals * board_rate) * hours_rent
    s_tot = (wetsuits * suit_rate) * hours_rent
    l_tot = lesson_fee if wants_lesson else 0
    
    grand_total = b_tot + s_tot + l_tot
    
    print("\n" + "=" * 40)
    print("             SURF RENTALS               ")
    print("=" * 40)
    print(f"Cowabunga, {surfer_name}!")
    print(f"Renting for {hours_rent} hours.")
    print("-" * 40)
    
    if board_rentals > 0:
        print(f"Surfboards ({board_rentals}):       ${b_tot:7.2f}")
    if wetsuits > 0:
        print(f"Wetsuits ({wetsuits}):         ${s_tot:7.2f}")
    if wants_lesson:
        print(f"Beginner Lesson:      ${l_tot:7.2f}")
    
    print("-" * 40)
    print(f"TOTAL WAVES COST:     ${grand_total:7.2f}")
    print("=" * 40)

if __name__ == "__main__":
    surf_shop()
