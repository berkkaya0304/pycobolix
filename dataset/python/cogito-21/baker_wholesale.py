def main():
    print("--- GRAIN & MILL WHOLESALE ---")
    bakery_name = input("Bakery Name: ")
    
    flour_sacks = int(input("Flour Sacks (50lb, $22.50 ea): "))
    sugar_sacks = int(input("Sugar Sacks (50lb, $28.00 ea): "))
    yeast_blocks = int(input("Yeast Blocks (5lb, $15.00 ea): "))
    delivery = input("Require Freight Delivery ($150 flat)? (Y/N): ").strip().upper()
    
    flour_price = 22.50
    sugar_price = 28.00
    yeast_price = 15.00
    
    flour_total = flour_sacks * flour_price
    sugar_total = sugar_sacks * sugar_price
    yeast_total = yeast_blocks * yeast_price
    
    freight_fee = 150.00 if delivery == 'Y' else 0.00
    
    grand_total = flour_total + sugar_total + yeast_total + freight_fee
    
    print("\n" + "=" * 40)
    print("           WHOLESALE INVOICE            ")
    print("=" * 40)
    print(f"Buyer: {bakery_name}")
    print("-" * 40)
    
    if flour_sacks > 0:
        print(f"Flour (x{flour_sacks}):      ${flour_total:,.2f}")
    if sugar_sacks > 0:
        print(f"Sugar (x{sugar_sacks}):      ${sugar_total:,.2f}")
    if yeast_blocks > 0:
        print(f"Yeast (x{yeast_blocks}):      ${yeast_total:,.2f}")
    if delivery == 'Y':
        print(f"LTL Freight:    ${freight_fee:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL DUE:      ${grand_total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
