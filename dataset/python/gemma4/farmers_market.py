def main():
    # Prices
    APPLE_P_LB = 2.99
    CARROT_P_B = 3.50
    HONEY_P_J = 12.00
    BAG_FEE_AMOUNT = 1.50

    print("--- SUNNY ACRES FARM STAND ---")
    
    try:
        apples_lbs = float(input("Apples (lbs) @ $2.99/lb: "))
        carrots_bunch = int(input("Carrot Bunches @ $3.50 ea: "))
        honey_jars = int(input("Local Honey Jars @ $12.00 ea: "))
        cloth_bag = input("Need a reusable cloth bag ($1.50)? (Y/N): ").strip().upper()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculations
    apples_tot = apples_lbs * APPLE_P_LB
    carrots_tot = carrots_bunch * CARROT_P_B
    honey_tot = honey_jars * HONEY_P_J
    
    bag_fee = BAG_FEE_AMOUNT if cloth_bag == 'Y' else 0.0
    final_bill = apples_tot + carrots_tot + honey_tot + bag_fee

    # Receipt Output
    print("\n========================================")
    print("        FARMERS MARKET RECIEPT          ")
    print("========================================")
    
    if apples_lbs > 0:
        print(f"Gala Apples ({apples_lbs} lbs): ${apples_tot:,.2f}")
    
    if carrots_bunch > 0:
        print(f"Carrots ({carrots_bunch} bch):     ${carrots_tot:,.2f}")
        
    if honey_jars > 0:
        print(f"Local Honey ({honey_jars} jar):  ${honey_tot:,.2f}")
        
    if cloth_bag == 'Y':
        print(f"Reusable Bag:           ${bag_fee:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL PRODUCE TOTAL: ${final_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
