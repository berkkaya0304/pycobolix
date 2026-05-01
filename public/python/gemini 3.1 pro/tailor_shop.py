def main():
    print("--- FINE STITCHES ALTERATIONS ---")
    cust_name = input("Customer Name: ")
    try:
        hemming_qty = int(input("Pants/Skirts Hemming QTY ($15 ea): "))
    except ValueError:
        hemming_qty = 0
    try:
        zipper_qty = int(input("Zipper Replacements QTY ($25 ea): "))
    except ValueError:
        zipper_qty = 0
    try:
        suit_fit_qty = int(input("Full Suit Tailoring QTY ($120 ea): "))
    except ValueError:
        suit_fit_qty = 0
    rush_order = input("Rush Order (Next Day +30%)? (Y/N): ").strip().upper() == 'Y'

    hem_rate = 15.00
    zip_rate = 25.00
    suit_rate = 120.00

    hem_tot = hemming_qty * hem_rate
    zip_tot = zipper_qty * zip_rate
    suit_tot = suit_fit_qty * suit_rate

    sub_total = hem_tot + zip_tot + suit_tot

    rush_fee = 0.0
    if rush_order:
        rush_fee = sub_total * 0.30

    grand_tot = sub_total + rush_fee

    print("\n========================================")
    print("          ALTERATION TICKET             ")
    print("========================================")
    print(f"Name: {cust_name}")
    print("----------------------------------------")
    
    if hemming_qty > 0:
        print(f"{hemming_qty:02d}x Hemming:          ${hem_tot:6.2f}")
        
    if zipper_qty > 0:
        print(f"{zipper_qty:02d}x Zipper Fix:       ${zip_tot:6.2f}")
        
    if suit_fit_qty > 0:
        print(f"{suit_fit_qty:02d}x Suit Tailoring:   ${suit_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:           ${sub_total:6.2f}")
    
    if rush_order:
        print(f"Rush Charge (30%):  ${rush_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
