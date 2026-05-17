def tea_house():
    print("--- ZEN LEAF TEA HOUSE ---")

    patron_name = input("Name: ").strip()
    green_tea_qty = int(input("Matcha/Green Tea QTY ($4.00): "))
    black_tea_qty = int(input("Earl Grey/Black Tea QTY ($3.50): "))
    herbal_tea_qty = int(input("Chamomile/Herbal QTY ($4.50): "))
    pastry_qty = int(input("Assorted Pastries ($5.00): "))

    green_rate = 4.00
    black_rate = 3.50
    herbal_rate = 4.50
    pastry_rate = 5.00

    g_tot = green_tea_qty * green_rate
    b_tot = black_tea_qty * black_rate
    h_tot = herbal_tea_qty * herbal_rate
    p_tot = pastry_qty * pastry_rate
    grand_tot = g_tot + b_tot + h_tot + p_tot

    print("")
    print("=" * 40)
    print("             TEA INVOICE                ")
    print("=" * 40)
    print(f"Patron: {patron_name}")
    print("-" * 40)

    if green_tea_qty > 0:
        print(f"{green_tea_qty}x Green Teas:       ${g_tot:,.2f}")
    if black_tea_qty > 0:
        print(f"{black_tea_qty}x Black Teas:       ${b_tot:,.2f}")
    if herbal_tea_qty > 0:
        print(f"{herbal_tea_qty}x Herbal Teas:      ${h_tot:,.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty}x Fresh Pastries:   ${p_tot:,.2f}")

    print("-" * 40)
    print(f"TOTAL BALANCE:       ${grand_tot:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    tea_house()
