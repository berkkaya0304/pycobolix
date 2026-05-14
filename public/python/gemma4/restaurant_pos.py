import sys

def format_money(amount):
    return f"${amount:,.2f}"

def main():
    print("=== STARLIGHT RESTAURANT POS ===")
    
    try:
        table_num = input("Table Number: ")
        guest_count = int(input("Number of Guests: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    menu_items = []
    food_tot = 0.0
    
    for i in range(1, 6):
        try:
            name = input("Enter Item Name: ")
            qty = int(input("Enter Quantity: "))
            price = float(input("Enter Price per Item: "))
            
            subtot = qty * price
            food_tot += subtot
            
            menu_items.append({
                'name': name,
                'qty': qty,
                'subtot': subtot
            })
            
            if i < 5:
                more = input("Add another item? (Y/N): ").strip().upper()
                if more == 'N':
                    break
            else:
                print("Max items reached.")
                break
        except ValueError:
            print("Invalid input. Item skipped.")
            continue

    # Calculate Tax and Tip
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

    # Print Bill
    print("\n===========================================")
    print("              GUEST CHECK                  ")
    print(f" TABLE: {table_num:<10}             GUESTS: {guest_count}")
    print("===========================================")
    
    for item in menu_items:
        if item['qty'] > 0:
            print(f"{item['name']:<15}   {item['qty']:<3}   {format_money(item['subtot'])}")
            
    print("-------------------------------------------")
    print(f"SUBTOTAL:         {format_money(food_tot)}")
    print(f"TAX:              {format_money(tax_amt)}")
    print(f"GRATUITY:         {format_money(tip_amt)}")
    print("===========================================")
    print(f"TOTAL DUE:        {format_money(grand_tot)}")
    print("      Thank You For Dining With Us!        ")
    print("===========================================")

if __name__ == "__main__":
    main()
