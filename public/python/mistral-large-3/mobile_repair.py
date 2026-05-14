def mobile_repair():
    print("--- CELL DOCTOR REPAIRS ---")
    customer = input("Customer: ").strip()
    phone_model = input("Phone Model: ").strip()

    screen_fix = input("OLED Screen Replacement ($180)? (Y/N): ").strip().upper() == 'Y'
    battery_fix = input("Battery Replacement ($65)? (Y/N): ").strip().upper() == 'Y'
    water_damage = input("Water Damage Diagnostics ($40)? (Y/N): ").strip().upper() == 'Y'

    screen_fee = 180.00 if screen_fix else 0.00
    batt_fee = 65.00 if battery_fix else 0.00
    diag_fee = 40.00 if water_damage else 0.00
    total_cost = screen_fee + batt_fee + diag_fee

    print("\n========================================")
    print("            REPAIR TICKET               ")
    print("========================================")
    print(f"Customer: {customer}")
    print(f"Device:   {phone_model}")
    print("----------------------------------------")

    if screen_fix:
        print(f"Screen Replacement: ${screen_fee:,.2f}")
    if battery_fix:
        print(f"Battery Install:    ${batt_fee:,.2f}")
    if water_damage:
        print(f"Water Diagnostic:   ${diag_fee:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_cost:,.2f}")
    print("========================================")

if __name__ == "__main__":
    mobile_repair()
