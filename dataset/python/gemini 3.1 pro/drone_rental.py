def main():
    print("--- AERO CAPTURE DRONE RENTALS ---")
    cust_name = input("Renter Name: ")
    drone_model = input("Drone (1=Basic $40, 2=Pro 4K $90, 3=Cinema $250): ").strip()
    try:
        days_rnt = int(input("Days to Rent: "))
    except ValueError:
        days_rnt = 0
    try:
        extra_batt = int(input("Extra Battery Packs ($10/day ea): "))
    except ValueError:
        extra_batt = 0
    wants_ins = input("Add Crash Insurance ($25/day)? (Y/N): ").strip().upper() == 'Y'

    if drone_model == '1':
        daily_rate = 40.00
    elif drone_model == '2':
        daily_rate = 90.00
    elif drone_model == '3':
        daily_rate = 250.00
    else:
        daily_rate = 40.00

    drone_tot = daily_rate * days_rnt
    batt_tot = (extra_batt * 10.00) * days_rnt

    insure_tot = 25.00 * days_rnt if wants_ins else 0.0

    grand_tot = drone_tot + batt_tot + insure_tot

    print("\n========================================")
    print("          RENTAL AGREEMENT              ")
    print("========================================")
    print(f"Renter: {cust_name}")
    print(f"Terms:  {days_rnt} Day(s)")
    print("----------------------------------------")
    print(f"Drone Flight Time:  ${drone_tot:6.2f}")
    
    if extra_batt > 0:
        print(f"Extra Power Packs:  ${batt_tot:6.2f}")
        
    if wants_ins:
        print(f"Crash Insurance:    ${insure_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
