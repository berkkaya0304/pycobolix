def main():
    print("--- OAK BARREL VINEYARD ---")
    guest_name = input("Guest Name: ")
    tour_tier = input("Tasting (1=Basic $25, 2=Reserve $50): ").strip()
    try:
        red_wine_btl = int(input("Cabernet Bottles to Buy ($40 ea): "))
    except ValueError:
        red_wine_btl = 0
    try:
        wht_wine_btl = int(input("Chardonnay Bottles to Buy ($30 ea): "))
    except ValueError:
        wht_wine_btl = 0

    if tour_tier == '1':
        tour_fee = 25.00
    elif tour_tier == '2':
        tour_fee = 50.00
    else:
        tour_fee = 25.00

    red_fee = red_wine_btl * 40.00
    wht_fee = wht_wine_btl * 30.00

    case_discount = 0.0
    if (red_wine_btl + wht_wine_btl) >= 6:
        case_discount = (red_fee + wht_fee) * 0.10

    grand_tot = tour_fee + red_fee + wht_fee - case_discount

    print("\n========================================")
    print("            VINEYARD RECEIPT            ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print("----------------------------------------")
    print(f"Tasting Flight Fee: ${tour_fee:6.2f}")
    
    if red_wine_btl > 0:
        print(f"Cabernet ({red_wine_btl:02d}):       ${red_fee:6.2f}")
        
    if wht_wine_btl > 0:
        print(f"Chardonnay ({wht_wine_btl:02d}):     ${wht_fee:6.2f}")
        
    if case_discount > 0:
        print(f"Half-Case Disc 10%: -${case_discount:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:   ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
