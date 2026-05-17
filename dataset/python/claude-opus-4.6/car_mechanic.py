"""
Grease Monkey Auto Shop - Car Mechanic
Converted from COBOL (car_mechanic.cbl) to Python
"""


def main():
    print("--- GREASE MONKEY AUTO SHOP ---")
    customer_name = input("Customer Name: ")
    vehicle_info = input("Vehicle Make/Model: ")
    oil_change = input("Synthetic Oil Change ($65)? (Y/N): ").strip().upper()
    tire_rotation = input("Tire Rotation & Balance ($40)? (Y/N): ").strip().upper()
    print("Brakes (1=Front $150, 2=Rear $150, 3=All $280,")
    brake_pads = int(input(" 0=None): "))

    oil_fee = 65.00 if oil_change == "Y" else 0.0
    tire_fee = 40.00 if tire_rotation == "Y" else 0.0

    if brake_pads == 1:
        brake_fee = 150.00
    elif brake_pads == 2:
        brake_fee = 150.00
    elif brake_pads == 3:
        brake_fee = 280.00
    else:
        brake_fee = 0.0

    shop_supplies = 15.00
    grand_tot = oil_fee + tire_fee + brake_fee + shop_supplies

    print()
    print("========================================")
    print("            REPAIR INVOICE              ")
    print("========================================")
    print(f"Customer: {customer_name}")
    print(f"Vehicle:  {vehicle_info}")
    print("----------------------------------------")
    if oil_change == "Y":
        print(f"Lube/Oil Change:    ${oil_fee:>9,.2f}")
    if tire_rotation == "Y":
        print(f"Tire Rotation:      ${tire_fee:>9,.2f}")
    if brake_fee > 0:
        print(f"Brake Pad Service:  ${brake_fee:>9,.2f}")
    print(f"Shop/Disposal Fee:  ${shop_supplies:>9,.2f}")
    print("----------------------------------------")
    print(f"GRAND TOTAL:        ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
