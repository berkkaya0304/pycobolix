def gourmet_cheese():
    print("--- THE RUSTIC WHEEL CHEESE SHOP ---")

    brie_lbs = float(input("French Brie (lbs, $18.50/lb): "))
    cheddar_lbs = float(input("Aged Cheddar (lbs, $12.00/lb): "))
    gouda_lbs = float(input("Smoked Gouda (lbs, $16.75/lb): "))
    cracker_boxes = int(input("Artisan Cracker Boxes ($4.50 ea): "))

    prices = {
        'brie': 18.50,
        'cheddar': 12.00,
        'gouda': 16.75,
        'crackers': 4.50
    }

    b_tot = brie_lbs * prices['brie']
    c_tot = cheddar_lbs * prices['cheddar']
    g_tot = gouda_lbs * prices['gouda']
    k_tot = cracker_boxes * prices['crackers']
    grand_tot = b_tot + c_tot + g_tot + k_tot

    print("\n========================================")
    print("             SHOP RECEIPT               ")
    print("========================================")

    if brie_lbs > 0:
        print(f"Brie ({brie_lbs:.2f} lbs):        ${b_tot:,.2f}")
    if cheddar_lbs > 0:
        print(f"Cheddar ({cheddar_lbs:.2f} lbs):     ${c_tot:,.2f}")
    if gouda_lbs > 0:
        print(f"Gouda ({gouda_lbs:.2f} lbs):       ${g_tot:,.2f}")
    if cracker_boxes > 0:
        print(f"Crackers ({cracker_boxes} boxes):   ${k_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL SALE:          ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    gourmet_cheese()
