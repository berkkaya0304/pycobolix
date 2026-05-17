def main():
    # Constants
    ADMISSION_FEE = 25.00
    PAINT_UNIT_PRICE = 5.00
    PRO_GUN_FEE = 15.00
    TAX_RATE = 0.07

    print("--- SPLAT ZONE PAINTBALL ---")
    
    player_name = input("Player Name: ")
    
    try:
        paintball_qty = int(input("Paintballs to Buy (qty of 100s, $5 per 100): "))
    except ValueError:
        paintball_qty = 0
        
    gun_upgrade = input("Upgrade to Pro Marker Gun ($15)? (Y/N): ").strip().upper()

    # Calculations
    paint_cost = (paintball_qty / 100) * PAINT_UNIT_PRICE if paintball_qty > 0 else 0.0
    gun_fee = PRO_GUN_FEE if gun_upgrade == 'Y' else 0.0
    
    sub_price = ADMISSION_FEE + paint_cost + gun_fee
    tax_amt = sub_price * TAX_RATE
    total_due = sub_price + tax_amt

    # Invoice Display
    print("\n========================================")
    print("            ARENA INVOICE               ")
    print("========================================")
    print(f"Player: {player_name}")
    print("----------------------------------------")
    print(f"Basic Entry Fee:    ${ADMISSION_FEE:,.2f}")
    
    if paintball_qty > 0:
        print(f"Extra Paint ({paintball_qty}): ${paint_cost:,.2f}")
        
    if gun_upgrade == 'Y':
        print(f"Pro Marker Upgrade: ${gun_fee:,.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:           ${sub_price:,.2f}")
    print(f"Tax (7%):           ${tax_amt:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
