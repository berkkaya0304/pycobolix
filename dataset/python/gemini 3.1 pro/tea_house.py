def main():
    print("--- ZEN LEAF TEA HOUSE ---")
    patron_name = input("Name: ")
    try:
        green_tea_qty = int(input("Matcha/Green Tea QTY ($4.00): "))
    except ValueError:
        green_tea_qty = 0
    try:
        black_tea_qty = int(input("Earl Grey/Black Tea QTY ($3.50): "))
    except ValueError:
        black_tea_qty = 0
    try:
        herbal_tea_qty = int(input("Chamomile/Herbal QTY ($4.50): "))
    except ValueError:
        herbal_tea_qty = 0
    try:
        pastry_qty = int(input("Assorted Pastries ($5.00): "))
    except ValueError:
        pastry_qty = 0

    green_rt = 4.00
    black_rt = 3.50
    herbal_rt = 4.50
    pastry_rt = 5.00

    g_tot = green_tea_qty * green_rt
    b_tot = black_tea_qty * black_rt
    h_tot = herbal_tea_qty * herbal_rt
    p_tot = pastry_qty * pastry_rt

    grand_tot = g_tot + b_tot + h_tot + p_tot

    print("\n========================================")
    print("             TEA INVOICE                ")
    print("========================================")
    print(f"Patron: {patron_name}")
    print("----------------------------------------")
    
    if green_tea_qty > 0:
        print(f"{green_tea_qty:02d}x Green Teas:       ${g_tot:6.2f}")
    if black_tea_qty > 0:
        print(f"{black_tea_qty:02d}x Black Teas:       ${b_tot:6.2f}")
    if herbal_tea_qty > 0:
        print(f"{herbal_tea_qty:02d}x Herbal Teas:      ${h_tot:6.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty:02d}x Fresh Pastries:   ${p_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
