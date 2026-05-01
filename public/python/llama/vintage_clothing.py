# VINTAGE-CLOTHING - Second Chance Thrift & Vintage
# Converted from COBOL to Python

def main():
    SHIRT_PRC = 15.00
    JACKET_PRC = 45.00
    PANT_PRC = 20.00

    print("--- SECOND CHANCE THRIFT & VINTAGE ---")
    shirt_qty = int(input("Graphic T-Shirts ($15.00 ea): "))
    jacket_qty = int(input("Leather/Denim Jackets ($45.00 ea): "))
    pants_qty = int(input("Vintage Pants/Jeans ($20.00 ea): "))
    donation = input("Donate $2 to Charity? (Y/N): ").strip().upper()

    sub_tot = (shirt_qty * SHIRT_PRC) + (jacket_qty * JACKET_PRC) + (pants_qty * PANT_PRC)
    discount = sub_tot * 0.15 if sub_tot > 100.00 else 0.0
    final_tot = sub_tot - discount
    if donation == 'Y':
        final_tot += 2.00

    print("")
    print("========================================")
    print("          SHOPPING RECEIPT              ")
    print("========================================")
    if shirt_qty > 0:
        print(f"{shirt_qty}x T-Shirts:         ${shirt_qty * SHIRT_PRC:,.2f}")
    if jacket_qty > 0:
        print(f"{jacket_qty}x Jackets:          ${jacket_qty * JACKET_PRC:,.2f}")
    if pants_qty > 0:
        print(f"{pants_qty}x Pants:            ${pants_qty * PANT_PRC:,.2f}")
    print("----------------------------------------")
    print(f"Cart Subtotal:      ${sub_tot:,.2f}")
    if discount > 0:
        print(f"Bulk Discount 15%: -${discount:,.2f}")
    if donation == 'Y':
        print("Charity Donation:    $    2.00")
    print("----------------------------------------")
    print(f"GRAND TOTAL:        ${final_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
