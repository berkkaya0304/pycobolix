def main():
    print("--- SWEET SCOOPS ICE CREAM ---")
    cust_name = input("Name for Order: ").strip()
    scoops = int(input("Number of Scoops ($2.50 ea): "))
    vessel = input("Vessel (W=Waffle Cone $1.50, C=Cup $0): ").strip().upper()
    topping_qty = int(input("Number of Toppings ($0.75 ea): "))

    scoop_price = 2.50
    waffle_price = 1.50
    topping_price = 0.75

    ice_cream_fee = scoops * scoop_price
    cone_fee = waffle_price if vessel == 'W' else 0.0
    top_fee = topping_qty * topping_price
    total_order = ice_cream_fee + cone_fee + top_fee

    print("")
    print("=" * 40)
    print("             ORDER TICKET               ")
    print("=" * 40)
    print(f"Name: {cust_name}")
    print("-" * 40)
    print(f"Ice Cream ({scoops} scoops):    ${ice_cream_fee:.2f}")

    if vessel == 'W':
        print(f"Waffle Cone:           ${cone_fee:.2f}")

    if topping_qty > 0:
        print(f"Toppings ({topping_qty}):          ${top_fee:.2f}")

    print("-" * 40)
    print(f"TOTAL DUE:             ${total_order:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
