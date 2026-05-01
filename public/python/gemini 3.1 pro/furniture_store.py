def main():
    print("--- COZY LIVING FURNITURE ---")
    buyer_name = input("Customer: ")
    try:
        sofa_qty = int(input("Sectional Sofas ($599.00 ea): "))
    except ValueError:
        sofa_qty = 0
    try:
        table_qty = int(input("Dining Tables ($349.00 ea): "))
    except ValueError:
        table_qty = 0
    try:
        chair_qty = int(input("Dining Chairs ($85.00 ea): "))
    except ValueError:
        chair_qty = 0
    home_delivery = input("White-Glove Delivery ($99 flat)? (Y/N): ").strip().upper() == 'Y'

    sofa_prc = 599.00
    table_prc = 349.00
    chair_prc = 85.00

    s_tot = sofa_qty * sofa_prc
    t_tot = table_qty * table_prc
    c_tot = chair_qty * chair_prc

    deliv_fee = 99.00 if home_delivery else 0.0

    grand_tot = s_tot + t_tot + c_tot + deliv_fee

    print("\n========================================")
    print("             STORE RECEIPT              ")
    print("========================================")
    print(f"Customer: {buyer_name}")
    print("----------------------------------------")
    
    if sofa_qty > 0:
        print(f"Sofas ({sofa_qty}):           ${s_tot:7.2f}")
    if table_qty > 0:
        print(f"Tables ({table_qty}):          ${t_tot:7.2f}")
    if chair_qty > 0:
        print(f"Chairs ({chair_qty}):          ${c_tot:7.2f}")
    if home_delivery:
        print(f"Delivery Fee:       ${deliv_fee:7.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL ORDER:        ${grand_tot:7.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
