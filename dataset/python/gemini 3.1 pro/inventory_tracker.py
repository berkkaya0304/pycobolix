def main():
    print("=== INVENTORY MANAGEMENT ===")
    print("Initialize a new item tracking...")
    item_id = input("Item ID: ")
    item_desc = input("Item Description: ")
    try:
        unit_price = float(input("Unit Price: "))
    except ValueError:
        unit_price = 0.0
    try:
        qty_on_hand = int(input("Initial Quantity: "))
    except ValueError:
        qty_on_hand = 0

    reorder_level = 20
    action_code = ''

    while action_code != 'Q':
        print("\nAction (A=Add, R=Remove, C=Check, Q=Quit): ")
        action_code = input("").strip().upper()

        if action_code == 'A':
            try:
                trx_qty = int(input("QTY to Add: "))
            except ValueError:
                trx_qty = 0
            qty_on_hand += trx_qty
            print(f"Stock updated. Current QTY: {qty_on_hand:04d}")

        elif action_code == 'R':
            try:
                trx_qty = int(input("QTY to Remove (Sale): "))
            except ValueError:
                trx_qty = 0
            if trx_qty > qty_on_hand:
                print(f"Cannot remove! Only {qty_on_hand:04d} available.")
            else:
                qty_on_hand -= trx_qty
                print(f"Stock shipped. Current QTY: {qty_on_hand:04d}")

        elif action_code == 'C':
            disp_value = qty_on_hand * unit_price
            print("--- ITEM STATUS ---")
            print(f"ID:     {item_id}")
            print(f"Desc:   {item_desc}")
            print(f"Price:  ${unit_price:7.2f}")
            print(f"Stock:  {qty_on_hand:04d}")
            print(f"Total Value: ${disp_value:11.2f}")
            if qty_on_hand <= reorder_level:
                print("*** WARNING: STOCK BELOW REORDER LEVEL ***")
            print("-------------------")

        elif action_code == 'Q':
            break
        else:
            print("Invalid Option.")

    print("Exiting Inventory System.")

if __name__ == "__main__":
    main()
