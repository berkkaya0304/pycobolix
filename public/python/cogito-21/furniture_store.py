class FurnitureStore:
    def __init__(self):
        self.prices = {
            'sofa': 599.00,
            'table': 349.00,
            'chair': 85.00,
            'delivery': 99.00
        }
        self.customer_name = ""
        self.quantities = {
            'sofa': 0,
            'table': 0,
            'chair': 0
        }
        self.wants_delivery = False
        self.totals = {
            'sofa': 0.0,
            'table': 0.0,
            'chair': 0.0,
            'delivery': 0.0,
            'grand_total': 0.0
        }

    def get_customer_input(self):
        print("--- COZY LIVING FURNITURE ---")
        self.customer_name = input("Customer: ").strip()
        
        self.quantities['sofa'] = int(input("Sectional Sofas ($599.00 ea): ").strip() or 0)
        self.quantities['table'] = int(input("Dining Tables ($349.00 ea): ").strip() or 0)
        self.quantities['chair'] = int(input("Dining Chairs ($85.00 ea): ").strip() or 0)
        
        delivery_input = input("White-Glove Delivery ($99 flat)? (Y/N): ").strip().upper()
        self.wants_delivery = delivery_input == 'Y'

    def calculate_totals(self):
        self.totals['sofa'] = self.quantities['sofa'] * self.prices['sofa']
        self.totals['table'] = self.quantities['table'] * self.prices['table']
        self.totals['chair'] = self.quantities['chair'] * self.prices['chair']
        
        if self.wants_delivery:
            self.totals['delivery'] = self.prices['delivery']
        
        self.totals['grand_total'] = (
            self.totals['sofa'] + 
            self.totals['table'] + 
            self.totals['chair'] + 
            self.totals['delivery']
        )

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("             STORE RECEIPT              ")
        print("=" * 40)
        print(f"Customer: {self.customer_name}")
        print("-" * 40)
        
        if self.quantities['sofa'] > 0:
            print(f"Sofas ({self.quantities['sofa']}):           {self.format_currency(self.totals['sofa'])}")
        if self.quantities['table'] > 0:
            print(f"Tables ({self.quantities['table']}):          {self.format_currency(self.totals['table'])}")
        if self.quantities['chair'] > 0:
            print(f"Chairs ({self.quantities['chair']}):          {self.format_currency(self.totals['chair'])}")
        if self.wants_delivery:
            print(f"Delivery Fee:       {self.format_currency(self.totals['delivery'])}")
            
        print("-" * 40)
        print(f"TOTAL ORDER:        {self.format_currency(self.totals['grand_total'])}")
        print("=" * 40)

    def run(self):
        self.get_customer_input()
        self.calculate_totals()
        self.display_receipt()

if __name__ == "__main__":
    store = FurnitureStore()
    store.run()
