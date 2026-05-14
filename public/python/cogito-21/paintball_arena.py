def main():
    print("--- SPLAT ZONE PAINTBALL ---")
    player_name = input("Player Name: ").strip()
    
    while True:
        try:
            paintball_qty = int(input("Paintballs to Buy (qty of 100s, $5 per 100): ").strip())
            if paintball_qty < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        gun_upgrade = input("Upgrade to Pro Marker Gun ($15)? (Y/N): ").strip().upper()
        if gun_upgrade in ['Y', 'N']:
            break
        print("Please enter 'Y' or 'N'.")
    
    admission_fee = 25.00
    paint_cost = (paintball_qty / 100) * 5.00
    gun_fee = 15.00 if gun_upgrade == 'Y' else 0.00
    
    sub_price = admission_fee + paint_cost + gun_fee
    tax_amt = sub_price * 0.07
    total_due = sub_price + tax_amt
    
    print("\n" + "=" * 40)
    print("            ARENA INVOICE               ")
    print("=" * 40)
    print(f"Player: {player_name}")
    print("-" * 40)
    print(f"Basic Entry Fee:    ${admission_fee:>7.2f}")
    
    if paintball_qty > 0:
        print(f"Extra Paint ({paintball_qty}): ${paint_cost:>7.2f}")
    
    if gun_upgrade == 'Y':
        print(f"Pro Marker Upgrade: ${gun_fee:>7.2f}")
    
    print("-" * 40)
    print(f"Subtotal:           ${sub_price:>7.2f}")
    print(f"Tax (7%):           ${tax_amt:>7.2f}")
    print("-" * 40)
    print(f"TOTAL BALANCE:      ${total_due:>7.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
