def calculate_toll():
    print("--- TURNPIKE TOLL AUTHORITY ---")
    
    license_plate = input("License Plate: ")
    try:
        axles = int(input("Number of Axles (e.g. 2 for car, 4+ for truck): "))
    except ValueError:
        axles = 2
        
    has_ezpass = input("EZ-Pass Transponder Detected? (Y/N): ").strip().upper()

    base_toll = 2.50
    axle_charge = 0.0
    discount = 0.0

    if axles > 2:
        axle_charge = (axles - 2) * 2.00

    gross_toll = base_toll + axle_charge

    if has_ezpass == 'Y':
        discount = gross_toll * 0.20

    net_toll = gross_toll - discount

    print("\n========================================")
    print("           TOLL RECEIPT                 ")
    print("========================================")
    print(f"Plate: {license_plate:<10}   Axles: {axles}")
    print("----------------------------------------")
    print(f"Base Vehicle Toll:  ${base_toll:,.2f}")
    
    if axle_charge > 0:
        print(f"Extra Axle Charge:  ${axle_charge:,.2f}")
    
    if has_ezpass == 'Y':
        print(f"EZ-Pass Discount:  -${discount:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TOLL FARE:    ${net_toll:,.2f}")
    print("========================================")

if __name__ == "__main__":
    calculate_toll()
