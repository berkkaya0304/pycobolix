def main():
    print("--- SECOND CHANCE THRIFT & VINTAGE ---")
    try:
        shirt_qty = int(input("Graphic T-Shirts ($15.00 ea): "))
    except ValueError:
        shirt_qty = 0
    try:
        jacket_qty = int(input("Leather/Denim Jackets ($45.00 ea): "))
    except ValueError:
        jacket_qty = 0
    try:
        pants_qty = int(input("Vintage Pants/Jeans ($20.00 ea): "))
    except ValueError:
        pants_qty = 0
    wants_donate = input("Donate $2 to Charity? (Y/N): ").strip().upper() == 'Y'

    shirt_prc = 15.00
    jacket_prc = 45.00
    pant_prc = 20.00

    sub_tot = (shirt_qty * shirt_prc) + (jacket_qty * jacket_prc) + (pants_qty * pant_prc)

    discount = 0.0
    if sub_tot > 100.00:
        discount = sub_tot * 0.15

    final_tot = sub_tot - discount

    if wants_donate:
        final_tot += 2.00

    print("\n========================================")
    print("          SHOPPING RECEIPT              ")
    print("========================================")
    if shirt_qty > 0:
        print(f"{shirt_qty:02d}x T-Shirts:         ${(shirt_qty * shirt_prc):6.2f}")
    if jacket_qty > 0:
        print(f"{jacket_qty:02d}x Jackets:          ${(jacket_qty * jacket_prc):6.2f}")
    if pants_qty > 0:
        print(f"{pants_qty:02d}x Pants:            ${(pants_qty * pant_prc):6.2f}")
        
    print("----------------------------------------")
    print(f"Cart Subtotal:      ${sub_tot:6.2f}")
    
    if discount > 0:
        print(f"Bulk Discount 15%: -${discount:6.2f}")
        
    if wants_donate:
        print("Charity Donation:    $  2.00")
        
    print("----------------------------------------")
    print(f"GRAND TOTAL:        ${final_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
