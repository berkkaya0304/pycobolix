"""
Turnpike Toll Authority - Toll Booth
Converted from COBOL (toll_booth.cbl) to Python
"""


def main():
    base_toll = 2.50

    print("--- TURNPIKE TOLL AUTHORITY ---")
    license_plate = input("License Plate: ")
    axles = int(input("Number of Axles (e.g. 2 for car, 4+ for truck): "))
    has_ezpass = input("EZ-Pass Transponder Detected? (Y/N): ").strip().upper()

    axle_charge = (axles - 2) * 2.00 if axles > 2 else 0.0
    gross_toll = base_toll + axle_charge
    discount = gross_toll * 0.20 if has_ezpass == "Y" else 0.0
    net_toll = gross_toll - discount

    print()
    print("========================================")
    print("           TOLL RECEIPT                 ")
    print("========================================")
    print(f"Plate: {license_plate}   Axles: {axles}")
    print("----------------------------------------")
    print(f"Base Vehicle Toll:  ${base_toll:>9,.2f}")
    if axle_charge > 0:
        print(f"Extra Axle Charge:  ${axle_charge:>9,.2f}")
    if has_ezpass == "Y":
        print(f"EZ-Pass Discount:  -${discount:>8,.2f}")
    print("----------------------------------------")
    print(f"TOTAL TOLL FARE:    ${net_toll:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
