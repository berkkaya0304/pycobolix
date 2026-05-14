class ComicBookStore:
    def __init__(self):
        self.prices = {
            'comic': 4.99,
            'figure': 24.99,
            'board_game': 49.99
        }
        self.cart = {
            'comic': 0,
            'figure': 0,
            'board_game': 0
        }
        self.is_subscriber = False
        self.subtotal = 0.0
        self.discount = 0.0
        self.final_bill = 0.0

    def get_quantity(self, item_name):
        while True:
            try:
                qty = int(input(f"{item_name} QTY: "))
                if qty < 0:
                    print("Please enter a non-negative number.")
                    continue
                return qty
            except ValueError:
                print("Please enter a valid number.")

    def get_yes_no(self, prompt):
        while True:
            response = input(prompt).strip().upper()
            if response in ('Y', 'N'):
                return response == 'Y'
            print("Please enter 'Y' or 'N'.")

    def calculate_totals(self):
        self.subtotal = (
            self.cart['comic'] * self.prices['comic'] +
            self.cart['figure'] * self.prices['figure'] +
            self.cart['board_game'] * self.prices['board_game']
        )
        
        self.discount = self.subtotal * 0.10 if self.is_subscriber else 0.0
        self.final_bill = self.subtotal - self.discount

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("             STORE TICKET               ")
        print("=" * 40)
        
        if self.cart['comic'] > 0:
            total = self.cart['comic'] * self.prices['comic']
            print(f"Comics ({self.cart['comic']}):           {self.format_currency(total)}")
            
        if self.cart['figure'] > 0:
            total = self.cart['figure'] * self.prices['figure']
            print(f"Figures ({self.cart['figure']}):          {self.format_currency(total)}")
            
        if self.cart['board_game'] > 0:
            total = self.cart['board_game'] * self.prices['board_game']
            print(f"Board Games ({self.cart['board_game']}):      {self.format_currency(total)}")
            
        print("-" * 40)
        print(f"Subtotal:            {self.format_currency(self.subtotal)}")
        
        if self.is_subscriber:
            print(f"Subscriber Disc(10%):-{self.format_currency(self.discount)}")
            
        print("-" * 40)
        print(f"TOTAL BALANCE:       {self.format_currency(self.final_bill)}")
        print("=" * 40)

    def run(self):
        print("--- GALAXY HEROES COMICS ---")
        self.cart['comic'] = self.get_quantity("Single Issue Comics ($4.99 ea)")
        self.cart['figure'] = self.get_quantity("Action Figures ($24.99 ea)")
        self.cart['board_game'] = self.get_quantity("Board Games ($49.99 ea)")
        self.is_subscriber = self.get_yes_no("Pull-List Subscriber (10% Off)? (Y/N): ")
        
        self.calculate_totals()
        self.display_receipt()

if __name__ == "__main__":
    store = ComicBookStore()
    store.run()
