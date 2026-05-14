class PlantNursery:
    def __init__(self):
        self.prices = {
            'succulents': 5.50,
            'ferns': 15.00,
            'trees': 45.00,
            'pots': 8.50,
            'soil': 12.00
        }
        self.cart = {
            'succulents': 0,
            'ferns': 0,
            'trees': 0,
            'pots': 0,
            'soil': 0
        }
        self.totals = {
            'succulents': 0.0,
            'ferns': 0.0,
            'trees': 0.0,
            'pots': 0.0,
            'soil': 0.0
        }
        self.grand_total = 0.0

    def get_quantity(self, prompt):
        while True:
            try:
                qty = int(input(prompt))
                if qty < 0:
                    print("Please enter a non-negative number.")
                    continue
                return qty
            except ValueError:
                print("Please enter a valid number.")

    def calculate_totals(self):
        for item in self.cart:
            self.totals[item] = self.cart[item] * self.prices[item]
        self.grand_total = sum(self.totals.values())

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("            GARDEN RECEIPT              ")
        print("=" * 40)
        
        item_display = {
            'succulents': ('Succulents', 16),
            'ferns': ('Ferns', 20),
            'trees': ('Trees', 20),
            'pots': ('Ceramic Pots', 13),
            'soil': ('Potting Soil', 14)
        }
        
        for item, (display_name, padding) in item_display.items():
            if self.cart[item] > 0:
                formatted_total = f"${self.totals[item]:.2f}"
                print(f"{display_name} ({self.cart[item]}):{formatted_total:>{padding}}")
        
        print("-" * 40)
        print(f"TOTAL AMOUNT DUE:    ${self.grand_total:>7.2f}")
        print("=" * 40)

    def run(self):
        print("--- BOTANICA PLANT NURSERY ---")
        self.cart['succulents'] = self.get_quantity("Mini Succulents QTY ($5.50 ea): ")
        self.cart['ferns'] = self.get_quantity("Ferns & Hanging Plants QTY ($15.00 ea): ")
        self.cart['trees'] = self.get_quantity("Small Indoor Trees QTY ($45.00 ea): ")
        self.cart['pots'] = self.get_quantity("Ceramic Pots ($8.50 ea): ")
        self.cart['soil'] = self.get_quantity("Bags of Potting Soil ($12.00 ea): ")
        
        self.calculate_totals()
        self.display_receipt()

if __name__ == "__main__":
    nursery = PlantNursery()
    nursery.run()
