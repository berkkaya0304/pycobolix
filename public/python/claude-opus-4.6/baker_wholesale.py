"""
Grain & Mill Wholesale Invoice
Converted from COBOL (baker_wholesale.cbl) to Python
"""


def main():
    flour_prc = 22.50
    sugar_prc = 28.00
    yeast_prc = 15.00

    print("--- GRAIN & MILL WHOLESALE ---")
    bakery_name = input("Bakery Name: ")
    flour_sacks = int(input("Flour Sacks (50lb, $22.50 ea): "))
    sugar_sacks = int(input("Sugar Sacks (50lb, $28.00 ea): "))
    yeast_blocks = int(input("Yeast Blocks (5lb, $15.00 ea): "))
    delivery = input("Require Freight Delivery ($150 flat)? (Y/N): ").strip().upper()

    f_tot = flour_sacks * flour_prc
    s_tot = sugar_sacks * sugar_prc
    y_tot = yeast_blocks * yeast_prc
    freight_fee = 150.00 if delivery == "Y" else 0.0
    grand_tot = f_tot + s_tot + y_tot + freight_fee

    print()
    print("========================================")
    print("           WHOLESALE INVOICE            ")
    print("========================================")
    print(f"Buyer: {bakery_name}")
    print("----------------------------------------")
    if flour_sacks > 0:
        print(f"Flour (x{flour_sacks}):      ${f_tot:>12,.2f}")
    if sugar_sacks > 0:
        print(f"Sugar (x{sugar_sacks}):      ${s_tot:>12,.2f}")
    if yeast_blocks > 0:
        print(f"Yeast (x{yeast_blocks}):      ${y_tot:>12,.2f}")
    if delivery == "Y":
        print(f"LTL Freight:    ${freight_fee:>12,.2f}")
    print("----------------------------------------")
    print(f"TOTAL DUE:      ${grand_tot:>12,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
