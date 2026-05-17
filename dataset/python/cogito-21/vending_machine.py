class VendingMachine:
    def __init__(self):
        self.items = {
            "A1": {"name": "Soda", "price": 1.50},
            "A2": {"name": "Chips", "price": 1.25},
            "B1": {"name": "Candy", "price": 2.00},
            "B2": {"name": "Water", "price": 1.00}
        }
        self.amount_inserted = 0.0

    def display_menu(self):
        print("--- SNACK-O-MATIC VENDING ---")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} (${item['price']:.2f})")

    def get_selection(self):
        return input("Enter Selection: ").strip().upper()

    def process_payment(self, price):
        while self.amount_inserted < price:
            try:
                new_money = float(input("Insert Money ($ format): $"))
                if new_money < 0:
                    print("Please enter a positive amount.")
                    continue
                self.amount_inserted += new_money
                print(f"Current Credit: ${self.amount_inserted:.2f}")
            except ValueError:
                print("Invalid amount. Please enter a number.")

    def run(self):
        self.display_menu()
        choice = self.get_selection()
        
        if choice not in self.items:
            print("Invalid Selection.")
            return
            
        item = self.items[choice]
        print(f"Selected: {item['name']}  Cost: ${item['price']:.2f}")
        
        self.process_payment(item['price'])
        
        change = self.amount_inserted - item['price']
        print("-----------------------------------")
        print(f"Vending {item['name']}...  *CLUNK*")
        
        if change > 0:
            print(f"Refunding Change: ${change:.2f}")
        else:
            print("Exact change inserted.")
            
        print("Thank you!")

if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
