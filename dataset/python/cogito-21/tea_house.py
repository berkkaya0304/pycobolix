class TeaHouse:
    def __init__(self):
        self.rates = {
            'green_tea': 4.00,
            'black_tea': 3.50,
            'herbal_tea': 4.50,
            'pastry': 5.00
        }
        self.order = {
            'patron_name': '',
            'green_tea_qty': 0,
            'black_tea_qty': 0,
            'herbal_tea_qty': 0,
            'pastry_qty': 0
        }
        self.totals = {
            'green_tea_total': 0.0,
            'black_tea_total': 0.0,
            'herbal_tea_total': 0.0,
            'pastry_total': 0.0,
            'grand_total': 0.0
        }

    def get_order(self):
        print("--- ZEN LEAF TEA HOUSE ---")
        self.order['patron_name'] = input("Name: ").strip()
        
        self.order['green_tea_qty'] = int(input("Matcha/Green Tea QTY ($4.00): ") or 0)
        self.order['black_tea_qty'] = int(input("Earl Grey/Black Tea QTY ($3.50): ") or 0)
        self.order['herbal_tea_qty'] = int(input("Chamomile/Herbal QTY ($4.50): ") or 0)
        self.order['pastry_qty'] = int(input("Assorted Pastries ($5.00): ") or 0)

    def calculate_totals(self):
        self.totals['green_tea_total'] = self.order['green_tea_qty'] * self.rates['green_tea']
        self.totals['black_tea_total'] = self.order['black_tea_qty'] * self.rates['black_tea']
        self.totals['herbal_tea_total'] = self.order['herbal_tea_qty'] * self.rates['herbal_tea']
        self.totals['pastry_total'] = self.order['pastry_qty'] * self.rates['pastry']
        
        self.totals['grand_total'] = (self.totals['green_tea_total'] + 
                                     self.totals['black_tea_total'] + 
                                     self.totals['herbal_tea_total'] + 
                                     self.totals['pastry_total'])

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("             TEA INVOICE                ")
        print("=" * 40)
        print(f"Patron: {self.order['patron_name']}")
        print("-" * 40)
        
        if self.order['green_tea_qty'] > 0:
            print(f"{self.order['green_tea_qty']}x Green Teas:       ${self.totals['green_tea_total']:,.2f}")
        if self.order['black_tea_qty'] > 0:
            print(f"{self.order['black_tea_qty']}x Black Teas:       ${self.totals['black_tea_total']:,.2f}")
        if self.order['herbal_tea_qty'] > 0:
            print(f"{self.order['herbal_tea_qty']}x Herbal Teas:      ${self.totals['herbal_tea_total']:,.2f}")
        if self.order['pastry_qty'] > 0:
            print(f"{self.order['pastry_qty']}x Fresh Pastries:   ${self.totals['pastry_total']:,.2f}")
            
        print("-" * 40)
        print(f"TOTAL BALANCE:       ${self.totals['grand_total']:,.2f}")
        print("=" * 40)

    def run(self):
        self.get_order()
        self.calculate_totals()
        self.display_invoice()

if __name__ == "__main__":
    tea_house = TeaHouse()
    tea_house.run()
