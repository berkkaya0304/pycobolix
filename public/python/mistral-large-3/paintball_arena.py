def paintball_arena():
    print("--- SPLAT ZONE PAINTBALL ---")
    player_name = input("Player Name: ").strip()
    paintball_qty = int(input("Paintballs to Buy (qty of 100s, $5 per 100): "))
    gun_upgrade = input("Upgrade to Pro Marker Gun ($15)? (Y/N): ").strip().upper() == 'Y'

    admission_fee = 25.00
    paint_cost = (paintball_qty / 100) * 5.00
    gun_fee = 15.00 if gun_upgrade else 0.00

    sub_price = admission_fee + paint_cost + gun_fee
    tax_amt = sub_price * 0.07
    total_due = sub_price + tax_amt

    def format_currency(value):
        return f"${value:,.2f}"

    print("\n========================================")
    print("            ARENA INVOICE               ")
    print("========================================")
    print(f"Player: {player_name}")
    print("----------------------------------------")
    print(f"Basic Entry Fee:    {format_currency(admission_fee)}")

    if paintball_qty > 0:
        print(f"Extra Paint ({paintball_qty}): {format_currency(paint_cost)}")

    if gun_upgrade:
        print(f"Pro Marker Upgrade: {format_currency(gun_fee)}")

    print("----------------------------------------")
    print(f"Subtotal:           {format_currency(sub_price)}")
    print(f"Tax (7%):           {format_currency(tax_amt)}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      {format_currency(total_due)}")
    print("========================================")

if __name__ == "__main__":
    paintball_arena()
