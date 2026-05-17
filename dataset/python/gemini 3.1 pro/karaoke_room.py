def main():
    print("--- NEON NIGHTS KARAOKE ---")
    guest_name = input("Host Name: ")
    room_size = input("Room (1=Small $30/hr, 2=Large $60/h, 3=Suite $100): ").strip()
    try:
        rent_hours = int(input("Time Reserved (Hours): "))
    except ValueError:
        rent_hours = 0
    try:
        food_drink_tab = float(input("Food & Drink Tab Total ($): "))
    except ValueError:
        food_drink_tab = 0.0

    if room_size == '1':
        hourly_rate = 30.00
    elif room_size == '2':
        hourly_rate = 60.00
    elif room_size == '3':
        hourly_rate = 100.00
    else:
        hourly_rate = 30.00

    room_tot = hourly_rate * rent_hours
    serv_chg = food_drink_tab * 0.18

    grand_tot = room_tot + food_drink_tab + serv_chg

    print("\n========================================")
    print("          KARAOKE ROOM INVOICE          ")
    print("========================================")
    print(f"Host: {guest_name}")
    print("----------------------------------------")
    print(f"Room Rental ({rent_hours}h):      ${room_tot:6.2f}")
    
    if food_drink_tab > 0:
        print(f"Food & Drink Tab:      ${food_drink_tab:6.2f}")
        print(f"Auto Gratuity (18%):   ${serv_chg:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:      ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
