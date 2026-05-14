def main():
    print("--- OAK BARREL VINEYARD ---")
    guest_name = input("Guest Name: ")
    
    while True:
        try:
            tour_tier = int(input("Tasting (1=Basic $25, 2=Reserve $50): "))
            if tour_tier in (1, 2):
                break
            print("Please enter 1 for Basic or 2 for Reserve.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            red_wine_btl = int(input("Cabernet Bottles to Buy ($40 ea): "))
            if red_wine_btl >= 0:
                break
            print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            wht_wine_btl = int(input("Chardonnay Bottles to Buy ($30 ea): "))
            if wht_wine_btl >= 0:
                break
            print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
    
    tour_fee = 50.00 if tour_tier == 2 else 25.00
    red_fee = red_wine_btl * 40.00
    wht_fee = wht_wine_btl * 30.00
    case_discount = 0.00
    
    if (red_wine_btl + wht_wine_btl) >= 6:
        case_discount = (red_fee + wht_fee) * 0.10
    
    grand_total = tour_fee + red_fee + wht_fee - case_discount
    
    print("\n" + "=" * 40)
    print("            VINEYARD RECEIPT            ")
    print("=" * 40)
    print(f"Guest: {guest_name}")
    print("-" * 40)
    print(f"Tasting Flight Fee: ${tour_fee:,.2f}")
    
    if red_wine_btl > 0:
        print(f"Cabernet ({red_wine_btl}):       ${red_fee:,.2f}")
    if wht_wine_btl > 0:
        print(f"Chardonnay ({wht_wine_btl}):     ${wht_fee:,.2f}")
    if case_discount > 0:
        print(f"Half-Case Disc 10%: -${case_discount:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:   ${grand_total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
