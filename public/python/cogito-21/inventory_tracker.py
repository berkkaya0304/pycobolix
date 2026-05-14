class InventoryTracker:
    def __init__(self):
        self.item_id = ""
        self.item_desc = ""
        self.qty_on_hand = 0
        self.reorder_level = 20
        self.unit_price = 0.0

    def add_stock(self):
        try:
            qty = int(input("QTY to Add: "))
            self.qty_on_hand += qty
            print(f"Stock updated. Current QTY: {self.qty_on_hand}")
        except ValueError:
            print("Invalid quantity entered.")

    def remove_stock(self):
        try:
            qty = int(input("QTY to Remove (Sale): "))
            if qty > self.qty_on_hand:
                print(f"Cannot remove! Only {self.qty_on_hand} available.")
            else:
                self.qty_on_hand -= qty
                print(f"Stock shipped. Current QTY: {self.qty_on_hand}")
        except ValueError:
            print("Invalid quantity entered.")

    def check_status(self):
        total_value = self.qty_on_hand * self.unit_price
        print("\n--- ITEM STATUS ---")
        print(f"ID:     {self.item_id}")
        print(f"Desc:   {self.item_desc}")
        print(f"Price:  ${self.unit_price:,.2f}")
        print(f"Stock:  {self.qty_on_hand}")
        print(f"Total Value: ${total_value:,.2f}")
        if self.qty_on_hand <= self.reorder_level:
            print("*** WARNING: STOCK BELOW REORDER LEVEL ***")
        print("-------------------")

    def run(self):
        print("=== INVENTORY MANAGEMENT ===")
        print("Initialize a new item tracking...")
        self.item_id = input("Item ID: ").strip()
        self.item_desc = input("Item Description: ").strip()
        
        while True:
            try:
                self.unit_price = float(input("Unit Price: "))
                break
            except ValueError:
                print("Please enter a valid price.")
        
        while True:
            try:
                self.qty_on_hand = int(input("Initial Quantity: "))
                break
            except ValueError:
                print("Please enter a valid quantity.")

        while True:
            print("\nAction (A=Add, R=Remove, C=Check, Q=Quit): ", end="")
            action = input().strip().upper()
            
            if action == 'Q':
                break
            elif action == 'A':
                self.add_stock()
            elif action == 'R':
                self.remove_stock()
            elif action == 'C':
                self.check_status()
            else:
                print("Invalid Option.")

        print("Exiting Inventory System.")

if __name__ == "__main__":
    tracker = InventoryTracker()
    tracker.run()
