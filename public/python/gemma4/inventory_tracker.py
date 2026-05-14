import sys

def main():
    print("=== INVENTORY MANAGEMENT ===")
    print("Initialize a new item tracking...")
    
    item_id = input("Item ID: ").strip()
    item_desc = input("Item Description: ").strip()
    
    try:
        unit_price = float(input("Unit Price: "))
        qty_on_hand = int(input("Initial Quantity: "))
    except ValueError:
        print("Invalid numeric input. Please restart.")
        return

    reorder_level = 20

    while True:
        print("\nAction (A=Add, R=Remove, C=Check, Q=Quit): ")
        action_code = input().strip().upper()

        if action_code == 'A':
            try:
                trx_qty = int(input("QTY to Add: "))
                qty_on_hand += trx_qty
                print(f"Stock updated. Current QTY: {qty_on_hand}")
            except ValueError:
                print("Invalid quantity.")
        
        elif action_code == 'R':
            try:
                trx_qty = int(input("QTY to Remove (Sale): "))
                if trx_qty > qty_on_hand:
                    print(f"Cannot remove! Only {qty_on_hand} available.")
                else:
                    qty_on_hand -= trx_qty
                    print(f"Stock shipped. Current QTY: {qty_on_hand}")
            except ValueError:
                print("Invalid quantity.")
        
        elif action_code == 'C':
            total_value = qty_on_hand * unit_price
            print("--- ITEM STATUS ---")
            print(f"ID:     {item_id}")
            print(f"Desc:   {item_desc}")
            print(f"Price:  ${unit_price:,.2f}")
            print(f"Stock:  {qty_on_hand}")
            print(f"Total Value: ${total_value:,.2f}")
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
