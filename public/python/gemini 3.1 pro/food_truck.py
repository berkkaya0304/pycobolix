def main():
    print("--- EL TACO LOCO TRUCK ---")
    order_name = input("Order Name: ")
    try:
        taco_qty = int(input("Street Tacos ($2.50 ea): "))
    except ValueError:
        taco_qty = 0
    try:
        burrito_qty = int(input("Super Burritos ($8.00 ea): "))
    except ValueError:
        burrito_qty = 0
    try:
        drink_qty = int(input("Sodas / Aguas Frescas ($2.00 ea): "))
    except ValueError:
        drink_qty = 0
    add_guac = input("Add side of Guac & Chips ($4.00)? (Y/N): ").strip().upper() == 'Y'

    taco_cost = taco_qty * 2.50
    burrito_cost = burrito_qty * 8.00
    drink_cost = drink_qty * 2.00
    
    guac_cost = 4.00 if add_guac else 0.0

    total_cost = taco_cost + burrito_cost + drink_cost + guac_cost

    print("\n========================================")
    print("          EL TACO LOCO RECEIPT          ")
    print("========================================")
    print(f"Name: {order_name}")
    print("----------------------------------------")
    
    if taco_qty > 0:
        print(f"{taco_qty}x Tacos:            ${taco_cost:6.2f}")
    if burrito_qty > 0:
        print(f"{burrito_qty}x Burritos:         ${burrito_cost:6.2f}")
    if drink_qty > 0:
        print(f"{drink_qty}x Drinks:           ${drink_cost:6.2f}")
    if add_guac:
        print(f"   Side of Guac:        ${guac_cost:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL ORDER:            ${total_cost:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
