def main():
    prices = {
        "succulents": 5.50,
        "ferns": 15.00,
        "trees": 45.00,
        "pots": 8.50,
        "soil": 12.00
    }

    print("--- BOTANICA PLANT NURSERY ---")
    
    try:
        suc_qty = int(input("Mini Succulents QTY ($5.50 ea): "))
        fern_qty = int(input("Ferns & Hanging Plants QTY ($15.00 ea): "))
        tree_qty = int(input("Small Info Trees QTY ($45.00 ea): "))
        pot_qty = int(input("Ceramic Pots ($8.50 ea): "))
        soil_qty = int(input("Bags of Potting Soil ($12.00 ea): "))
    except ValueError:
        print("Invalid input. Please enter numeric quantities.")
        return

    s_tot = suc_qty * prices["succulents"]
    f_tot = fern_qty * prices["ferns"]
    t_tot = tree_qty * prices["trees"]
    p_tot = pot_qty * prices["pots"]
    d_tot = soil_qty * prices["soil"]

    grand_tot = s_tot + f_tot + t_tot + p_tot + d_tot

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
        print(f"Ceramic Pots ({pot_qty}):      ${p_tot:,.2f}")
    if soil_qty > 0:
        print(f"Potting Soil ({soil_qty}):      ${d_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
