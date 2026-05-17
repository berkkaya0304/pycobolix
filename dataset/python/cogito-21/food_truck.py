def main():
    print("--- EL TACO LOCO TRUCK ---")
    order_name = input("Order Name: ")
    
    try:
        taco_qty = int(input("Street Tacos ($2.50 ea): "))
        burrito_qty = int(input("Super Burritos ($8.00 ea): "))
        drink_qty = int(input("Sodas / Aguas Frescas ($2.00 ea): "))
        add_guac = input("Add side of Guac & Chips ($4.00)? (Y/N): ").strip().upper()
        
        taco_cost = taco_qty * 2.50
        burrito_cost = burrito_qty * 8.00
        drink_cost = drink_qty * 2.00
        guac_cost = 4.00 if add_guac == 'Y' else 0.00
        total_cost = taco_cost + burrito_cost + drink_cost + guac_cost
        
        print("\n" + "=" * 40)
        print("          EL TACO LOCO RECEIPT          ")
        print("=" * 40)
        print(f"Name: {order_name}")
        print("-" * 40)
        
        if taco_qty > 0:
            print(f"{taco_qty}x Tacos:            ${taco_cost:6.2f}")
        if burrito_qty > 0:
            print(f"{burrito_qty}x Burritos:         ${burrito_cost:6.2f}")
        if drink_qty > 0:
            print(f"{drink_qty}x Drinks:           ${drink_cost:6.2f}")
        if add_guac == 'Y':
            print(f"   Side of Guac:        ${guac_cost:6.2f}")
            
        print("-" * 40)
        print(f"TOTAL ORDER:            ${total_cost:6.2f}")
        print("=" * 40)
        
    except ValueError:
        print("Error: Please enter valid numeric quantities.")

if __name__ == "__main__":
    main()
