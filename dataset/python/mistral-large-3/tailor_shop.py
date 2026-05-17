def tailor_shop():
    print("--- FINE STITCHES ALTERATIONS ---")
    cust_name = input("Customer Name: ").strip()
    hemming_qty = int(input("Pants/Skirts Hemming QTY ($15 ea): "))
    zipper_qty = int(input("Zipper Replacements QTY ($25 ea): "))
    suit_fit_qty = int(input("Full Suit Tailoring QTY ($120 ea): "))
    rush_order = input("Rush Order (Next Day +30%)? (Y/N): ").strip().upper() == 'Y'

    hem_rate = 15.00
    zip_rate = 25.00
    suit_rate = 120.00

    hem_tot = hemming_qty * hem_rate
    zip_tot = zipper_qty * zip_rate
    suit_tot = suit_fit_qty * suit_rate

    sub_total = hem_tot + zip_tot + suit_tot
    rush_fee = sub_total * 0.30 if rush_order else 0.00
    grand_tot = sub_total + rush_fee

    def format_currency(value):
        return f"${value:,.2f}"

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

    if rush_order:
        print(f"Rush Charge (30%):  {format_currency(rush_fee)}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:      {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    tailor_shop()
