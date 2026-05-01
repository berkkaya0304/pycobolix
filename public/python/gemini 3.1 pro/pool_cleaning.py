def main():
    print("--- CRYSTAL CLEAR POOL SERVICE ---")
    homeowner = input("Client: ")
    pool_type = input("Pool (1=Above Ground $50, 2=In Ground $80): ").strip()
    salt_water = input("Is it a Salt Water Pool (lower chem fee)? (Y/N): ").strip().upper() == 'Y'
    filter_clean = input("Add Filter Dismantle & Scrub ($45)? (Y/N): ").strip().upper() == 'Y'

    if pool_type == '1':
        base_clean = 50.00
    elif pool_type == '2':
        base_clean = 80.00
    else:
        base_clean = 50.00

    chem_charge = 10.00 if salt_water else 20.00
    filter_chg = 45.00 if filter_clean else 0.0

    total_bill = base_clean + chem_charge + filter_chg

    print("\n========================================")
    print("          POOL SERVICE RECIEPT          ")
    print("========================================")
    print(f"Home: {homeowner}")
    print("----------------------------------------")
    print(f"Base Cleaning:       ${base_clean:5.2f}")
    print(f"Chemicals Balancing: ${chem_charge:5.2f}")
    
    if filter_clean:
        print(f"Filter Deep Clean:   ${filter_chg:5.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_bill:5.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
