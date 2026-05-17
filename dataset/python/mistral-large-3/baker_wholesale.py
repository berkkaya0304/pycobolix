def baker_wholesale():
    print("--- GRAIN & MILL WHOLESALE ---")
    bakery_name = input("Bakery Name: ").strip()
    flour_sacks = int(input("Flour Sacks (50lb, $22.50 ea): "))
    sugar_sacks = int(input("Sugar Sacks (50lb, $28.00 ea): "))
    yeast_blocks = int(input("Yeast Blocks (5lb, $15.00 ea): "))
    delivery = input("Require Freight Delivery ($150 flat)? (Y/N): ").strip().upper() == 'Y'

    flour_prc = 22.50
    sugar_prc = 28.00
    yeast_prc = 15.00

    f_tot = flour_sacks * flour_prc
    s_tot = sugar_sacks * sugar_prc
    y_tot = yeast_blocks * yeast_prc
    freight_fee = 150.00 if delivery else 0.00
    grand_tot = f_tot + s_tot + y_tot + freight_fee

    def format_currency(value):
        return "${:,.2f}".format(value)

    print("")
    print("========================================")
    print("           WHOLESALE INVOICE            ")
    print("========================================")
    print(f"Buyer: {bakery_name}")
    print("----------------------------------------")

    if flour_sacks > 0:
        print(f"Flour (x{flour_sacks}):      {format_currency(f_tot)}")
    if sugar_sacks > 0:
        print(f"Sugar (x{sugar_sacks}):      {format_currency(s_tot)}")
    if yeast_blocks > 0:
        print(f"Yeast (x{yeast_blocks}):      {format_currency(y_tot)}")
    if delivery:
        print(f"LTL Freight:    {format_currency(freight_fee)}")

    print("----------------------------------------")
    print(f"TOTAL DUE:      {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    baker_wholesale()
