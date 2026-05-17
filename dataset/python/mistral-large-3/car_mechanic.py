def car_mechanic():
    print("--- GREASE MONKEY AUTO SHOP ---")
    customer_name = input("Customer Name: ").strip()
    vehicle_info = input("Vehicle Make/Model: ").strip()

    oil_change = input("Synthetic Oil Change ($65)? (Y/N): ").strip().upper()
    tire_rotation = input("Tire Rotation & Balance ($40)? (Y/N): ").strip().upper()

    print("Brakes (1=Front $150, 2=Rear $150, 3=All $280, 0=None): ")
    brake_pads = input().strip()

    oil_fee = 65.00 if oil_change == 'Y' else 0.00
    tire_fee = 40.00 if tire_rotation == 'Y' else 0.00

    if brake_pads == '1':
        brake_fee = 150.00
    elif brake_pads == '2':
        brake_fee = 150.00
    elif brake_pads == '3':
        brake_fee = 280.00
    else:
        brake_fee = 0.00

    shop_supplies = 15.00
    grand_total = oil_fee + tire_fee + brake_fee + shop_supplies

    print("\n========================================")
    print("            REPAIR INVOICE              ")
    print("========================================")
    print(f"Customer: {customer_name}")
    print(f"Vehicle:  {vehicle_info}")
    print("----------------------------------------")

    if oil_change == 'Y':
        print(f"Lube/Oil Change:    ${oil_fee:.2f}")
    if tire_rotation == 'Y':
        print(f"Tire Rotation:      ${tire_fee:.2f}")
    if brake_fee > 0:
        print(f"Brake Pad Service:  ${brake_fee:.2f}")

    print(f"Shop/Disposal Fee:  ${shop_supplies:.2f}")
    print("----------------------------------------")
    print(f"GRAND TOTAL:        ${grand_total:.2f}")
    print("========================================")

if __name__ == "__main__":
    car_mechanic()
