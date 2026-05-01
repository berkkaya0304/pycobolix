def main():
    print("--- INKWELL PRINTING SERVICES ---")
    business_name = input("Business Name: ")
    try:
        flyer_qty = int(input("Flyers QTY ($0.05 B&W): "))
    except ValueError:
        flyer_qty = 0
    try:
        bcard_qty = int(input("Business Cards QTY ($0.02 B&W): "))
    except ValueError:
        bcard_qty = 0
    color_ink = input("Upgrade to Full Color (+50% base)? (Y/N): ").strip().upper() == 'Y'
    rush_print = input("Rush 24Hr Turnaround (+$25 flat)? (Y/N): ").strip().upper() == 'Y'

    flyer_rt = 0.05
    bcard_rt = 0.02
    
    flyer_tot = flyer_qty * flyer_rt
    bcard_tot = bcard_qty * bcard_rt

    sub_tot = flyer_tot + bcard_tot

    color_fee = 0.0
    if color_ink:
        color_fee = sub_tot * 0.50

    rush_fee = 0.0
    if rush_print:
        rush_fee = 25.00

    grand_tot = sub_tot + color_fee + rush_fee

    print("\n========================================")
    print("             PRINT INVOICE              ")
    print("========================================")
    print(f"Account: {business_name}")
    print("----------------------------------------")
    
    if flyer_qty > 0:
        print(f"Flyers (x{flyer_qty:05d}):  ${flyer_tot:7.2f}")
    if bcard_qty > 0:
        print(f"Biz Cards (x{bcard_qty:05d}):${bcard_tot:7.2f}")
        
    if color_ink:
        print(f"Color Ink (+50%):  ${color_fee:7.2f}")
        
    if rush_print:
        print(f"Rush Handling:     ${rush_fee:7.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL ORDER COST:  ${grand_tot:7.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
