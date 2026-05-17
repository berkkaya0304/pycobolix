"""
Starlight Restaurant POS
Converted from COBOL (restaurant_pos.cbl) to Python
"""


def main():
    print("=== STARLIGHT RESTAURANT POS ===")
    table_num = input("Table Number: ")
    guest_count = int(input("Number of Guests: "))

    items = []
    food_tot = 0.0
    more_items = "Y"
    i = 0

    while more_items.upper() == "Y" and i < 5:
        item_name = input("Enter Item Name: ")
        item_qty = int(input("Enter Quantity: "))
        item_price = float(input("Enter Price per Item: "))
        item_subtot = item_qty * item_price
        food_tot += item_subtot
        items.append((item_name, item_qty, item_price, item_subtot))
        i += 1
        if i < 5:
            more_items = input("Add another item? (Y/N): ").strip().upper()
        else:
            print("Max items reached.")

    tax_amt = food_tot * 0.0825
    if guest_count >= 6:
        tip_amt = food_tot * 0.18
        print("*** Automatic Gratuity Applied (Party >= 6) ***")
    else:
        tip_amt = float(input("Enter Tip Amount ($): "))

    grand_tot = food_tot + tax_amt + tip_amt

    print()
    print("===========================================")
    print("              GUEST CHECK                  ")
    print(f" TABLE: {table_num}             GUESTS: {guest_count}")
    print("===========================================")
    for name, qty, price, subtot in items:
        print(f"{name:<16}{qty:>3}   ${subtot:>9,.2f}")
    print("-------------------------------------------")
    print(f"SUBTOTAL:         ${food_tot:>9,.2f}")
    print(f"TAX:              ${tax_amt:>9,.2f}")
    print(f"GRATUITY:         ${tip_amt:>9,.2f}")
    print("===========================================")
    print(f"TOTAL DUE:        ${grand_tot:>9,.2f}")
    print("      Thank You For Dining With Us!        ")
    print("===========================================")


if __name__ == "__main__":
    main()
