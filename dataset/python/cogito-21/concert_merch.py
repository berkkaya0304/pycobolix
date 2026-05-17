class ConcertMerch:
    def __init__(self):
        self.prices = {
            'tshirt': 35.00,
            'poster': 15.00,
            'record': 40.00,
            'sign_fee': 20.00
        }
        self.order = {
            'fan_name': '',
            'tshirt_qty': 0,
            'poster_qty': 0,
            'record_qty': 0,
            'wants_signed': False
        }
        self.totals = {
            'tshirt': 0.0,
            'poster': 0.0,
            'record': 0.0,
            'subtotal': 0.0,
            'total_due': 0.0
        }

    def get_input(self):
        print("--- STADIUM MERCH BOOTH ---")
        self.order['fan_name'] = input("Fan Name: ").strip()
        
        self.order['tshirt_qty'] = int(input("Tour T-Shirts ($35 ea): ") or 0)
        self.order['poster_qty'] = int(input("Tour Posters ($15 ea): ") or 0)
        self.order['record_qty'] = int(input("Vinyl Records ($40 ea): ") or 0)
        
        sign_input = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper()
        self.order['wants_signed'] = sign_input == 'Y'

    def calculate_totals(self):
        self.totals['tshirt'] = self.order['tshirt_qty'] * self.prices['tshirt']
        self.totals['poster'] = self.order['poster_qty'] * self.prices['poster']
        self.totals['record'] = self.order['record_qty'] * self.prices['record']
        
        self.totals['subtotal'] = self.totals['tshirt'] + self.totals['poster'] + self.totals['record']
        
        self.totals['total_due'] = self.totals['subtotal']
        if self.order['wants_signed']:
            self.totals['total_due'] += self.prices['sign_fee']

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def display_receipt(self):
        print("\n" + "="*40)
        print("           MERCHANDISE RECEIPT          ")
        print("="*40)
        print(f"Fan: {self.order['fan_name']}")
        print("-"*40)
        
        if self.order['tshirt_qty'] > 0:
            print(f"T-Shirts ({self.order['tshirt_qty']}):        {self.format_currency(self.totals['tshirt'])}")
        if self.order['poster_qty'] > 0:
            print(f"Posters ({self.order['poster_qty']}):         {self.format_currency(self.totals['poster'])}")
        if self.order['record_qty'] > 0:
            print(f"Vinyl Records ({self.order['record_qty']}):   {self.format_currency(self.totals['record'])}")
            
        print("-"*40)
        print(f"Subtotal:            {self.format_currency(self.totals['subtotal'])}")
        
        if self.order['wants_signed']:
            print(f"VIP Autograph Add-On: {self.format_currency(self.prices['sign_fee'])}")
            
        print("-"*40)
        print(f"TOTAL AMOUNT DUE:    {self.format_currency(self.totals['total_due'])}")
        print("="*40)

    def run(self):
        self.get_input()
        self.calculate_totals()
        self.display_receipt()

if __name__ == "__main__":
    booth = ConcertMerch()
    booth.run()
