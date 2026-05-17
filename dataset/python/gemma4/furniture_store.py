def main():
    # Prices
    SOFA_PRC = 599.00
    TABLE_PRC = 349.00
    CHAIR_PRC = 85.00
    DELIV_FEE_AMOUNT = 99.00

    print("--- COZY LIVING FURNITURE ---")
    
    buyer_name = input("Customer: ")
    
    try:
        sofa_qty = int(input("Sectional Sofas ($599.00 ea): ") or 0)
        table_qty = int(input("Dining Tables ($349.00 ea): ") or 0)
        chair_qty = int(input("Dining Chairs ($85.00 ea): ") or 0)
    except ValueError:
        print("Invalid quantity entered. Defaulting to 0.")
        sofa_qty = table_qty = chair_qty = 0

    home_delivery = input("White-Glove Delivery ($99 flat)? (Y/N): ").strip().upper()
    wants_deliv = (home_delivery == 'Y')

    # Calculations
    s_tot = sofa_qty * SOFA_PRC
    t_tot = table_qty * TABLE_PRC
    c_tot = chair_qty * CHAIR_PRC
    
    deliv_fee = DELIV_FEE_AMOUNT if wants_deliv else 0.0
    grand_tot = s_tot + t_tot + c_tot + deliv_fee

    # Receipt Output
    print("\n========================================")
    print("             STORE RECEIPT              ")
    print("========================================")
    print(f"Customer: {buyer_name}")
    print("----------------------------------------")

    if sofa_qty > 0:
        print(f"Sofas ({sofa_qty}):           ${s_tot:,.2f}")
    
    if table_qty > 0:
        print(f"Tables ({table_qty}):          ${t_tot:,.2f}")
        
    if chair_qty > 0:
        print(f"Chairs ({chair_qty}):          ${c_tot:,.2f}")
        
    if wants_deliv:
        print(f"Delivery Fee:       ${deliv_fee:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL ORDER:        ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
