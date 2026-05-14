def main():
    print("--- CELL DOCTOR REPAIRS ---")
    
    customer = input("Customer: ")
    phone_model = input("Phone Model: ")
    
    screen_fix_input = input("OLED Screen Replacement ($180)? (Y/N): ").strip().upper()
    battery_fix_input = input("Battery Replacement ($65)? (Y/N): ").strip().upper()
    water_damage_input = input("Water Damage Diagnostics ($40)? (Y/N): ").strip().upper()

    screen_fee = 180.00 if screen_fix_input == 'Y' else 0.00
    batt_fee = 65.00 if battery_fix_input == 'Y' else 0.00
    diag_fee = 40.00 if water_damage_input == 'Y' else 0.00

    total_cost = screen_fee + batt_fee + diag_fee

    print("\n========================================")
    print("            REPAIR TICKET               ")
    print("========================================")
    print(f"Customer: {customer}")
    print(f"Device:   {phone_model}")
    print("----------------------------------------")
    
    if screen_fee > 0:
        print(f"Screen Replacement: ${screen_fee:,.2f}")
    if batt_fee > 0:
        print(f"Battery Install:    ${batt_fee:,.2f}")
    if diag_fee > 0:
        print(f"Water Diagnostic:   ${diag_fee:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_cost:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
