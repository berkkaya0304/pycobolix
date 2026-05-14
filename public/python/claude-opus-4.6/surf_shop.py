"""
Big Kahuna Surf Shack - Surf Shop
Converted from COBOL (surf_shop.cbl) to Python
"""


def main():
    board_rt, suit_rt, lesson_fee = 15.00, 10.00, 45.00

    print("--- BIG KAHUNA SURF SHACK ---")
    surfer_name = input("Name: ")
    board_rentals = int(input("Surfboards to Rent ($15/hr): "))
    wetsuits = int(input("Wetsuits to Rent ($10/hr): "))
    hours_rent = int(input("Rental Duration (Hours): "))
    lesson_add = input("Add 1-Hour Beginner Lesson ($45)? (Y/N): ").strip().upper()

    b_tot = (board_rentals * board_rt) * hours_rent
    s_tot = (wetsuits * suit_rt) * hours_rent
    l_tot = lesson_fee if lesson_add == "Y" else 0.0
    grand_tot = b_tot + s_tot + l_tot

    print()
    print("========================================")
    print("             SURF RENTALS               ")
    print("========================================")
    print(f"Cowabunga, {surfer_name}!")
    print(f"Renting for {hours_rent} hours.")
    print("----------------------------------------")
    if board_rentals > 0:
        print(f"Surfboards ({board_rentals}):       ${b_tot:>9,.2f}")
    if wetsuits > 0:
        print(f"Wetsuits ({wetsuits}):         ${s_tot:>9,.2f}")
    if lesson_add == "Y":
        print(f"Beginner Lesson:      ${l_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL WAVES COST:     ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
