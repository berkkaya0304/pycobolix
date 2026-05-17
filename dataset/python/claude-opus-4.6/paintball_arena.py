"""
Splat Zone Paintball Arena
Converted from COBOL (paintball_arena.cbl) to Python
"""


def main():
    admission_fee = 25.00

    print("--- SPLAT ZONE PAINTBALL ---")
    player_name = input("Player Name: ")
    paintball_qty = int(input("Paintballs to Buy (qty of 100s, $5 per 100): "))
    gun_upgrade = input("Upgrade to Pro Marker Gun ($15)? (Y/N): ").strip().upper()

    paint_cost = (paintball_qty / 100) * 5.00
    gun_fee = 15.00 if gun_upgrade == "Y" else 0.0
    sub_price = admission_fee + paint_cost + gun_fee
    tax_amt = sub_price * 0.07
    total_due = sub_price + tax_amt

    print()
    print("========================================")
    print("            ARENA INVOICE               ")
    print("========================================")
    print(f"Player: {player_name}")
    print("----------------------------------------")
    print(f"Basic Entry Fee:    ${admission_fee:>9,.2f}")
    if paintball_qty > 0:
        print(f"Extra Paint ({paintball_qty}): ${paint_cost:>9,.2f}")
    if gun_upgrade == "Y":
        print(f"Pro Marker Upgrade: ${gun_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:           ${sub_price:>9,.2f}")
    print(f"Tax (7%):           ${tax_amt:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_due:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
