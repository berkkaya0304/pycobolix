# WINE-TASTING - Oak Barrel Vineyard
# Converted from COBOL to Python

def main():
    print("--- OAK BARREL VINEYARD ---")
    guest_name = input("Guest Name: ")
    tour_tier = int(input("Tasting (1=Basic $25, 2=Reserve $50): "))
    red_wine_btl = int(input("Cabernet Bottles to Buy ($40 ea): "))
    wht_wine_btl = int(input("Chardonnay Bottles to Buy ($30 ea): "))

    if tour_tier == 1:
        tour_fee = 25.00
    elif tour_tier == 2:
        tour_fee = 50.00
    else:
        tour_fee = 25.00

    red_fee = red_wine_btl * 40.00
    wht_fee = wht_wine_btl * 30.00

    case_discount = 0.0
    if (red_wine_btl + wht_wine_btl) >= 6:
        case_discount = (red_fee + wht_fee) * 0.10

    grand_tot = tour_fee + red_fee + wht_fee - case_discount

    print("")
    print("========================================")
    print("            VINEYARD RECEIPT            ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print("----------------------------------------")
    print(f"Tasting Flight Fee: ${tour_fee:,.2f}")
    if red_wine_btl > 0:
        print(f"Cabernet ({red_wine_btl}):       ${red_fee:,.2f}")
    if wht_wine_btl > 0:
        print(f"Chardonnay ({wht_wine_btl}):     ${wht_fee:,.2f}")
    if case_discount > 0:
        print(f"Half-Case Disc 10%: -${case_discount:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:   ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
