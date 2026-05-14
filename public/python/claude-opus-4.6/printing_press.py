"""
Inkwell Printing Services
Converted from COBOL (printing_press.cbl) to Python
"""


def main():
    print("--- INKWELL PRINTING SERVICES ---")
    business_name = input("Business Name: ")
    flyer_qty = int(input("Flyers QTY ($0.05 B&W): "))
    bcard_qty = int(input("Business Cards QTY ($0.02 B&W): "))
    color_ink = input("Upgrade to Full Color (+50% base)? (Y/N): ").strip().upper()
    rush_print = input("Rush 24Hr Turnaround (+$25 flat)? (Y/N): ").strip().upper()

    flyer_tot = flyer_qty * 0.05
    bcard_tot = bcard_qty * 0.02
    sub_tot = flyer_tot + bcard_tot
    color_fee = sub_tot * 0.50 if color_ink == "Y" else 0.0
    rush_fee = 25.00 if rush_print == "Y" else 0.0
    grand_tot = sub_tot + color_fee + rush_fee

    print()
    print("========================================")
    print("             PRINT INVOICE              ")
    print("========================================")
    print(f"Account: {business_name}")
    print("----------------------------------------")
    if flyer_qty > 0:
        print(f"Flyers (x{flyer_qty}):  ${flyer_tot:>9,.2f}")
    if bcard_qty > 0:
        print(f"Biz Cards (x{bcard_qty}):${bcard_tot:>9,.2f}")
    if color_ink == "Y":
        print(f"Color Ink (+50%):  ${color_fee:>9,.2f}")
    if rush_print == "Y":
        print(f"Rush Handling:     ${rush_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL ORDER COST:  ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
