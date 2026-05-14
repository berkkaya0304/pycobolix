"""
Sunny Acres Farm Stand - Farmers Market
Converted from COBOL (farmers_market.cbl) to Python
"""


def main():
    apple_p_lb = 2.99
    carrot_p_b = 3.50
    honey_p_j = 12.00

    print("--- SUNNY ACRES FARM STAND ---")
    apples_lbs = float(input("Apples (lbs) @ $2.99/lb: "))
    carrots_bunch = int(input("Carrot Bunches @ $3.50 ea: "))
    honey_jars = int(input("Local Honey Jars @ $12.00 ea: "))
    cloth_bag = input("Need a reusable cloth bag ($1.50)? (Y/N): ").strip().upper()

    apples_tot = apples_lbs * apple_p_lb
    carrots_tot = carrots_bunch * carrot_p_b
    honey_tot = honey_jars * honey_p_j
    bag_fee = 1.50 if cloth_bag == "Y" else 0.0

    final_bill = apples_tot + carrots_tot + honey_tot + bag_fee

    print()
    print("========================================")
    print("        FARMERS MARKET RECIEPT          ")
    print("========================================")
    if apples_lbs > 0:
        print(f"Gala Apples ({apples_lbs} lbs): ${apples_tot:>9,.2f}")
    if carrots_bunch > 0:
        print(f"Carrots ({carrots_bunch} bch):     ${carrots_tot:>9,.2f}")
    if honey_jars > 0:
        print(f"Local Honey ({honey_jars} jar):  ${honey_tot:>9,.2f}")
    if cloth_bag == "Y":
        print("Reusable Bag:           $    1.50")
    print("----------------------------------------")
    print(f"TOTAL PRODUCE TOTAL:${final_bill:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
