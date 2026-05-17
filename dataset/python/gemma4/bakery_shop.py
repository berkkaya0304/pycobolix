def main():
    # Item Prices
    CAKE_PRC = 25.00
    BREAD_PRC = 4.50
    PASTRY_PRC = 3.00

    print("--- SUNRISE BAKERY POS ---")
    
    # Input
    cust_name = input("Customer Name: ")
    try:
        cake_qty = int(input("Whole Cakes ($25.00 ea): ") or 0)
        bread_qty = int(input("Loaves of Bread ($4.50 ea): ") or 0)
        pastry_qty = int(input("Assorted Pastries ($3.00 ea): ") or 0)
    except ValueError:
        print("Invalid quantity entered. Defaulting to 0.")
        cake_qty = bread_qty = pastry_qty = 0

    # Process Order
    cake_tot = cake_qty * CAKE_PRC
    bread_tot = bread_qty * BREAD_PRC
    pastry_tot = pastry_qty * PASTRY_PRC

    sub_total = cake_tot + bread_tot + pastry_tot
    
    discount = 0.0
    if sub_total >= 50.00:
        discount = sub_total * 0.10

    final_tot = sub_total - discount

    # Print Bill
    print("\n=========================================")
    print("          BAKERY ORDER RECEIPT           ")
    print("=========================================")
    print(f"Customer: {cust_name}")
    print("-----------------------------------------")
    
    if cake_qty > 0:
        print(f"{cake_qty} x Cakes:         ${cake_tot:,.2f}")
    if bread_qty > 0:
        print(f"{bread_qty} x Bread Loaves:  ${bread_tot:,.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty} x Pastries:      ${pastry_tot:,.2f}")
        
    print("-----------------------------------------")
    print(f"Subtotal:         ${sub_total:,.2f}")
    
    if discount > 0:
        print(f"Bulk Discount:   -${discount:,.2f}")
        
    print("-----------------------------------------")
    print(f"TOTAL DUE:        ${final_tot:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
