def plant_nursery():
    print("--- BOTANICA PLANT NURSERY ---")

    # Get quantities from user
    suc_qty = int(input("Mini Succulents QTY ($5.50 ea): "))
    fern_qty = int(input("Ferns & Hanging Plants QTY ($15.00 ea): "))
    tree_qty = int(input("Small Info Trees QTY ($45.00 ea): "))
    pot_qty = int(input("Ceramic Pots ($8.50 ea): "))
    soil_bags = int(input("Bags of Potting Soil ($12.00 ea): "))

    # Prices
    prices = {
        'succulent': 5.50,
        'fern': 15.00,
        'tree': 45.00,
        'pot': 8.50,
        'soil': 12.00
    }

    # Calculate totals
    s_tot = suc_qty * prices['succulent']
    f_tot = fern_qty * prices['fern']
    t_tot = tree_qty * prices['tree']
    p_tot = pot_qty * prices['pot']
    d_tot = soil_bags * prices['soil']
    grand_tot = s_tot + f_tot + t_tot + p_tot + d_tot

    # Display receipt
    print("\n========================================")
    print("            GARDEN RECEIPT              ")
    print("========================================")

    if suc_qty > 0:
        print(f"Succulents ({suc_qty}):        ${s_tot:,.2f}")
    if fern_qty > 0:
        print(f"Ferns ({fern_qty}):             ${f_tot:,.2f}")
    if tree_qty > 0:
        print(f"Trees ({tree_qty}):             ${t_tot:,.2f}")
    if pot_qty > 0:
        print(f"Ceramic Pots ({pot_qty}):       ${p_tot:,.2f}")
    if soil_bags > 0:
        print(f"Potting Soil ({soil_bags}):     ${d_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    plant_nursery()
