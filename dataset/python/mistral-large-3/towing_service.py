def towing_service():
    print("--- HIGHWAY HERO TOWING ---")
    driver_name = input("Motorist: ").strip()
    print("Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): ", end="")
    veh_type = int(input().strip())
    tow_miles = float(input("Total Towing Miles: ").strip())
    winch_out = input("Did vehicle require ditch/snow winch-out? (Y/N): ").strip().upper() == 'Y'

    hook_fee = 0.0
    mile_rate = 0.0

    if veh_type == 1:
        hook_fee = 75.00
        mile_rate = 3.50
    elif veh_type == 2:
        hook_fee = 125.00
        mile_rate = 5.00
    elif veh_type == 3:
        hook_fee = 60.00
        mile_rate = 3.00
    else:
        hook_fee = 75.00
        mile_rate = 3.50

    mile_tot = tow_miles * mile_rate
    winch_fee = 50.00 if winch_out else 0.0
    grand_tot = hook_fee + mile_tot + winch_fee

    print("")
    print("=" * 40)
    print("          TOW SERVICE SUMMARY           ")
    print("=" * 40)
    print(f"Motorist: {driver_name}")
    print("-" * 40)
    print(f"Base Hookup Fee:     ${hook_fee:,.2f}")
    print(f"Mileage ({tow_miles}m):     ${mile_tot:,.2f}")

    if winch_out:
        print(f"Winch-Out Surcharge: ${winch_fee:,.2f}")

    print("-" * 40)
    print(f"TOTAL TOW BILL:      ${grand_tot:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    towing_service()
