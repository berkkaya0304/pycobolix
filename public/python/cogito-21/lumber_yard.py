def main():
    print("--- TIMBER WORKS LUMBER YARD ---")
    builder_name = input("Contractor Name: ")
    
    print("Wood (1=Pine $2/bf, 2=Oak $6/bf, 3=Cedar $4/bf): ")
    wood_type = int(input().strip())
    
    print("Quantity (Board Feet): ")
    board_feet = int(input().strip())
    
    print("Delivery to Job Site ($75 flat)? (Y/N): ")
    delivery_req = input().strip().upper()
    
    price_per_bf = 0.0
    wood_name = ""
    
    if wood_type == 1:
        price_per_bf = 2.00
        wood_name = "Pine"
    elif wood_type == 2:
        price_per_bf = 6.00
        wood_name = "Oak"
    elif wood_type == 3:
        price_per_bf = 4.00
        wood_name = "Cedar"
    else:
        price_per_bf = 2.00
        wood_name = "Pine"
        print("Invalid Type. Defaulted to Pine.")
    
    wood_cost = board_feet * price_per_bf
    delivery_fee = 75.00 if delivery_req == 'Y' else 0.0
    total_order = wood_cost + delivery_fee
    
    print("\n===========================================")
    print("            LUMBER INVOICE                 ")
    print("===========================================")
    print(f"Builder: {builder_name}")
    print(f"Lumber:  {board_feet} board feet of {wood_name}")
    print("-------------------------------------------")
    print(f"Price Per BF:     ${price_per_bf:.2f}")
    print(f"Material Cost:    ${wood_cost:,.2f}")
    
    if delivery_req == 'Y':
        print(f"Delivery Freight: ${delivery_fee:,.2f}")
    
    print("-------------------------------------------")
    print(f"GRAND TOTAL:      ${total_order:,.2f}")
    print("===========================================")

if __name__ == "__main__":
    main()
