def main():
    print("--- SEASIDE RESORT BOOKING ---")
    guest = input("Guest Name: ")
    season = input("Season (P=Peak, O=Off-Peak): ").strip().upper()
    view_type = input("Room View (1=Std, 2=Ocean, 3=Suite): ").strip()
    try:
        nights = int(input("Number of Nights: "))
    except ValueError:
        nights = 0

    if view_type == '1':
        base_rate = 150.00
    elif view_type == '2':
        base_rate = 250.00
    elif view_type == '3':
        base_rate = 500.00
    else:
        base_rate = 150.00

    season_mult = 1.50 if season == 'P' else 1.00

    nightly_rate = base_rate * season_mult
    subtotal = nightly_rate * nights
    taxes = subtotal * 0.125
    grand_total = subtotal + taxes

    print("\n====================================")
    print("       BOOKING CONFIRMATION         ")
    print("====================================")
    print(f"Guest:  {guest}")
    print(f"Nights: {nights}")
    print("------------------------------------")
    print(f"Est. Nightly Rate: ${nightly_rate:8.2f}")
    print(f"Room Subtotal:     ${subtotal:8.2f}")
    print(f"Taxes (12.5%):     ${taxes:8.2f}")
    print("------------------------------------")
    print(f"TOTAL STAY COST:   ${grand_total:8.2f}")
    print("====================================")

if __name__ == "__main__":
    main()
