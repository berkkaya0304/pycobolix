def main():
    print("--- NEON NIGHTS KARAOKE ---")
    guest_name = input("Host Name: ").strip()
    
    print("Room (1=Small $30/hr, 2=Large $60/h, 3=Suite $100): ", end="")
    room_size = int(input())
    
    print("Time Reserved (Hours): ", end="")
    rent_hours = int(input())
    
    print("Food & Drink Tab Total ($): ", end="")
    food_drink_tab = float(input())
    
    if room_size == 1:
        hourly_rate = 30.00
    elif room_size == 2:
        hourly_rate = 60.00
    elif room_size == 3:
        hourly_rate = 100.00
    else:
        hourly_rate = 30.00
    
    room_total = hourly_rate * rent_hours
    service_charge = food_drink_tab * 0.18
    grand_total = room_total + food_drink_tab + service_charge
    
    print("\n" + "=" * 40)
    print("          KARAOKE ROOM INVOICE          ")
    print("=" * 40)
    print(f"Host: {guest_name}")
    print("-" * 40)
    print(f"Room Rental ({rent_hours}h):      ${room_total:,.2f}")
    
    if food_drink_tab > 0:
        print(f"Food & Drink Tab:      ${food_drink_tab:,.2f}")
        print(f"Auto Gratuity (18%):   ${service_charge:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:      ${grand_total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
