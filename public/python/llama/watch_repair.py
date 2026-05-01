# WATCH-REPAIR - Tic-Tock Watch Repair
# Converted from COBOL to Python

def main():
    print("--- TIC-TOCK WATCH REPAIR ---")
    client_name = input("Client: ")
    watch_brand = input("Watch Brand: ")
    luxury_tier = input("Is this a luxury timepiece (+25%)? (Y/N): ").strip().upper()
    sv_battery = input("Replace Battery ($20)? (Y/N): ").strip().upper()
    sv_strap = input("Replace/Fix Strap ($35)? (Y/N): ").strip().upper()
    sv_polish = input("Surface Polish ($45)? (Y/N): ").strip().upper()

    batt_fee = 20.00 if sv_battery == 'Y' else 0.0
    strap_fee = 35.00 if sv_strap == 'Y' else 0.0
    polish_fee = 45.00 if sv_polish == 'Y' else 0.0
    sub_tot = batt_fee + strap_fee + polish_fee
    luxury_surchg = sub_tot * 0.25 if luxury_tier == 'Y' else 0.0
    grand_tot = sub_tot + luxury_surchg

    print("")
    print("========================================")
    print("            SERVICE TICKET              ")
    print("========================================")
    print(f"Client: {client_name}")
    print(f"Brand:  {watch_brand}")
    print("----------------------------------------")
    if sv_battery == 'Y':
        print(f"Battery Service:    ${batt_fee:,.2f}")
    if sv_strap == 'Y':
        print(f"Strap Replacement:  ${strap_fee:,.2f}")
    if sv_polish == 'Y':
        print(f"Polishing Service:  ${polish_fee:,.2f}")
    print("----------------------------------------")
    if luxury_tier == 'Y':
        print(f"Luxury Brand Fee:   ${luxury_surchg:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SERVICE COST: ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
