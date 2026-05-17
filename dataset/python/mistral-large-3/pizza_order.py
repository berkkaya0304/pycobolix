def pizza_order():
    print("--- MARIO'S PIZZERIA ---")
    cust_name = input("Customer Name: ").strip()
    pizza_size = input("Size (S=Small $10, M=Medium $14, L=Large $18): ").strip().upper()
    crust_type = input("Crust (1=Thin, 2=Thick, 3=Stuffed +$3): ").strip()
    topping_qty = int(input("Number of Extra Toppings ($1.50 ea): ").strip())

    base_price = 0.0
    crust_fee = 0.0
    topping_fee = 0.0
    sub_total = 0.0
    tax_amt = 0.0
    grand_total = 0.0

    if pizza_size == 'S':
        base_price = 10.00
    elif pizza_size == 'M':
        base_price = 14.00
    elif pizza_size == 'L':
        base_price = 18.00
    else:
        base_price = 10.00
        print("Invalid Size, Default to Small.")

    if crust_type == '3':
        crust_fee = 3.00

    topping_fee = topping_qty * 1.50
    sub_total = base_price + crust_fee + topping_fee
    tax_amt = sub_total * 0.08
    grand_total = sub_total + tax_amt

    print("\n========================================")
    print("          PIZZA ORDER RECEIPT           ")
    print("========================================")
    print(f"Order for: {cust_name}")
    print("----------------------------------------")
    print(f"Base Pizza:       ${base_price:.2f}")
    if crust_fee > 0:
        print(f"Stuffed Crust:    ${crust_fee:.2f}")
    if topping_fee > 0:
        print(f"Toppings ({topping_qty}):    ${topping_fee:.2f}")
    print("----------------------------------------")
    print(f"Subtotal:         ${sub_total:.2f}")
    print(f"Tax (8%):         ${tax_amt:.2f}")
    print("========================================")
    print(f"TOTAL AMOUNT DUE: ${grand_total:.2f}")
    print("========================================")

if __name__ == "__main__":
    pizza_order()
