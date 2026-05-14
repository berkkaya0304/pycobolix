def restaurant_pos():
    print("=== STARLIGHT RESTAURANT POS ===")

    table_num = int(input("Table Number: "))
    guest_count = int(input("Number of Guests: "))

    menu_items = []
    food_tot = 0.0
    more_items = 'Y'

    for i in range(5):
        if more_items.upper() != 'Y':
            break

        print(f"Enter Item Name: ")
        item_name = input().strip()
        item_qty = int(input("Enter Quantity: "))
        item_price = float(input("Enter Price per Item: "))

        item_subtot = item_qty * item_price
        food_tot += item_subtot

        menu_items.append({
            'name': item_name,
            'qty': item_qty,
            'price': item_price,
            'subtot': item_subtot
        })

        if i < 4:
            more_items = input("Add another item? (Y/N): ").upper()
        else:
            print("Max items reached.")
            more_items = 'N'

    tax_amt, tip_amt, grand_tot = calculate_tax_tip(food_tot, guest_count)
    print_bill(table_num, guest_count, menu_items, food_tot, tax_amt, tip_amt, grand_tot)

def calculate_tax_tip(food_tot, guest_count):
    tax_amt = food_tot * 0.0825

    if guest_count >= 6:
        tip_amt = food_tot * 0.18
        print("*** Automatic Gratuity Applied (Party >= 6) ***")
    else:
        tip_amt = float(input("Enter Tip Amount ($): "))

    grand_tot = food_tot + tax_amt + tip_amt
    return tax_amt, tip_amt, grand_tot

def format_currency(amount):
    return f"${amount:,.2f}"

def print_bill(table_num, guest_count, menu_items, food_tot, tax_amt, tip_amt, grand_tot):
    print("\n===========================================")
    print("              GUEST CHECK                  ")
    print(f" TABLE: {table_num}             GUESTS: {guest_count}")
    print("===========================================")

    for item in menu_items:
        if item['qty'] > 0:
            print(f"{item['name']:<15}   {item['qty']}   {format_currency(item['subtot'])}")

    print("-------------------------------------------")
    print(f"SUBTOTAL:         {format_currency(food_tot)}")
    print(f"TAX:              {format_currency(tax_amt)}")
    print(f"GRATUITY:         {format_currency(tip_amt)}")
    print("===========================================")
    print(f"TOTAL DUE:        {format_currency(grand_tot)}")
    print("      Thank You For Dining With Us!        ")
    print("===========================================")

if __name__ == "__main__":
    restaurant_pos()
