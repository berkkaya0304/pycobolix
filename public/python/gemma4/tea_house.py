def main():
    # Item Rates
    rates = {
        "green": 4.00,
        "black": 3.50,
        "herbal": 4.50,
        "pastry": 5.00
    }

    print("--- ZEN LEAF TEA HOUSE ---")
    
    # Input Section
    patron_name = input("Name: ")
    
    try:
        green_qty = int(input("Matcha/Green Tea QTY ($4.00): ") or 0)
        black_qty = int(input("Earl Grey/Black Tea QTY ($3.50): ") or 0)
        herbal_qty = int(input("Chamomile/Herbal QTY ($4.50): ") or 0)
        pastry_qty = int(input("Assorted Pastries ($5.00): ") or 0)
    except ValueError:
        print("Invalid input. Please enter numeric values for quantities.")
        return

    # Calculations
    g_tot = green_qty * rates["green"]
    b_tot = black_qty * rates["black"]
    h_tot = herbal_qty * rates["herbal"]
    p_tot = pastry_qty * rates["pastry"]
    
    grand_total = g_tot + b_tot + h_tot + p_tot

    # Invoice Display
    print("\n========================================")
    print("             TEA INVOICE                ")
    print("========================================")
    print(f"Patron: {patron_name}")
    print("----------------------------------------")

    if green_qty > 0:
        print(f"{green_qty}x Green Teas:       ${g_tot:,.2f}")
    if black_qty > 0:
        print(f"{black_qty}x Black Teas:       ${b_tot:,.2f}")
    if herbal_qty > 0:
        print(f"{herbal_qty}x Herbal Teas:      ${h_tot:,.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty}x Fresh Pastries:   ${p_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${grand_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
