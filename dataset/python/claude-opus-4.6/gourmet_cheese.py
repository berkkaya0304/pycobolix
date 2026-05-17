"""
The Rustic Wheel Cheese Shop
Converted from COBOL (gourmet_cheese.cbl) to Python
"""


def main():
    brie_pr = 18.50
    cheddar_pr = 12.00
    gouda_pr = 16.75
    cracker_pr = 4.50

    print("--- THE RUSTIC WHEEL CHEESE SHOP ---")
    brie_lbs = float(input("French Brie (lbs, $18.50/lb): "))
    cheddar_lbs = float(input("Aged Cheddar (lbs, $12.00/lb): "))
    gouda_lbs = float(input("Smoked Gouda (lbs, $16.75/lb): "))
    cracker_boxes = int(input("Artisan Cracker Boxes ($4.50 ea): "))

    b_tot = brie_lbs * brie_pr
    c_tot = cheddar_lbs * cheddar_pr
    g_tot = gouda_lbs * gouda_pr
    k_tot = cracker_boxes * cracker_pr
    grand_tot = b_tot + c_tot + g_tot + k_tot

    print()
    print("========================================")
    print("             SHOP RECEIPT               ")
    print("========================================")
    if brie_lbs > 0:
        print(f"Brie ({brie_lbs} lbs):        ${b_tot:>9,.2f}")
    if cheddar_lbs > 0:
        print(f"Cheddar ({cheddar_lbs} lbs):     ${c_tot:>9,.2f}")
    if gouda_lbs > 0:
        print(f"Gouda ({gouda_lbs} lbs):       ${g_tot:>9,.2f}")
    if cracker_boxes > 0:
        print(f"Crackers ({cracker_boxes} boxes):   ${k_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SALE:          ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
