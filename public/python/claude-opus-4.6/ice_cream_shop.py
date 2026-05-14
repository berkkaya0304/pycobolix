"""
Sweet Scoops Ice Cream Shop
Converted from COBOL (ice_cream_shop.cbl) to Python
"""


def main():
    scoop_prc = 2.50
    waffle_prc = 1.50
    topping_prc = 0.75

    print("--- SWEET SCOOPS ICE CREAM ---")
    cust_name = input("Name for Order: ")
    scoops = int(input("Number of Scoops ($2.50 ea): "))
    cone_bowl = input("Vessel (W=Waffle Cone $1.50, C=Cup $0): ").strip().upper()
    topping_qty = int(input("Number of Toppings ($0.75 ea): "))

    ice_cream_fee = scoops * scoop_prc
    cone_fee = waffle_prc if cone_bowl == "W" else 0.0
    top_fee = topping_qty * topping_prc
    total_order = ice_cream_fee + cone_fee + top_fee

    print()
    print("========================================")
    print("             ORDER TICKET               ")
    print("========================================")
    print(f"Name: {cust_name}")
    print("----------------------------------------")
    print(f"Ice Cream ({scoops} scoops): ${ice_cream_fee:>9,.2f}")
    if cone_bowl == "W":
        print(f"Waffle Cone:           ${cone_fee:>9,.2f}")
    if topping_qty > 0:
        print(f"Toppings ({topping_qty}):          ${top_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL DUE:             ${total_order:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
