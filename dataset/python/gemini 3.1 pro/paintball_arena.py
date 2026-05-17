def main():
    print("--- SPLAT ZONE PAINTBALL ---")
    player_name = input("Player Name: ")
    try:
        paintball_qty = int(input("Paintballs to Buy (qty of 100s, $5 per 100): "))
    except ValueError:
        paintball_qty = 0
    gun_upgrade = input("Upgrade to Pro Marker Gun ($15)? (Y/N): ").strip().upper() == 'Y'

    admission_fee = 25.00
    paint_cost = (paintball_qty // 100) * 5.00
    gun_fee = 15.00 if gun_upgrade else 0.0

    sub_price = admission_fee + paint_cost + gun_fee
    tax_amt = sub_price * 0.07
    total_due = sub_price + tax_amt

    print("\n========================================")
    print("            ARENA INVOICE               ")
    print("========================================")
    print(f"Player: {player_name}")
    print("----------------------------------------")
    print(f"Basic Entry Fee:    ${admission_fee:6.2f}")
    
    if paintball_qty > 0:
        print(f"Extra Paint ({paintball_qty:04d}): ${paint_cost:6.2f}")
        
    if gun_upgrade:
        print(f"Pro Marker Upgrade: ${gun_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:           ${sub_price:6.2f}")
    print(f"Tax (7%):           ${tax_amt:6.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_due:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
