def main():
    print("--- BOTANICA PLANT NURSERY ---")
    try:
        suc_qty = int(input("Mini Succulents QTY ($5.50 ea): "))
    except ValueError:
        suc_qty = 0
    try:
        fern_qty = int(input("Ferns & Hanging Plants QTY ($15.00 ea): "))
    except ValueError:
        fern_qty = 0
    try:
        tree_qty = int(input("Small Info Trees QTY ($45.00 ea): "))
    except ValueError:
        tree_qty = 0
    try:
        pot_qty = int(input("Ceramic Pots ($8.50 ea): "))
    except ValueError:
        pot_qty = 0
    try:
        soil_bags = int(input("Bags of Potting Soil ($12.00 ea): "))
    except ValueError:
        soil_bags = 0

    suc_prc = 5.50
    fern_prc = 15.00
    tree_prc = 45.00
    pot_prc = 8.50
    soil_prc = 12.00

    s_tot = suc_qty * suc_prc
    f_tot = fern_qty * fern_prc
    t_tot = tree_qty * tree_prc
    p_tot = pot_qty * pot_prc
    d_tot = soil_bags * soil_prc

    grand_tot = s_tot + f_tot + t_tot + p_tot + d_tot

    print("\n========================================")
    print("            GARDEN RECEIPT              ")
    print("========================================")
    
    if suc_qty > 0:
        print(f"Succulents ({suc_qty:02d}):        ${s_tot:6.2f}")
    if fern_qty > 0:
        print(f"Ferns ({fern_qty:02d}):             ${f_tot:6.2f}")
    if tree_qty > 0:
        print(f"Trees ({tree_qty:02d}):             ${t_tot:6.2f}")
    if pot_qty > 0:
        print(f"Ceramic Pots ({pot_qty:02d}):      ${p_tot:6.2f}")
    if soil_bags > 0:
        print(f"Potting Soil ({soil_bags:02d}):      ${d_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
