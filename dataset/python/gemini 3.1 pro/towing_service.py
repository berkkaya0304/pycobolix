def main():
    print("--- HIGHWAY HERO TOWING ---")
    driver_name = input("Motorist: ")
    veh_type = input("Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): ").strip()
    try:
        tow_miles = float(input("Total Towing Miles: "))
    except ValueError:
        tow_miles = 0.0
    need_wintch = input("Did vehicle require ditch/snow winch-out? (Y/N): ").strip().upper() == 'Y'

    if veh_type == '1':
        hook_fee = 75.00
        mile_rate = 3.50
    elif veh_type == '2':
        hook_fee = 125.00
        mile_rate = 5.00
    elif veh_type == '3':
        hook_fee = 60.00
        mile_rate = 3.00
    else:
        hook_fee = 75.00
        mile_rate = 3.50

    mile_tot = tow_miles * mile_rate
    wintch_fee = 50.00 if need_wintch else 0.0

    grand_tot = hook_fee + mile_tot + wintch_fee

    print("\n========================================")
    print("          TOW SERVICE SUMMARY           ")
    print("========================================")
    print(f"Motorist: {driver_name}")
    print("----------------------------------------")
    print(f"Base Hookup Fee:     ${hook_fee:6.2f}")
    print(f"Mileage ({tow_miles:3.1f}m):     ${mile_tot:6.2f}")
    
    if need_wintch:
        print(f"Winch-Out Surcharge: ${wintch_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TOW BILL:      ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
