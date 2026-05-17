"""
Crystal Clear Pool Service
Converted from COBOL (pool_cleaning.cbl) to Python
"""


def main():
    print("--- CRYSTAL CLEAR POOL SERVICE ---")
    homeowner = input("Client: ")
    pool_type = int(input("Pool (1=Above Ground $50, 2=In Ground $80): "))
    salt_water = input("Is it a Salt Water Pool? (Y/N): ").strip().upper()
    filter_clean = input("Add Filter Dismantle & Scrub ($45)? (Y/N): ").strip().upper()

    base_clean = 50.00 if pool_type == 1 else 80.00
    chem_charge = 10.00 if salt_water == "Y" else 20.00
    filter_chg = 45.00 if filter_clean == "Y" else 0.0
    total_bill = base_clean + chem_charge + filter_chg

    print()
    print("========================================")
    print("          POOL SERVICE RECIEPT          ")
    print("========================================")
    print(f"Home: {homeowner}")
    print("----------------------------------------")
    print(f"Base Cleaning:       ${base_clean:>9,.2f}")
    print(f"Chemicals Balancing: ${chem_charge:>9,.2f}")
    if filter_clean == "Y":
        print(f"Filter Deep Clean:   ${filter_chg:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_bill:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
