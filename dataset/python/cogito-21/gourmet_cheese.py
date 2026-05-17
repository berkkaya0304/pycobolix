class CheeseShop:
    def __init__(self):
        self.prices = {
            'brie': 18.50,
            'cheddar': 12.00,
            'gouda': 16.75,
            'crackers': 4.50
        }
        self.order = {
            'brie': 0.0,
            'cheddar': 0.0,
            'gouda': 0.0,
            'crackers': 0
        }
        self.totals = {
            'brie': 0.0,
            'cheddar': 0.0,
            'gouda': 0.0,
            'crackers': 0.0
        }

    def get_order(self):
        print("--- THE RUSTIC WHEEL CHEESE SHOP ---")
        self.order['brie'] = float(input("French Brie (lbs, $18.50/lb): "))
        self.order['cheddar'] = float(input("Aged Cheddar (lbs, $12.00/lb): "))
        self.order['gouda'] = float(input("Smoked Gouda (lbs, $16.75/lb): "))
        self.order['crackers'] = int(input("Artisan Cracker Boxes ($4.50 ea): "))

    def calculate_totals(self):
        self.totals['brie'] = self.order['brie'] * self.prices['brie']
        self.totals['cheddar'] = self.order['cheddar'] * self.prices['cheddar']
        self.totals['gouda'] = self.order['gouda'] * self.prices['gouda']
        self.totals['crackers'] = self.order['crackers'] * self.prices['crackers']
        return sum(self.totals.values())

    def display_receipt(self, grand_total):
        print("\n" + "=" * 40)
        print("             SHOP RECEIPT               ")
        print("=" * 40)
        
        if self.order['brie'] > 0:
            print(f"Brie ({self.order['brie']} lbs):        ${self.totals['brie']:7.2f}")
        if self.order['cheddar'] > 0:
            print(f"Cheddar ({self.order['cheddar']} lbs):     ${self.totals['cheddar']:7.2f}")
        if self.order['gouda'] > 0:
            print(f"Gouda ({self.order['gouda']} lbs):       ${self.totals['gouda']:7.2f}")
        if self.order['crackers'] > 0:
            print(f"Crackers ({self.order['crackers']} boxes):   ${self.totals['crackers']:7.2f}")
            
        print("-" * 40)
        print(f"TOTAL SALE:          ${grand_total:7.2f}")
        print("=" * 40)

def main():
    shop = CheeseShop()
    shop.get_order()
    grand_total = shop.calculate_totals()
    shop.display_receipt(grand_total)

if __name__ == "__main__":
    main()
