def main():
    print("--- GRAIN & MILL WHOLESALE ---")
    bakery_name = input("Bakery Name: ")
    try:
        flour_sacks = int(input("Flour Sacks (50lb, $22.50 ea): ") or 0)
    except ValueError:
        flour_sacks = 0
    try:
        sugar_sacks = int(input("Sugar Sacks (50lb, $28.00 ea): ") or 0)
    except ValueError:
        sugar_sacks = 0
    try:
        yeast_blocks = int(input("Yeast Blocks (5lb, $15.00 ea): ") or 0)
    except ValueError:
        yeast_blocks = 0
    delivery = input("Require Freight Delivery ($150 flat)? (Y/N): ").strip().upper() == 'Y'

    flour_prc = 22.50
    sugar_prc = 28.00
    yeast_prc = 15.00

    f_tot = flour_sacks * flour_prc
    s_tot = sugar_sacks * sugar_prc
    y_tot = yeast_blocks * yeast_prc

    freight_fee = 150.00 if delivery else 0.0

    grand_tot = f_tot + s_tot + y_tot + freight_fee

    print("\n========================================")
    print("           WHOLESALE INVOICE            ")
    print("========================================")
    print(f"Buyer: {bakery_name}")
    print("----------------------------------------")
    
    if flour_sacks > 0:
        print(f"Flour (x{flour_sacks}):      ${f_tot:11.2f}")
    if sugar_sacks > 0:
        print(f"Sugar (x{sugar_sacks}):      ${s_tot:11.2f}")
    if yeast_blocks > 0:
        print(f"Yeast (x{yeast_blocks}):      ${y_tot:11.2f}")
    if delivery:
        print(f"LTL Freight:    ${freight_fee:11.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL DUE:      ${grand_tot:11.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
