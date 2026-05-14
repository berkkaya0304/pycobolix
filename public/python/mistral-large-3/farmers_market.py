def farmers_market():
    # Initialize market basket
    apples_lbs = 0.0
    carrots_bunch = 0
    honey_jars = 0
    needs_bag = False

    # Prices
    apple_price_per_lb = 2.99
    carrot_price_per_bunch = 3.50
    honey_price_per_jar = 12.00
    bag_fee = 0.0

    # Display welcome message
    print("--- SUNNY ACRES FARM STAND ---")

    # Get user input
    apples_lbs = float(input("Apples (lbs) @ $2.99/lb: "))
    carrots_bunch = int(input("Carrot Bunches @ $3.50 ea: "))
    honey_jars = int(input("Local Honey Jars @ $12.00 ea: "))
    bag_response = input("Need a reusable cloth bag ($1.50)? (Y/N): ").strip().upper()
    needs_bag = bag_response == 'Y'

    # Calculate totals
    apples_total = apples_lbs * apple_price_per_lb
    carrots_total = carrots_bunch * carrot_price_per_bunch
    honey_total = honey_jars * honey_price_per_jar

    if needs_bag:
        bag_fee = 1.50

    final_bill = apples_total + carrots_total + honey_total + bag_fee

    # Display receipt
    print("\n========================================")
    print("        FARMERS MARKET RECEIPT          ")
    print("========================================")

    if apples_lbs > 0:
        print(f"Gala Apples ({apples_lbs:.1f} lbs): ${apples_total:>8.2f}")

    if carrots_bunch > 0:
        print(f"Carrots ({carrots_bunch} bch):     ${carrots_total:>8.2f}")

    if honey_jars > 0:
        print(f"Local Honey ({honey_jars} jar):  ${honey_total:>8.2f}")

    if needs_bag:
        print("Reusable Bag:           $    1.50")

    print("----------------------------------------")
    print(f"TOTAL PRODUCE TOTAL:    ${final_bill:>8.2f}")
    print("========================================")

if __name__ == "__main__":
    farmers_market()
