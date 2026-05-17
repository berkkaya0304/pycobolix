def drone_rental():
    print("--- AERO CAPTURE DRONE RENTALS ---")

    cust_name = input("Renter Name: ").strip()
    drone_model = int(input("Drone (1=Basic $40, 2=Pro 4K $90, 3=Cinema $250): "))
    days_rnt = int(input("Days to Rent: "))
    extra_batt = int(input("Extra Battery Packs ($10/day ea): "))
    insure_wvt = input("Add Crash Insurance ($25/day)? (Y/N): ").strip().upper() == 'Y'

    daily_rate = 0.0
    if drone_model == 1:
        daily_rate = 40.00
    elif drone_model == 2:
        daily_rate = 90.00
    elif drone_model == 3:
        daily_rate = 250.00
    else:
        daily_rate = 40.00

    drone_tot = daily_rate * days_rnt
    batt_tot = (extra_batt * 10.00) * days_rnt
    insure_tot = 25.00 * days_rnt if insure_wvt else 0.0
    grand_tot = drone_tot + batt_tot + insure_tot

    print("")
    print("========================================")
    print("          RENTAL AGREEMENT              ")
    print("========================================")
    print(f"Renter: {cust_name}")
    print(f"Terms:  {days_rnt} Day(s)")
    print("----------------------------------------")
    print(f"Drone Flight Time:  ${drone_tot:,.2f}")

    if extra_batt > 0:
        print(f"Extra Power Packs:  ${batt_tot:,.2f}")

    if insure_wvt:
        print(f"Crash Insurance:    ${insure_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    drone_rental()
