def main():
    print("--- HOTEL BOOKING SYSTEM ---")
    
    while True:
        guest_info = get_booking()
        room_total, addon_total, grand_total = calculate_bill(guest_info)
        show_receipt(guest_info, room_total, addon_total, grand_total)
        
        if input("Process another guest? (Y/N): ").upper() != 'Y':
            break
    
    print("System Shutdown.")

def get_booking():
    guest_info = {
        'name': input("Enter Guest Name: "),
        'room_type': input("Select Room Type (S=Std, D=Deluxe, P=Suite): ").upper(),
        'nights': int(input("Number of Nights: ")),
        'breakfast': input("Include Breakfast? ($20/night) (Y/N): ").upper() == 'Y',
        'spa': input("Include Spa Access? ($50 flat fee) (Y/N): ").upper() == 'Y'
    }
    return guest_info

def calculate_bill(guest):
    room_rates = {
        'S': 100.00,
        'D': 180.00,
        'P': 350.00
    }
    
    cost_per_night = room_rates.get(guest['room_type'], 100.00)
    if guest['room_type'] not in room_rates:
        print("Invalid room type, defaulted to Standard.")
    
    room_total = cost_per_night * guest['nights']
    addon_total = 0.0
    
    if guest['breakfast']:
        addon_total += 20.00 * guest['nights']
    
    if guest['spa']:
        addon_total += 50.00
    
    grand_total = room_total + addon_total
    return room_total, addon_total, grand_total

def show_receipt(guest, room_total, addon_total, grand_total):
    print("\n" + "*" * 35)
    print("       GUEST RECEIPT               ")
    print("*" * 35)
    print(f"Guest: {guest['name']}")
    print(f"Nights: {guest['nights']}")
    print(f"Room Charge:    ${room_total:,.2f}")
    print(f"Add-Ons Charge: ${addon_total:,.2f}")
    print("-" * 35)
    print(f"TOTAL BILL:     ${grand_total:,.2f}")
    print("*" * 35 + "\n")

if __name__ == "__main__":
    main()
