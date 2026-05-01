# PLANT-NURSERY - Botanica Plant Nursery
# Converted from COBOL to Python

def main():
    SUC_PRC = 5.50
    FERN_PRC = 15.00
    TREE_PRC = 45.00
    POT_PRC = 8.50
    SOIL_PRC = 12.00

    print("--- BOTANICA PLANT NURSERY ---")
    suc_qty = int(input("Mini Succulents QTY ($5.50 ea): "))
    fern_qty = int(input("Ferns & Hanging Plants QTY ($15.00 ea): "))
    tree_qty = int(input("Small Info Trees QTY ($45.00 ea): "))
    pot_qty = int(input("Ceramic Pots ($8.50 ea): "))
    soil_bags = int(input("Bags of Potting Soil ($12.00 ea): "))

    s_tot = suc_qty * SUC_PRC
    f_tot = fern_qty * FERN_PRC
    t_tot = tree_qty * TREE_PRC
    p_tot = pot_qty * POT_PRC
    d_tot = soil_bags * SOIL_PRC
    grand_tot = s_tot + f_tot + t_tot + p_tot + d_tot

    print("")
    print("========================================")
    print("            GARDEN RECEIPT              ")
    print("========================================")
    if suc_qty > 0:
        print(f"Succulents ({suc_qty}):        ${s_tot:,.2f}")
    if fern_qty > 0:
        print(f"Ferns ({fern_qty}):             ${f_tot:,.2f}")
    if tree_qty > 0:
        print(f"Trees ({tree_qty}):             ${t_tot:,.2f}")
    if pot_qty > 0:
        print(f"Ceramic Pots ({pot_qty}):      ${p_tot:,.2f}")
    if soil_bags > 0:
        print(f"Potting Soil ({soil_bags}):      ${d_tot:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
