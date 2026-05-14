"""
Zen Leaf Tea House
Converted from COBOL (tea_house.cbl) to Python
"""


def main():
    green_rt, black_rt, herbal_rt, pastry_rt = 4.00, 3.50, 4.50, 5.00

    print("--- ZEN LEAF TEA HOUSE ---")
    patron_name = input("Name: ")
    green_tea_qty = int(input("Matcha/Green Tea QTY ($4.00): "))
    black_tea_qty = int(input("Earl Grey/Black Tea QTY ($3.50): "))
    herbal_tea_qty = int(input("Chamomile/Herbal QTY ($4.50): "))
    pastry_qty = int(input("Assorted Pastries ($5.00): "))

    g_tot = green_tea_qty * green_rt
    b_tot = black_tea_qty * black_rt
    h_tot = herbal_tea_qty * herbal_rt
    p_tot = pastry_qty * pastry_rt
    grand_tot = g_tot + b_tot + h_tot + p_tot

    print()
    print("========================================")
    print("             TEA INVOICE                ")
    print("========================================")
    print(f"Patron: {patron_name}")
    print("----------------------------------------")
    if green_tea_qty > 0:
        print(f"{green_tea_qty}x Green Teas:       ${g_tot:>9,.2f}")
    if black_tea_qty > 0:
        print(f"{black_tea_qty}x Black Teas:       ${b_tot:>9,.2f}")
    if herbal_tea_qty > 0:
        print(f"{herbal_tea_qty}x Herbal Teas:      ${h_tot:>9,.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty}x Fresh Pastries:   ${p_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
