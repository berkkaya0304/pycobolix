def main():
    print("--- TIC-TOCK WATCH REPAIR ---")
    
    client_name = input("Client: ")
    watch_brand = input("Watch Brand: ")
    is_luxury = input("Is this a luxury timepiece (+25%)? (Y/N): ").upper() == 'Y'
    fix_batt = input("Replace Battery ($20)? (Y/N): ").upper() == 'Y'
    fix_strap = input("Replace/Fix Strap ($35)? (Y/N): ").upper() == 'Y'
    fix_polish = input("Surface Polish ($45)? (Y/N): ").upper() == 'Y'

    batt_fee = 20.00 if fix_batt else 0.00
    strap_fee = 35.00 if fix_strap else 0.00
    polish_fee = 45.00 if fix_polish else 0.00

    sub_tot = batt_fee + strap_fee + polish_fee
    luxury_surchg = sub_tot * 0.25 if is_luxury else 0.00
    grand_tot = sub_tot + luxury_surchg

    print("\n========================================")
    print("            SERVICE TICKET              ")
    print("========================================")
    print(f"Client: {client_name}")
    print(f"Brand:  {watch_brand}")
    print("----------------------------------------")
    
    if fix_batt:
        print(f"Battery Service:    ${batt_fee:,.2f}")
    if fix_strap:
        print(f"Strap Replacement:  ${strap_fee:,.2f}")
    if fix_polish:
        print(f"Polishing Service:  ${polish_fee:,.2f}")
        
    print("----------------------------------------")
    if is_luxury:
        print(f"Luxury Brand Fee:   ${luxury_surchg:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL SERVICE COST: ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
