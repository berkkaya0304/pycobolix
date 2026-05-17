def main():
    # Pricing Constants
    SHIRT_PRICE = 15.00
    JACKET_PRICE = 45.00
    PANTS_PRICE = 20.00
    DONATION_AMOUNT = 2.00
    DISCOUNT_RATE = 0.15
    DISCOUNT_THRESHOLD = 100.00

    print("--- SECOND CHANCE THRIFT & VINTAGE ---")
    
    try:
        shirt_qty = int(input("Graphic T-Shirts ($15.00 ea): "))
        jacket_qty = int(input("Leather/Denim Jackets ($45.00 ea): "))
        pants_qty = int(input("Vintage Pants/Jeans ($20.00 ea): "))
        donation_choice = input("Donate $2 to Charity? (Y/N): ").strip().upper()
    except ValueError:
        print("Invalid input. Please enter numeric values for quantities.")
        return

    # Calculations
    sub_total = (shirt_qty * SHIRT_PRICE) + (jacket_qty * JACKET_PRICE) + (pants_qty * PANTS_PRICE)
    
    discount = 0.0
    if sub_total > DISCOUNT_THRESHOLD:
        discount = sub_total * DISCOUNT_RATE
    
    final_total = sub_total - discount
    
    wants_donate = (donation_choice == 'Y')
    if wants_donate:
        final_total += DONATION_AMOUNT

    # Receipt Output
    print("\n========================================")
    print("          SHOPPING RECEIPT              ")
    print("========================================")
    
    if shirt_qty > 0:
        print(f"{shirt_qty}x T-Shirts:         ${shirt_qty * SHIRT_PRICE:,.2f}")
    if jacket_qty > 0:
        print(f"{jacket_qty}x Jackets:          ${jacket_qty * JACKET_PRICE:,.2f}")
    if pants_qty > 0:
        print(f"{pants_qty}x Pants:            ${pants_qty * PANTS_PRICE:,.2f}")
        
    print("----------------------------------------")
    print(f"Cart Subtotal:      ${sub_total:,.2f}")
    
    if discount > 0:
        print(f"Bulk Discount 15%: -${discount:,.2f}")
        
    if wants_donate:
        print(f"Charity Donation:    $    {DONATION_AMOUNT:.2f}")
        
    print("----------------------------------------")
    print(f"GRAND TOTAL:        ${final_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
