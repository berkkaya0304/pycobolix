def main():
    # Constants for rates
    HEM_RATE = 15.00
    ZIP_RATE = 25.00
    SUIT_RATE = 120.00
    RUSH_MULTIPLIER = 0.30

    print("--- FINE STITCHES ALTERATIONS ---")
    
    # Input Section
    cust_name = input("Customer Name: ")
    try:
        hemming_qty = int(input("Pants/Skirts Hemming QTY ($15 ea): ") or 0)
        zipper_qty = int(input("Zipper Replacements QTY ($25 ea): ") or 0)
        suit_fit_qty = int(input("Full Suit Tailoring QTY ($120 ea): ") or 0)
    except ValueError:
        hemming_qty = zipper_qty = suit_fit_qty = 0

    rush_order = input("Rush Order (Next Day +30%)? (Y/N): ").strip().upper()
    is_rush = (rush_order == 'Y')

    # Calculations
    hem_tot = hemming_qty * HEM_RATE
    zip_tot = zipper_qty * ZIP_RATE
    suit_tot = suit_fit_qty * SUIT_RATE
    
    sub_total = hem_tot + zip_tot + suit_tot
    rush_fee = sub_total * RUSH_MULTIPLIER if is_rush else 0.0
    grand_tot = sub_total + rush_fee

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    # Output Section
    print("\n========================================")
    print("          ALTERATION TICKET             ")
    print("========================================")
    print(f"Name: {cust_name}")
    print("----------------------------------------")
    
    if hemming_qty > 0:
        print(f"{hemming_qty}x Hemming:          {format_currency(hem_tot)}")
    
    if zipper_qty > 0:
        print(f"{zipper_qty}x Zipper Fix:       {format_currency(zip_tot)}")
        
    if suit_fit_qty > 0:
        print(f"{suit_fit_qty}x Suit Tailoring:   {format_currency(suit_tot)}")
        
    print("----------------------------------------")
    print(f"Subtotal:           {format_currency(sub_total)}")
    
    if is_rush:
        print(f"Rush Charge (30%):  {format_currency(rush_fee)}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    main()
