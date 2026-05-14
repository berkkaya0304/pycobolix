def main():
    print("--- SECOND CHANCE THRIFT & VINTAGE ---")
    
    shirt_qty = int(input("Graphic T-Shirts ($15.00 ea): "))
    jacket_qty = int(input("Leather/Denim Jackets ($45.00 ea): "))
    pants_qty = int(input("Vintage Pants/Jeans ($20.00 ea): "))
    donation = input("Donate $2 to Charity? (Y/N): ").strip().upper()
    
    shirt_prc = 15.00
    jacket_prc = 45.00
    pant_prc = 20.00
    
    sub_tot = (shirt_qty * shirt_prc) + (jacket_qty * jacket_prc) + (pants_qty * pant_prc)
    
    discount = 0.00
    if sub_tot > 100.00:
        discount = sub_tot * 0.15
    
    final_tot = sub_tot - discount
    
    if donation == 'Y':
        final_tot += 2.00
    
    print("\n" + "=" * 40)
    print("          SHOPPING RECEIPT              ")
    print("=" * 40)
    
    if shirt_qty > 0:
        print(f"{shirt_qty}x T-Shirts:         ${shirt_qty * shirt_prc:7.2f}")
    if jacket_qty > 0:
        print(f"{jacket_qty}x Jackets:          ${jacket_qty * jacket_prc:7.2f}")
    if pants_qty > 0:
        print(f"{pants_qty}x Pants:            ${pants_qty * pant_prc:7.2f}")
    
    print("-" * 40)
    print(f"Cart Subtotal:      ${sub_tot:7.2f}")
    
    if discount > 0:
        print(f"Bulk Discount 15%: -${discount:7.2f}")
    
    if donation == 'Y':
        print("Charity Donation:    $    2.00")
    
    print("-" * 40)
    print(f"GRAND TOTAL:        ${final_tot:7.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
