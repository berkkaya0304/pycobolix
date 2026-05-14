def main():
    print("--- AERO CAPTURE DRONE RENTALS ---")
    
    cust_name = input("Renter Name: ")
    drone_model = input("Drone (1=Basic $40, 2=Pro 4K $90, 3=Cinema $250): ")
    days_rnt = int(input("Days to Rent: ") or 0)
    extra_batt = int(input("Extra Battery Packs ($10/day ea): ") or 0)
    insure_wvt = input("Add Crash Insurance ($25/day)? (Y/N): ").upper()

    # Determine Daily Rate
    if drone_model == "1":
        daily_rate = 40.00
    elif drone_model == "2":
        daily_rate = 90.00
    elif drone_model == "3":
        daily_rate = 250.00
    else:
        daily_rate = 40.00

    # Calculations
    drone_tot = daily_rate * days_rnt
    batt_tot = (extra_batt * 10.00) * days_rnt
    insure_tot = (25.00 * days_rnt) if insure_wvt == 'Y' else 0.0
    grand_tot = drone_tot + batt_tot + insure_tot

    # Formatting for currency
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("          RENTAL AGREEMENT              ")
    print("========================================")
    print(f"Renter: {cust_name}")
    print(f"Terms:  {days_rnt} Day(s)")
    print("----------------------------------------")
    print(f"Drone Flight Time:  {format_currency(drone_tot)}")
    
    if extra_batt > 0:
        print(f"Extra Power Packs:  {format_currency(batt_tot)}")
    
    if insure_wvt == 'Y':
        print(f"Crash Insurance:    {format_currency(insure_tot)}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    main()
