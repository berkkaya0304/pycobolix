def main():
    print("--- HIGHWAY HERO TOWING ---")
    
    driver_name = input("Motorist: ")
    
    try:
        veh_type = int(input("Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): "))
    except ValueError:
        veh_type = 1

    try:
        tow_miles = float(input("Total Towing Miles: "))
    except ValueError:
        tow_miles = 0.0

    winch_out = input("Did vehicle require ditch/snow winch-out? (Y/N): ").upper()

    # Determine rates based on vehicle type
    if veh_type == 2:  # HEAVY-TRUCK
        hook_fee = 125.00
        mile_rate = 5.00
    elif veh_type == 3:  # MOTORCYCLE
        hook_fee = 60.00
        mile_rate = 3.00
    else:  # STD-CAR or OTHER
        hook_fee = 75.00
        mile_rate = 3.50

    mile_tot = tow_miles * mile_rate
    winch_fee = 50.00 if winch_out == 'Y' else 0.0
    grand_tot = hook_fee + mile_tot + winch_fee

    print("\n========================================")
    print("          TOW SERVICE SUMMARY           ")
    print("========================================")
    print(f"Motorist: {driver_name}")
    print("----------------------------------------")
    print(f"Base Hookup Fee:     ${hook_fee:,.2f}")
    print(f"Mileage ({tow_miles}m):     ${mile_tot:,.2f}")
    
    if winch_out == 'Y':
        print(f"Winch-Out Surcharge: ${winch_fee:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TOW BILL:      ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
