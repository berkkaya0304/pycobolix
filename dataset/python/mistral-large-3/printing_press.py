def printing_press():
    print("--- INKWELL PRINTING SERVICES ---")

    business_name = input("Business Name: ").strip()
    flyer_qty = int(input("Flyers QTY ($0.05 B&W): "))
    bcard_qty = int(input("Business Cards QTY ($0.02 B&W): "))
    color_ink = input("Upgrade to Full Color (+50% base)? (Y/N): ").upper() == 'Y'
    rush_print = input("Rush 24Hr Turnaround (+$25 flat)? (Y/N): ").upper() == 'Y'

    flyer_rate = 0.05
    bcard_rate = 0.02
    flyer_tot = flyer_qty * flyer_rate
    bcard_tot = bcard_qty * bcard_rate
    sub_tot = flyer_tot + bcard_tot

    color_fee = sub_tot * 0.5 if color_ink else 0.0
    rush_fee = 25.0 if rush_print else 0.0
    grand_tot = sub_tot + color_fee + rush_fee

    print("\n========================================")
    print("             PRINT INVOICE              ")
    print("========================================")
    print(f"Account: {business_name}")
    print("----------------------------------------")

    if flyer_qty > 0:
        print(f"Flyers (x{flyer_qty}):  ${flyer_tot:,.2f}")

    if bcard_qty > 0:
        print(f"Biz Cards (x{bcard_qty}): ${bcard_tot:,.2f}")

    if color_ink:
        print(f"Color Ink (+50%):  ${color_fee:,.2f}")

    if rush_print:
        print(f"Rush Handling:     ${rush_fee:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL ORDER COST:  ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    printing_press()
