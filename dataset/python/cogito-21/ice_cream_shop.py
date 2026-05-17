class IceCreamShop:
    def __init__(self):
        self.prices = {
            'scoop': 2.50,
            'waffle_cone': 1.50,
            'topping': 0.75
        }
        self.order = {
            'customer_name': '',
            'scoops': 0,
            'vessel': '',
            'toppings': 0
        }
        self.totals = {
            'ice_cream': 0.0,
            'cone': 0.0,
            'toppings': 0.0,
            'total': 0.0
        }

    def get_order_details(self):
        print("--- SWEET SCOOPS ICE CREAM ---")
        self.order['customer_name'] = input("Name for Order: ").strip()
        
        while True:
            try:
                self.order['scoops'] = int(input("Number of Scoops ($2.50 ea): "))
                if self.order['scoops'] < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            vessel = input("Vessel (W=Waffle Cone $1.50, C=Cup $0): ").strip().upper()
            if vessel in ['W', 'C']:
                self.order['vessel'] = vessel
                break
            print("Please enter 'W' for Waffle Cone or 'C' for Cup.")
        
        while True:
            try:
                self.order['toppings'] = int(input("Number of Toppings ($0.75 ea): "))
                if self.order['toppings'] < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

    def calculate_totals(self):
        self.totals['ice_cream'] = self.order['scoops'] * self.prices['scoop']
        
        if self.order['vessel'] == 'W':
            self.totals['cone'] = self.prices['waffle_cone']
        
        self.totals['toppings'] = self.order['toppings'] * self.prices['topping']
        
        self.totals['total'] = (
            self.totals['ice_cream'] + 
            self.totals['cone'] + 
            self.totals['toppings']
        )

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("             ORDER TICKET               ")
        print("=" * 40)
        print(f"Name: {self.order['customer_name']}")
        print("-" * 40)
        
        print(f"Ice Cream ({self.order['scoops']} scoops): ${self.totals['ice_cream']:.2f}")
        
        if self.order['vessel'] == 'W':
            print(f"Waffle Cone:           ${self.totals['cone']:.2f}")
        
        if self.order['toppings'] > 0:
            print(f"Toppings ({self.order['toppings']}):          ${self.totals['toppings']:.2f}")
        
        print("-" * 40)
        print(f"TOTAL DUE:             ${self.totals['total']:.2f}")
        print("=" * 40)

def main():
    shop = IceCreamShop()
    shop.get_order_details()
    shop.calculate_totals()
    shop.display_receipt()

if __name__ == "__main__":
    main()
