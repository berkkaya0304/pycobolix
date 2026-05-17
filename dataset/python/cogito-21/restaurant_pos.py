class RestaurantPOS:
    def __init__(self):
        self.table_num = 0
        self.guest_count = 0
        self.menu_items = [{'name': '', 'qty': 0, 'price': 0.0, 'subtotal': 0.0} for _ in range(5)]
        self.food_total = 0.0
        self.tax_amount = 0.0
        self.tip_amount = 0.0
        self.grand_total = 0.0

    def get_input(self, prompt, input_type=float):
        while True:
            try:
                if input_type == str:
                    return input(prompt).strip()
                return input_type(input(prompt))
            except ValueError:
                print("Invalid input. Please try again.")

    def start_pos(self):
        print("=== STARLIGHT RESTAURANT POS ===")
        self.table_num = self.get_input("Table Number: ", int)
        self.guest_count = self.get_input("Number of Guests: ", int)

        for i in range(5):
            print(f"\nItem {i+1}:")
            self.menu_items[i]['name'] = self.get_input("Enter Item Name: ", str)
            self.menu_items[i]['qty'] = self.get_input("Enter Quantity: ", int)
            self.menu_items[i]['price'] = self.get_input("Enter Price per Item: ", float)
            
            self.menu_items[i]['subtotal'] = self.menu_items[i]['qty'] * self.menu_items[i]['price']
            self.food_total += self.menu_items[i]['subtotal']

            if i < 4:
                more_items = input("Add another item? (Y/N): ").strip().upper()
                if more_items != 'Y':
                    break
            else:
                print("Max items reached.")

        self.calculate_tax_tip()
        self.print_bill()

    def calculate_tax_tip(self):
        self.tax_amount = self.food_total * 0.0825
        
        if self.guest_count >= 6:
            self.tip_amount = self.food_total * 0.18
            print("\n*** Automatic Gratuity Applied (Party >= 6) ***")
        else:
            self.tip_amount = self.get_input("\nEnter Tip Amount ($): ", float)
        
        self.grand_total = self.food_total + self.tax_amount + self.tip_amount

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def print_bill(self):
        print("\n" + "=" * 50)
        print("              GUEST CHECK                  ")
        print(f" TABLE: {self.table_num}             GUESTS: {self.guest_count}")
        print("=" * 50)
        
        for item in self.menu_items:
            if item['qty'] > 0:
                print(f"{item['name']:15} {item['qty']:2}   {self.format_currency(item['subtotal'])}")
        
        print("-" * 50)
        print(f"SUBTOTAL:         {self.format_currency(self.food_total)}")
        print(f"TAX:              {self.format_currency(self.tax_amount)}")
        print(f"GRATUITY:         {self.format_currency(self.tip_amount)}")
        print("=" * 50)
        print(f"TOTAL DUE:        {self.format_currency(self.grand_total)}")
        print("      Thank You For Dining With Us!        ")
        print("=" * 50)

if __name__ == "__main__":
    pos = RestaurantPOS()
    pos.start_pos()
