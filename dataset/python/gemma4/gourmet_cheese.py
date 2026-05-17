from decimal import Decimal, ROUND_HALF_UP

def main():
    # Prices
    PRICES = {
        "brie": Decimal("18.50"),
        "cheddar": Decimal("12.00"),
        "gouda": Decimal("16.75"),
        "crackers": Decimal("4.50")
    }

    print("--- THE RUSTIC WHEEL CHEESE SHOP ---")
    
    try:
        brie_lbs = Decimal(input("French Brie (lbs, $18.50/lb): ") or "0")
        cheddar_lbs = Decimal(input("Aged Cheddar (lbs, $12.00/lb): ") or "0")
        gouda_lbs = Decimal(input("Smoked Gouda (lbs, $16.75/lb): ") or "0")
        cracker_boxes = Decimal(input("Artisan Cracker Boxes ($4.50 ea): ") or "0")
    except Exception:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculations
    b_tot = (brie_lbs * PRICES["brie"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    c_tot = (cheddar_lbs * PRICES["cheddar"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    g_tot = (gouda_lbs * PRICES["gouda"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    k_tot = (cracker_boxes * PRICES["crackers"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    grand_tot = b_tot + c_tot + g_tot + k_tot

    print("\n========================================")
    print("             SHOP RECEIPT               ")
    print("========================================")

    if brie_lbs > 0:
        print(f"Brie ({brie_lbs} lbs):        ${b_tot:,.2f}")
    if cheddar_lbs > 0:
        print(f"Cheddar ({cheddar_lbs} lbs):     ${c_tot:,.2f}")
    if gouda_lbs > 0:
        print(f"Gouda ({gouda_lbs} lbs):       ${g_tot:,.2f}")
    if cracker_boxes > 0:
        print(f"Crackers ({cracker_boxes} boxes):   ${k_tot:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL SALE:          ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
