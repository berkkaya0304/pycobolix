# INVENTORY-TRACKER - Inventory Management System
# Converted from COBOL to Python

def main():
    REORDER_LEVEL = 20

    print("=== INVENTORY MANAGEMENT ===")
    print("Initialize a new item tracking...")
    item_id = input("Item ID: ")
    item_desc = input("Item Description: ")
    unit_price = float(input("Unit Price: "))
    qty_on_hand = int(input("Initial Quantity: "))

    while True:
        print("")
        action_code = input("Action (A=Add, R=Remove, C=Check, Q=Quit): ").strip().upper()

        if action_code == 'A':
            trx_qty = int(input("QTY to Add: "))
            qty_on_hand += trx_qty
            print(f"Stock updated. Current QTY: {qty_on_hand}")
        elif action_code == 'R':
            trx_qty = int(input("QTY to Remove (Sale): "))
            if trx_qty > qty_on_hand:
                print(f"Cannot remove! Only {qty_on_hand} available.")
            else:
                qty_on_hand -= trx_qty
                print(f"Stock shipped. Current QTY: {qty_on_hand}")
        elif action_code == 'C':
            total_value = qty_on_hand * unit_price
            print("--- ITEM STATUS ---")
            print(f"ID:     {item_id}")
            print(f"Desc:   {item_desc}")
            print(f"Price:  ${unit_price:,.2f}")
            print(f"Stock:  {qty_on_hand}")
            print(f"Total Value: ${total_value:,.2f}")
            if qty_on_hand <= REORDER_LEVEL:
                print("*** WARNING: STOCK BELOW REORDER LEVEL ***")
            print("-------------------")
        elif action_code == 'Q':
            break
        else:
            print("Invalid Option.")

    print("Exiting Inventory System.")

if __name__ == "__main__":
    main()
