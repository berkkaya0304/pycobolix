import sys
from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    items = {
        "A1": {"name": "Soda", "price": Decimal("1.50")},
        "A2": {"name": "Chips", "price": Decimal("1.25")},
        "B1": {"name": "Candy", "price": Decimal("2.00")},
        "B2": {"name": "Water", "price": Decimal("1.00")},
    }

    print("--- SNACK-O-MATIC VENDING ---")
    print("A1. Soda ($1.50)")
    print("A2. Chips ($1.25)")
    print("B1. Candy ($2.00)")
    print("B2. Water ($1.00)")
    
    item_choice = input("Enter Selection: ").strip().upper()

    if item_choice not in items:
        print("Invalid Selection.")
        sys.exit()

    selected_item = items[item_choice]
    item_name = selected_item["name"]
    item_price = selected_item["price"]

    print(f"Selected: {item_name}  Cost: {format_currency(item_price)}")

    amount_inserted = Decimal("0.00")
    while amount_inserted < item_price:
        try:
            new_money_str = input("Insert Money ($ format): ")
            new_money = Decimal(new_money_str)
            amount_inserted += new_money
            print(f"Current Credit: {format_currency(amount_inserted)}")
        except Exception:
            print("Invalid amount entered.")

    change_due = amount_inserted - item_price
    print("-----------------------------------")
    print(f"Vending {item_name}...  *CLUNK*")

    if change_due > 0:
        print(f"Refunding Change: {format_currency(change_due)}")
    else:
        print("Exact change inserted.")

    print("Thank you!")

if __name__ == "__main__":
    main()
