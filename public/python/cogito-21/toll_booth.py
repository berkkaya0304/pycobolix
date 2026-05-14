def main():
    print("--- TURNPIKE TOLL AUTHORITY ---")
    license_plate = input("License Plate: ")
    
    while True:
        try:
            axles = int(input("Number of Axles (e.g. 2 for car, 4+ for truck): "))
            if axles >= 2:
                break
            print("Please enter a valid number of axles (minimum 2).")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        has_ezpass = input("EZ-Pass Transponder Detected? (Y/N): ").upper()
        if has_ezpass in ('Y', 'N'):
            break
        print("Please enter 'Y' or 'N'.")

    base_toll = 2.50
    axle_charge = 0.0
    discount = 0.0

    if axles > 2:
        axle_charge = (axles - 2) * 2.00

    gross_toll = base_toll + axle_charge

    if has_ezpass == 'Y':
        discount = gross_toll * 0.20

    net_toll = gross_toll - discount

    print("\n" + "=" * 40)
    print("           TOLL RECEIPT                 ")
    print("=" * 40)
    print(f"Plate: {license_plate:<10}   Axles: {axles}")
    print("-" * 40)
    print(f"Base Vehicle Toll:  ${base_toll:>6.2f}")
    
    if axle_charge > 0:
        print(f"Extra Axle Charge:  ${axle_charge:>6.2f}")
    
    if has_ezpass == 'Y':
        print(f"EZ-Pass Discount:  -${discount:>6.2f}")
    
    print("-" * 40)
    print(f"TOTAL TOLL FARE:    ${net_toll:>6.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
