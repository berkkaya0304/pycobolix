import sys

def get_booking():
    guest_name = input("Enter Guest Name: ")
    room_type = input("Select Room Type (S=Std, D=Deluxe, P=Suite): ").upper()
    try:
        nights = int(input("Number of Nights: "))
    except ValueError:
        nights = 0
    breakfast_inc = input("Include Breakfast? ($20/night) (Y/N): ").upper()
    spa_access = input("Include Spa Access? ($50 flat fee) (Y/N): ").upper()
    
    return {
        "name": guest_name,
        "room_type": room_type,
        "nights": nights,
        "breakfast": breakfast_inc == 'Y',
        "spa": spa_access == 'Y'
    }

def calc_bill(booking):
    rates = {
        'S': 100.00,
        'D': 180.00,
        'P': 350.00
    }
    
    cost_per_night = rates.get(booking['room_type'])
    if cost_per_night is None:
        cost_per_night = 100.00
        print("Invalid room type, defaulted to Standard.")
    
    room_total = cost_per_night * booking['nights']
    
    addon_total = 0.0
    if booking['breakfast']:
        addon_total += 20.00 * booking['nights']
    if booking['spa']:
        addon_total += 50.00
        
    grand_bill = room_total + addon_total
    
    return room_total, addon_total, grand_bill

def show_receipt(booking, room_total, addon_total, grand_bill):
    print("\n***********************************")
    print("       GUEST RECEIPT               ")
    print("***********************************")
    print(f"Guest: {booking['name']}")
    print(f"Nights: {booking['nights']}")
    print(f"Room Charge:    ${room_total:,.2f}")
    print(f"Add-Ons Charge: ${addon_total:,.2f}")
    print("-----------------------------------")
    print(f"TOTAL BILL:     ${grand_bill:,.2f}")
    print("***********************************\n")

def main():
    print("--- HOTEL BOOKING SYSTEM ---")
    continue_prog = 'Y'
    
    while continue_prog.upper() == 'Y':
        booking = get_booking()
        room_total, addon_total, grand_bill = calc_bill(booking)
        show_receipt(booking, room_total, addon_total, grand_bill)
        
        continue_prog = input("Process another guest? (Y/N): ")
        
    print("System Shutdown.")

if __name__ == "__main__":
    main()
