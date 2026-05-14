def inventory_tracker():
    class InventoryItem:
        def __init__(self):
            self.item_id = ""
            self.item_desc = ""
            self.qty_on_hand = 0
            self.reorder_level = 20
            self.unit_price = 0.0

    class TransactionData:
        def __init__(self):
            self.trx_qty = 0
            self.action_code = ""

    item = InventoryItem()
    transaction = TransactionData()

    print("=== INVENTORY MANAGEMENT ===")
    print("Initialize a new item tracking...")
    item.item_id = input("Item ID: ").strip()
    item.item_desc = input("Item Description: ").strip()
    item.unit_price = float(input("Unit Price: "))
    item.qty_on_hand = int(input("Initial Quantity: "))

    while True:
        print()
        action = input("Action (A=Add, R=Remove, C=Check, Q=Quit): ").strip().upper()

        if action == 'A':
            add_logic(item, transaction)
        elif action == 'R':
            remove_logic(item, transaction)
        elif action == 'C':
            status_logic(item)
        elif action == 'Q':
            break
        else:
            print("Invalid Option.")

    print("Exiting Inventory System.")

def add_logic(item, transaction):
    transaction.trx_qty = int(input("QTY to Add: "))
    item.qty_on_hand += transaction.trx_qty
    print(f"Stock updated. Current QTY: {item.qty_on_hand}")

def remove_logic(item, transaction):
    transaction.trx_qty = int(input("QTY to Remove (Sale): "))
    if transaction.trx_qty > item.qty_on_hand:
        print(f"Cannot remove! Only {item.qty_on_hand} available.")
    else:
        item.qty_on_hand -= transaction.trx_qty
        print(f"Stock shipped. Current QTY: {item.qty_on_hand}")

def status_logic(item):
    total_value = item.qty_on_hand * item.unit_price
    print("--- ITEM STATUS ---")
    print(f"ID:     {item.item_id}")
    print(f"Desc:   {item.item_desc}")
    print(f"Price:  ${item.unit_price:,.2f}")
    print(f"Stock:  {item.qty_on_hand}")
    print(f"Total Value: ${total_value:,.2f}")
    if item.qty_on_hand <= item.reorder_level:
        print("*** WARNING: STOCK BELOW REORDER LEVEL ***")
    print("-------------------")

if __name__ == "__main__":
    inventory_tracker()
