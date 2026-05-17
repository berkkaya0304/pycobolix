def main():
    print("--- SNACK-O-MATIC VENDING ---")
    print("A1. Soda ($1.50)")
    print("A2. Chips ($1.25)")
    print("B1. Candy ($2.00)")
    print("B2. Water ($1.00)")
    item_choice = input("Enter Selection: ").strip().upper()

    if item_choice == "A1":
        item_price = 1.50
        item_name = "Soda"
    elif item_choice == "A2":
        item_price = 1.25
        item_name = "Chips"
    elif item_choice == "B1":
        item_price = 2.00
        item_name = "Candy"
    elif item_choice == "B2":
        item_price = 1.00
        item_name = "Water"
    else:
        print("Invalid Selection.")
        return

    print(f"Selected: {item_name}  Cost: ${item_price:6.2f}")
    
    amount_inserted = 0.0
    while amount_inserted < item_price:
        try:
            new_money = float(input("Insert Money ($ format): "))
        except ValueError:
            new_money = 0.0
        amount_inserted += new_money
        print(f"Current Credit: ${amount_inserted:6.2f}")

    change_due = amount_inserted - item_price
    print("-----------------------------------")
    print(f"Vending {item_name}...  *CLUNK*")
    
    if change_due > 0:
        print(f"Refunding Change: ${change_due:6.2f}")
    else:
        print("Exact change inserted.")
        
    print("Thank you!")

if __name__ == "__main__":
    main()
