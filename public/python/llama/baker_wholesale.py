# BAKER-WHOLESALE - Grain & Mill Wholesale
# Converted from COBOL to Python

def main():
    FLOUR_PRC = 22.50
    SUGAR_PRC = 28.00
    YEAST_PRC = 15.00

    print("--- GRAIN & MILL WHOLESALE ---")
    bakery_name = input("Bakery Name: ")
    flour_sacks = int(input("Flour Sacks (50lb, $22.50 ea): "))
    sugar_sacks = int(input("Sugar Sacks (50lb, $28.00 ea): "))
    yeast_blocks = int(input("Yeast Blocks (5lb, $15.00 ea): "))
    delivery = input("Require Freight Delivery ($150 flat)? (Y/N): ").strip().upper()

    f_tot = flour_sacks * FLOUR_PRC
    s_tot = sugar_sacks * SUGAR_PRC
    y_tot = yeast_blocks * YEAST_PRC
    freight_fee = 150.00 if delivery == 'Y' else 0.0
    grand_tot = f_tot + s_tot + y_tot + freight_fee

    print("")
    print("========================================")
    print("           WHOLESALE INVOICE            ")
    print("========================================")
    print(f"Buyer: {bakery_name}")
    print("----------------------------------------")
    if flour_sacks > 0:
        print(f"Flour (x{flour_sacks}):      ${f_tot:,.2f}")
    if sugar_sacks > 0:
        print(f"Sugar (x{sugar_sacks}):      ${s_tot:,.2f}")
    if yeast_blocks > 0:
        print(f"Yeast (x{yeast_blocks}):      ${y_tot:,.2f}")
    if delivery == 'Y':
        print(f"LTL Freight:    ${freight_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL DUE:      ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
