def pool_cleaning():
    print("--- CRYSTAL CLEAR POOL SERVICE ---")
    homeowner = input("Client: ")
    
    while True:
        pool_type = input("Pool (1=Above Ground $50, 2=In Ground $80): ")
        if pool_type in ['1', '2']:
            break
        print("Please enter 1 or 2")
    
    salt_water = input("Is it a Salt Water Pool (lower chem fee)? (Y/N): ").upper()
    filter_clean = input("Add Filter Dismantle & Scrub ($45)? (Y/N): ").upper()
    
    if pool_type == '1':
        base_clean = 50.00
    else:
        base_clean = 80.00
    
    chem_charge = 10.00 if salt_water == 'Y' else 20.00
    filter_chg = 45.00 if filter_clean == 'Y' else 0.00
    total_bill = base_clean + chem_charge + filter_chg
    
    print("\n" + "="*40)
    print("          POOL SERVICE RECEIPT          ")
    print("="*40)
    print(f"Home: {homeowner}")
    print("-"*40)
    print(f"Base Cleaning:       ${base_clean:5.2f}")
    print(f"Chemicals Balancing: ${chem_charge:5.2f}")
    if filter_clean == 'Y':
        print(f"Filter Deep Clean:   ${filter_chg:5.2f}")
    print("-"*40)
    print(f"TOTAL AMOUNT DUE:    ${total_bill:6.2f}")
    print("="*40)

if __name__ == "__main__":
    pool_cleaning()
