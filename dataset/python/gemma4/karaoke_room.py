def main():
    print("--- NEON NIGHTS KARAOKE ---")
    
    guest_name = input("Host Name: ")
    room_size = input("Room (1=Small $30/hr, 2=Large $60/h, 3=Suite $100): ")
    rent_hours = float(input("Time Reserved (Hours): ") or 0)
    food_drink_tab = float(input("Food & Drink Tab Total ($): ") or 0)

    # Determine hourly rate based on room size
    rates = {
        "1": 30.00,
        "2": 60.00,
        "3": 100.00
    }
    hourly_rate = rates.get(room_size, 30.00)

    # Calculations
    room_tot = hourly_rate * rent_hours
    serv_chg = food_drink_tab * 0.18
    grand_tot = room_tot + food_drink_tab + serv_chg

    # Invoice Output
    print("\n========================================")
    print("          KARAOKE ROOM INVOICE          ")
    print("========================================")
    print(f"Host: {guest_name}")
    print("----------------------------------------")
    print(f"Room Rental ({int(rent_hours)}h):      ${room_tot:,.2f}")
    
    if food_drink_tab > 0:
        print(f"Food & Drink Tab:      ${food_drink_tab:,.2f}")
        print(f"Auto Gratuity (18%):   ${serv_chg:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:      ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
