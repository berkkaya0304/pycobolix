def main():
    print("--- CELL DOCTOR REPAIRS ---")
    customer = input("Customer: ").strip()
    phone_model = input("Phone Model: ").strip()
    
    screen_fix = input("OLED Screen Replacement ($180)? (Y/N): ").strip().upper()
    battery_fix = input("Battery Replacement ($65)? (Y/N): ").strip().upper()
    water_damage = input("Water Damage Diagnostics ($40)? (Y/N): ").strip().upper()
    
    screen_fee = 180.00 if screen_fix == 'Y' else 0.00
    batt_fee = 65.00 if battery_fix == 'Y' else 0.00
    diag_fee = 40.00 if water_damage == 'Y' else 0.00
    
    total_cost = screen_fee + batt_fee + diag_fee
    
    print("\n" + "=" * 40)
    print("            REPAIR TICKET               ")
    print("=" * 40)
    print(f"Customer: {customer}")
    print(f"Device:   {phone_model}")
    print("-" * 40)
    
    if screen_fix == 'Y':
        print(f"Screen Replacement: ${screen_fee:>6.2f}")
    if battery_fix == 'Y':
        print(f"Battery Install:    ${batt_fee:>6.2f}")
    if water_damage == 'Y':
        print(f"Water Diagnostic:   ${diag_fee:>6.2f}")
    
    print("-" * 40)
    print(f"TOTAL BALANCE:      ${total_cost:>6.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
