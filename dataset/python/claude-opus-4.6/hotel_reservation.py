"""
Hotel Booking System - Hotel Reservation
Converted from COBOL (hotel_reservation.cbl) to Python
"""


def main():
    print("--- HOTEL BOOKING SYSTEM ---")
    continue_prog = "Y"

    while continue_prog.upper() == "Y":
        guest_name = input("Enter Guest Name: ")
        room_type = input("Select Room Type (S=Std, D=Deluxe, P=Suite): ").strip().upper()
        nights = int(input("Number of Nights: "))
        breakfast_inc = input("Include Breakfast? ($20/night) (Y/N): ").strip().upper()
        spa_access = input("Include Spa Access? ($50 flat fee) (Y/N): ").strip().upper()

        if room_type == "S":
            cost_per_night = 100.00
        elif room_type == "D":
            cost_per_night = 180.00
        elif room_type == "P":
            cost_per_night = 350.00
        else:
            cost_per_night = 100.00
            print("Invalid room type, defaulted to Standard.")

        room_total = cost_per_night * nights
        addon_total = 0.0

        if breakfast_inc == "Y":
            addon_total += 20.00 * nights
        if spa_access == "Y":
            addon_total += 50.00

        grand_bill = room_total + addon_total

        print()
        print("***********************************")
        print("       GUEST RECEIPT               ")
        print("***********************************")
        print(f"Guest: {guest_name}")
        print(f"Nights: {nights}")
        print(f"Room Charge:    ${room_total:>12,.2f}")
        print(f"Add-Ons Charge: ${addon_total:>12,.2f}")
        print("-----------------------------------")
        print(f"TOTAL BILL:     ${grand_bill:>12,.2f}")
        print("***********************************")
        print()

        continue_prog = input("Process another guest? (Y/N): ").strip().upper()

    print("System Shutdown.")


if __name__ == "__main__":
    main()
