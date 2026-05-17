def vending_machine():
    items = {
        "A1": {"name": "Soda", "price": 1.50},
        "A2": {"name": "Chips", "price": 1.25},
        "B1": {"name": "Candy", "price": 2.00},
        "B2": {"name": "Water", "price": 1.00}
    }

    print("--- SNACK-O-MATIC VENDING ---")
    print("A1. Soda ($1.50)")
    print("A2. Chips ($1.25)")
    print("B1. Candy ($2.00)")
    print("B2. Water ($1.00)")
    item_choice = input("Enter Selection: ").strip().upper()

    if item_choice not in items:
        print("Invalid Selection.")
        return

    item = items[item_choice]
    item_name = item["name"]
    item_price = item["price"]

    print(f"Selected: {item_name}  Cost: ${item_price:.2f}")

    amount_inserted = 0.0
    while amount_inserted < item_price:
        try:
            new_money = float(input("Insert Money ($ format): "))
            if new_money <= 0:
                print("Please insert a positive amount.")
                continue
            amount_inserted += new_money
            print(f"Current Credit: ${amount_inserted:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    change_due = amount_inserted - item_price
    print("-----------------------------------")
    print(f"Vending {item_name}...  *CLUNK*")
    if change_due > 0:
        print(f"Refunding Change: ${change_due:.2f}")
    else:
        print("Exact change inserted.")
    print("Thank you!")

if __name__ == "__main__":
    vending_machine()
