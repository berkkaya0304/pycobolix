def main():
    print("--- CRYSTAL CLEAR POOL SERVICE ---")
    
    homeowner = input("Client: ")
    pool_type_input = input("Pool (1=Above Ground $50, 2=In Ground $80): ")
    salt_water_input = input("Is it a Salt Water Pool (lower chem fee)? (Y/N): ").upper()
    filter_clean_input = input("Add Filter Dismantle & Scrub ($45)? (Y/N): ").upper()

    # Determine Base Cleaning Fee
    if pool_type_input == '1':
        base_clean = 50.00
    elif pool_type_input == '2':
        base_clean = 80.00
    else:
        base_clean = 50.00

    # Determine Chemical Charge
    chem_charge = 10.00 if salt_water_input == 'Y' else 20.00

    # Determine Filter Charge
    filter_chg = 45.00 if filter_clean_input == 'Y' else 0.00

    total_bill = base_clean + chem_charge + filter_chg

    print("\n========================================")
    print("          POOL SERVICE RECIEPT          ")
    print("========================================")
    print(f"Home: {homeowner}")
    print("----------------------------------------")
    print(f"Base Cleaning:       ${base_clean:>.2f}")
    print(f"Chemicals Balancing: ${chem_charge:>.2f}")
    
    if filter_clean_input == 'Y':
        print(f"Filter Deep Clean:   ${filter_chg:>.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_bill:>.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
