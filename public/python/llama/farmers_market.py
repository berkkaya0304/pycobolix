# FARMERS-MARKET - Sunny Acres Farm Stand
# Converted from COBOL to Python

def main():
    APPLE_P_LB = 2.99
    CARROT_P_B = 3.50
    HONEY_P_J = 12.00

    print("--- SUNNY ACRES FARM STAND ---")
    apples_lbs = float(input("Apples (lbs) @ $2.99/lb: "))
    carrots_bunch = int(input("Carrot Bunches @ $3.50 ea: "))
    honey_jars = int(input("Local Honey Jars @ $12.00 ea: "))
    cloth_bag = input("Need a reusable cloth bag ($1.50)? (Y/N): ").strip().upper()

    apples_tot = apples_lbs * APPLE_P_LB
    carrots_tot = carrots_bunch * CARROT_P_B
    honey_tot = honey_jars * HONEY_P_J
    bag_fee = 1.50 if cloth_bag == 'Y' else 0.0
    final_bill = apples_tot + carrots_tot + honey_tot + bag_fee

    print("")
    print("========================================")
    print("        FARMERS MARKET RECIEPT          ")
    print("========================================")
    if apples_lbs > 0:
        print(f"Gala Apples ({apples_lbs} lbs): ${apples_tot:,.2f}")
    if carrots_bunch > 0:
        print(f"Carrots ({carrots_bunch} bch):     ${carrots_tot:,.2f}")
    if honey_jars > 0:
        print(f"Local Honey ({honey_jars} jar):  ${honey_tot:,.2f}")
    if cloth_bag == 'Y':
        print("Reusable Bag:           $    1.50")
    print("----------------------------------------")
    print(f"TOTAL PRODUCE TOTAL:${final_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
