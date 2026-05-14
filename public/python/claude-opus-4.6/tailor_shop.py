"""
Fine Stitches Alterations - Tailor Shop
Converted from COBOL (tailor_shop.cbl) to Python
"""


def main():
    hem_rate, zip_rate, suit_rate = 15.00, 25.00, 120.00

    print("--- FINE STITCHES ALTERATIONS ---")
    cust_name = input("Customer Name: ")
    hemming_qty = int(input("Pants/Skirts Hemming QTY ($15 ea): "))
    zipper_qty = int(input("Zipper Replacements QTY ($25 ea): "))
    suit_fit_qty = int(input("Full Suit Tailoring QTY ($120 ea): "))
    rush_order = input("Rush Order (Next Day +30%)? (Y/N): ").strip().upper()

    hem_tot = hemming_qty * hem_rate
    zip_tot = zipper_qty * zip_rate
    suit_tot = suit_fit_qty * suit_rate
    sub_total = hem_tot + zip_tot + suit_tot
    rush_fee = sub_total * 0.30 if rush_order == "Y" else 0.0
    grand_tot = sub_total + rush_fee

    print()
    print("========================================")
    print("          ALTERATION TICKET             ")
    print("========================================")
    print(f"Name: {cust_name}")
    print("----------------------------------------")
    if hemming_qty > 0:
        print(f"{hemming_qty}x Hemming:          ${hem_tot:>9,.2f}")
    if zipper_qty > 0:
        print(f"{zipper_qty}x Zipper Fix:       ${zip_tot:>9,.2f}")
    if suit_fit_qty > 0:
        print(f"{suit_fit_qty}x Suit Tailoring:   ${suit_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:           ${sub_total:>9,.2f}")
    if rush_order == "Y":
        print(f"Rush Charge (30%):  ${rush_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
