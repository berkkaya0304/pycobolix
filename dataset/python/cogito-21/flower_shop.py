def flower_shop():
    print("--- BLOSSOMS FLORIST ---")
    recipient_name = input("Recipient Name: ")
    
    print("Bouquet Size (1=Small $30, 2=Med $50, 3=Lrg $80): ")
    bouquet_size = int(input().strip())
    print("Vase (1=Wrapped, 2=Glass $15, 3=Crystal $40): ")
    vase_type = int(input().strip())
    print("Delivery Zone (1=Local $10, 2=Regional $25): ")
    delivery_zone = int(input().strip())
    
    if bouquet_size == 1:
        flower_cost = 30.00
    elif bouquet_size == 2:
        flower_cost = 50.00
    elif bouquet_size == 3:
        flower_cost = 80.00
    else:
        flower_cost = 30.00
    
    if vase_type == 1:
        vase_cost = 0.00
    elif vase_type == 2:
        vase_cost = 15.00
    elif vase_type == 3:
        vase_cost = 40.00
    else:
        vase_cost = 0.00
    
    if delivery_zone == 1:
        delivery_fee = 10.00
    elif delivery_zone == 2:
        delivery_fee = 25.00
    else:
        delivery_fee = 10.00
    
    total_bill = flower_cost + vase_cost + delivery_fee
    
    print("\n" + "=" * 40)
    print("          FLORIST ORDER RECEIPT         ")
    print("=" * 40)
    print(f"Send To: {recipient_name}")
    print("-" * 40)
    print(f"Arrangement:        ${flower_cost:.2f}")
    
    if vase_cost > 0:
        print(f"Vase/Container:     ${vase_cost:.2f}")
    
    print(f"Delivery Fee:       ${delivery_fee:.2f}")
    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:   ${total_bill:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    flower_shop()
