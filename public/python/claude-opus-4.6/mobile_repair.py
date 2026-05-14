"""
Cell Doctor Repairs - Mobile Repair
Converted from COBOL (mobile_repair.cbl) to Python
"""


def main():
    print("--- CELL DOCTOR REPAIRS ---")
    customer = input("Customer: ")
    phone_model = input("Phone Model: ")
    screen_fix = input("OLED Screen Replacement ($180)? (Y/N): ").strip().upper()
    battery_fix = input("Battery Replacement ($65)? (Y/N): ").strip().upper()
    water_damage = input("Water Damage Diagnostics ($40)? (Y/N): ").strip().upper()

    screen_fee = 180.00 if screen_fix == "Y" else 0.0
    batt_fee = 65.00 if battery_fix == "Y" else 0.0
    diag_fee = 40.00 if water_damage == "Y" else 0.0
    total_cost = screen_fee + batt_fee + diag_fee

    print()
    print("========================================")
    print("            REPAIR TICKET               ")
    print("========================================")
    print(f"Customer: {customer}")
    print(f"Device:   {phone_model}")
    print("----------------------------------------")
    if screen_fix == "Y":
        print(f"Screen Replacement: ${screen_fee:>9,.2f}")
    if battery_fix == "Y":
        print(f"Battery Install:    ${batt_fee:>9,.2f}")
    if water_damage == "Y":
        print(f"Water Diagnostic:   ${diag_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_cost:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
