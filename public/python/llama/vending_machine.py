# VENDING-MACHINE - Snack-O-Matic Vending
# Converted from COBOL to Python

def main():
    print("--- SNACK-O-MATIC VENDING ---")
    print("A1. Soda ($1.50)")
    print("A2. Chips ($1.25)")
    print("B1. Candy ($2.00)")
    print("B2. Water ($1.00)")
    item_choice = input("Enter Selection: ").strip().upper()

    prices = {"A1": (1.50, "Soda"), "A2": (1.25, "Chips"), "B1": (2.00, "Candy"), "B2": (1.00, "Water")}
    if item_choice not in prices:
        print("Invalid Selection.")
        return

    item_price, item_name = prices[item_choice]
    print(f"Selected: {item_name}  Cost: ${item_price:,.2f}")

    amount_inserted = 0.0
    while amount_inserted < item_price:
        new_money = float(input("Insert Money ($ format): "))
        amount_inserted += new_money
        print(f"Current Credit: ${amount_inserted:,.2f}")

    change_due = amount_inserted - item_price
    print("-----------------------------------")
    print(f"Vending {item_name}...  *CLUNK*")
    if change_due > 0:
        print(f"Refunding Change: ${change_due:,.2f}")
    else:
        print("Exact change inserted.")
    print("Thank you!")

if __name__ == "__main__":
    main()
