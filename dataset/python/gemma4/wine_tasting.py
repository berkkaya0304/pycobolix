def main():
    print("--- OAK BARREL VINEYARD ---")
    
    guest_name = input("Guest Name: ")
    
    try:
        tour_tier = int(input("Tasting (1=Basic $25, 2=Reserve $50): "))
    except ValueError:
        tour_tier = 1

    try:
        red_wine_btl = int(input("Cabernet Bottles to Buy ($40 ea): "))
    except ValueError:
        red_wine_btl = 0

    try:
        wht_wine_btl = int(input("Chardonnay Bottles to Buy ($30 ea): "))
    except ValueError:
        wht_wine_btl = 0

    # Determine Tour Fee
    if tour_tier == 2:
        tour_fee = 50.00
    else:
        tour_fee = 25.00

    # Calculate Wine Fees
    red_fee = red_wine_btl * 40.00
    wht_fee = wht_wine_btl * 30.00

    # Calculate Discount
    case_discount = 0.00
    if (red_wine_btl + wht_wine_btl) >= 6:
        case_discount = (red_fee + wht_fee) * 0.10

    # Calculate Grand Total
    grand_tot = tour_fee + red_fee + wht_fee - case_discount

    # Formatting helper for currency
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("            VINEYARD RECEIPT            ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print("----------------------------------------")
    print(f"Tasting Flight Fee: {format_currency(tour_fee)}")
    
    if red_wine_btl > 0:
        print(f"Cabernet ({red_wine_btl}):       {format_currency(red_fee)}")
    
    if wht_wine_btl > 0:
        print(f"Chardonnay ({wht_wine_btl}):     {format_currency(wht_fee)}")
        
    if case_discount > 0:
        print(f"Half-Case Disc 10%: -{format_currency(case_discount)}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:   {format_currency(grand_tot)}")
    print("========================================")

if __name__ == "__main__":
    main()
