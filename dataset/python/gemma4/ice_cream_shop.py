def main():
    # Constants
    SCOOP_PRC = 2.50
    WAFFLE_PRC = 1.50
    TOPPING_PRC = 0.75

    print("--- SWEET SCOOPS ICE CREAM ---")
    
    cust_name = input("Name for Order: ")
    
    try:
        scoops = int(input("Number of Scoops ($2.50 ea): "))
        cone_bowl = input("Vessel (W=Waffle Cone $1.50, C=Cup $0): ").upper()
        topping_qty = int(input("Number of Toppings ($0.75 ea): "))
    except ValueError:
        print("Invalid input. Please enter numbers for scoops and toppings.")
        return

    # Calculations
    ice_cream_fee = scoops * SCOOP_PRC
    cone_fee = WAFFLE_PRC if cone_bowl == 'W' else 0.0
    top_fee = topping_qty * TOPPING_PRC
    total_order = ice_cream_fee + cone_fee + top_fee

    # Output
    print("\n========================================")
    print("             ORDER TICKET               ")
    print("========================================")
    print(f"Name: {cust_name}")
    print("----------------------------------------")
    print(f"Ice Cream ({scoops} scoops): ${ice_cream_fee:6.2f}")
    
    if cone_bowl == 'W':
        print(f"Waffle Cone:           ${cone_fee:6.2f}")
    
    if topping_qty > 0:
        print(f"Toppings ({topping_qty}):          ${top_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL DUE:             ${total_order:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
