def main():
    print("--- BLOSSOMS FLORIST ---")
    
    recipient_name = input("Recipient Name: ")
    
    try:
        bouquet_size = int(input("Bouquet Size (1=Small $30, 2=Med $50, 3=Lrg $80): "))
    except ValueError:
        bouquet_size = 0

    try:
        vase_type = int(input("Vase (1=Wrapped, 2=Glass $15, 3=Crystal $40): "))
    except ValueError:
        vase_type = 0

    try:
        delivery_zone = int(input("Delivery Zone (1=Local $10, 2=Regional $25): "))
    except ValueError:
        delivery_zone = 0

    # Determine Flower Cost
    if bouquet_size == 1:
        flower_cost = 30.00
    elif bouquet_size == 2:
        flower_cost = 50.00
    elif bouquet_size == 3:
        flower_cost = 80.00
    else:
        flower_cost = 30.00

    # Determine Vase Cost
    if vase_type == 1:
        vase_cost = 0.00
    elif vase_type == 2:
        vase_cost = 15.00
    elif vase_type == 3:
        vase_cost = 40.00
    else:
        vase_cost = 0.00

    # Determine Delivery Fee
    if delivery_zone == 1:
        deliv_fee = 10.00
    elif delivery_zone == 2:
        deliv_fee = 25.00
    else:
        deliv_fee = 10.00

    total_bill = flower_cost + vase_cost + deliv_fee

    print("\n")
    print("========================================")
    print("          FLORIST ORDER RECEIPT         ")
    print("========================================")
    print(f"Send To: {recipient_name}")
    print("----------------------------------------")
    print(f"Arrangement:        ${flower_cost:,.2f}")
    
    if vase_cost > 0:
        print(f"Vase/Container:     ${vase_cost:,.2f}")
        
    print(f"Delivery Fee:       ${deliv_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:   ${total_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
