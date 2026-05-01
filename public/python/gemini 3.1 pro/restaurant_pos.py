def main():
    print("=== STARLIGHT RESTAURANT POS ===")
    try:
        table_num = int(input("Table Number: "))
    except ValueError:
        table_num = 0
    try:
        guest_count = int(input("Number of Guests: "))
    except ValueError:
        guest_count = 0

    item_names = []
    item_qtys = []
    item_subtots = []
    food_tot = 0.0
    more_items = 'Y'

    for i in range(5):
        item_name = input("Enter Item Name: ")
        try:
            item_qty = int(input("Enter Quantity: "))
        except ValueError:
            item_qty = 0
        try:
            item_price = float(input("Enter Price per Item: "))
        except ValueError:
            item_price = 0.0
            
        item_subtot = item_qty * item_price
        food_tot += item_subtot
        
        item_names.append(item_name)
        item_qtys.append(item_qty)
        item_subtots.append(item_subtot)
        
        if i < 4:
            more_items = input("Add another item? (Y/N): ").strip().upper()
            if more_items != 'Y':
                break
        else:
            print("Max items reached.")

    tax_amt = food_tot * 0.0825
    
    if guest_count >= 6:
        tip_amt = food_tot * 0.18
        print("*** Automatic Gratuity Applied (Party >= 6) ***")
    else:
        try:
            tip_amt = float(input("Enter Tip Amount ($): "))
        except ValueError:
            tip_amt = 0.0

    grand_tot = food_tot + tax_amt + tip_amt

    print("\n===========================================")
    print("              GUEST CHECK                  ")
    print(f" TABLE: {table_num:02d}             GUESTS: {guest_count:02d}")
    print("===========================================")
    
    for i in range(len(item_names)):
        if item_qtys[i] > 0:
            name = item_names[i].ljust(15)[:15]
            qty = f"{item_qtys[i]:02d}".ljust(5)
            subtot = f"${item_subtots[i]:8.2f}"
            print(f"{name}   {qty}   {subtot}")
            
    print("-------------------------------------------")
    print(f"SUBTOTAL:         ${food_tot:8.2f}")
    print(f"TAX:              ${tax_amt:8.2f}")
    print(f"GRATUITY:         ${tip_amt:8.2f}")
    print("===========================================")
    print(f"TOTAL DUE:        ${grand_tot:8.2f}")
    print("      Thank You For Dining With Us!        ")
    print("===========================================")

if __name__ == "__main__":
    main()
