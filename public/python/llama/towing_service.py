# TOWING-SERVICE - Highway Hero Towing
# Converted from COBOL to Python

def main():
    print("--- HIGHWAY HERO TOWING ---")
    driver_name = input("Motorist: ")
    veh_type = int(input("Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): "))
    tow_miles = float(input("Total Towing Miles: "))
    wintch_out = input("Did vehicle require ditch/snow winch-out? (Y/N): ").strip().upper()

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
    wintch_fee = 50.00 if wintch_out == 'Y' else 0.0
    grand_tot = hook_fee + mile_tot + wintch_fee

    print("")
    print("========================================")
    print("          TOW SERVICE SUMMARY           ")
    print("========================================")
    print(f"Motorist: {driver_name}")
    print("----------------------------------------")
    print(f"Base Hookup Fee:     ${hook_fee:,.2f}")
    print(f"Mileage ({tow_miles}m):     ${mile_tot:,.2f}")
    if wintch_out == 'Y':
        print(f"Winch-Out Surcharge: ${wintch_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL TOW BILL:      ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
