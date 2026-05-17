"""
Mario's Pizzeria - Pizza Order
Converted from COBOL (pizza_order.cbl) to Python
"""


def main():
    print("--- MARIO'S PIZZERIA ---")
    cust_name = input("Customer Name: ")
    pizza_size = input("Size (S=Small $10, M=Medium $14, L=Large $18): ").strip().upper()
    crust_type = int(input("Crust (1=Thin, 2=Thick, 3=Stuffed +$3): "))
    topping_qty = int(input("Number of Extra Toppings ($1.50 ea): "))

    if pizza_size == "S":
        base_price = 10.00
    elif pizza_size == "M":
        base_price = 14.00
    elif pizza_size == "L":
        base_price = 18.00
    else:
        base_price = 10.00
        print("Invalid Size, Default to Small.")

    crust_fee = 3.00 if crust_type == 3 else 0.0
    topping_fee = topping_qty * 1.50
    sub_total = base_price + crust_fee + topping_fee
    tax_amt = sub_total * 0.08
    grand_total = sub_total + tax_amt

    print()
    print("========================================")
    print("          PIZZA ORDER RECEIPT           ")
    print("========================================")
    print(f"Order for: {cust_name}")
    print("----------------------------------------")
    print(f"Base Pizza:       ${base_price:>9,.2f}")
    if crust_fee > 0:
        print(f"Stuffed Crust:    ${crust_fee:>9,.2f}")
    if topping_fee > 0:
        print(f"Toppings ({topping_qty}):    ${topping_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:         ${sub_total:>9,.2f}")
    print(f"Tax (8%):         ${tax_amt:>9,.2f}")
    print("========================================")
    print(f"TOTAL AMOUNT DUE: ${grand_total:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
