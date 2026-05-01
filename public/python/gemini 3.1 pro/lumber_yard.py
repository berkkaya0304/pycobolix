def main():
    print("--- TIMBER WORKS LUMBER YARD ---")
    builder_name = input("Contractor Name: ")
    wood_type = input("Wood (1=Pine $2/bf, 2=Oak $6/bf, 3=Cedar $4/bf): ").strip()
    try:
        board_feet = int(input("Quantity (Board Feet): "))
    except ValueError:
        board_feet = 0
    delivery_req = input("Delivery to Job Site ($75 flat)? (Y/N): ").strip().upper() == 'Y'

    if wood_type == '1':
        price_per_bf = 2.00
    elif wood_type == '2':
        price_per_bf = 6.00
    elif wood_type == '3':
        price_per_bf = 4.00
    else:
        price_per_bf = 2.00
        print("Invalid Type. Defaulted to Pine.")

    wood_cost = board_feet * price_per_bf
    deliv_fee = 75.00 if delivery_req else 0.0

    total_order = wood_cost + deliv_fee

    print("\n===========================================")
    print("            LUMBER INVOICE                 ")
    print("===========================================")
    print(f"Builder: {builder_name}")
    print(f"Lumber:  {board_feet:04d} board feet")
    print("-------------------------------------------")
    print(f"Price Per BF:     ${price_per_bf:9.2f}")
    print(f"Material Cost:    ${wood_cost:9.2f}")
    
    if delivery_req:
        print(f"Delivery Freight: ${deliv_fee:9.2f}")
        
    print("-------------------------------------------")
    print(f"GRAND TOTAL:      ${total_order:9.2f}")
    print("===========================================")

if __name__ == "__main__":
    main()
