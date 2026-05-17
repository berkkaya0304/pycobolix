class SupermarketCheckout:
    def __init__(self):
        self.items = []
        self.gross_total = 0.0
        self.tax_amount = 0.0
        self.net_total = 0.0
        self.member_card = ''

    def get_currency(self, amount):
        return f"${amount:,.2f}"

    def get_input(self, prompt):
        return input(prompt).strip()

    def run(self):
        print("--- FRESH MART CHECKOUT ---")
        self.member_card = self.get_input("Do you have a loyalty card? (Y/N): ").upper()

        for i in range(3):
            item = {}
            print(f"\nItem {i+1}")
            item['name'] = self.get_input("Item Name: ")
            
            while True:
                pricing_type = self.get_input("Pricing (U=Unit, W=Weight/lbs): ").upper()
                if pricing_type in ('U', 'W'):
                    item['pricing_type'] = pricing_type
                    break
                print("Invalid input. Please enter 'U' or 'W'.")
            
            while True:
                try:
                    price = float(self.get_input("Price per U/W ($): "))
                    if price >= 0:
                        item['price'] = price
                        break
                    print("Price cannot be negative.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            while True:
                try:
                    if item['pricing_type'] == 'U':
                        qty = int(self.get_input("Quantity: "))
                    else:
                        qty = float(self.get_input("Weight (lbs): "))
                    if qty > 0:
                        item['quantity'] = qty
                        break
                    print("Value must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            item['subtotal'] = item['price'] * item['quantity']
            self.gross_total += item['subtotal']
            self.items.append(item)
        
        self.process_bill()
        self.print_receipt()

    def process_bill(self):
        if self.member_card == 'Y':
            self.gross_total *= 0.95
            print("\n(5% Member Discount Applied)")
        
        self.tax_amount = self.gross_total * 0.02
        self.net_total = self.gross_total + self.tax_amount

    def print_receipt(self):
        print("\n" + "=" * 40)
        print("          FRESH MART RECEIPT           ")
        print("=" * 40)
        
        for item in self.items:
            if item['pricing_type'] == 'U':
                qty_display = f"x {int(item['quantity'])}"
            else:
                qty_display = f"x {item['quantity']} lbs"
            
            print(f"{item['name']:15} {qty_display:10} {self.get_currency(item['subtotal']):>10}")
        
        print("-" * 40)
        print(f"Subtotal:        {self.get_currency(self.gross_total):>10}")
        print(f"Tax (2%):        {self.get_currency(self.tax_amount):>10}")
        print("-" * 40)
        print(f"TOTAL BALANCE:   {self.get_currency(self.net_total):>10}")
        print("=" * 40)

if __name__ == "__main__":
    checkout = SupermarketCheckout()
    checkout.run()
