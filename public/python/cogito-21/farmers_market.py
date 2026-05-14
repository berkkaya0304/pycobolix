def main():
    print("--- SUNNY ACRES FARM STAND ---")
    
    apples_lbs = float(input("Apples (lbs) @ $2.99/lb: "))
    carrots_bunch = int(input("Carrot Bunches @ $3.50 ea: "))
    honey_jars = int(input("Local Honey Jars @ $12.00 ea: "))
    needs_bag = input("Need a reusable cloth bag ($1.50)? (Y/N): ").strip().upper() == 'Y'
    
    apple_price = 2.99
    carrot_price = 3.50
    honey_price = 12.00
    
    apples_total = apples_lbs * apple_price
    carrots_total = carrots_bunch * carrot_price
    honey_total = honey_jars * honey_price
    bag_fee = 1.50 if needs_bag else 0.0
    
    final_bill = apples_total + carrots_total + honey_total + bag_fee
    
    print("\n" + "=" * 40)
    print("        FARMERS MARKET RECEIPT          ")
    print("=" * 40)
    
    if apples_lbs > 0:
        print(f"Gala Apples ({apples_lbs} lbs): ${apples_total:7.2f}")
    if carrots_bunch > 0:
        print(f"Carrots ({carrots_bunch} bch):     ${carrots_total:7.2f}")
    if honey_jars > 0:
        print(f"Local Honey ({honey_jars} jar):  ${honey_total:7.2f}")
    if needs_bag:
        print("Reusable Bag:           $    1.50")
    
    print("-" * 40)
    print(f"TOTAL PRODUCE TOTAL: ${final_bill:7.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
