class ArtGallery:
    def __init__(self):
        self.collector_name = ""
        self.art_title = ""
        self.art_price = 0.0
        self.ship_method = 0
        self.ship_fee = 0.0
        self.handling_fee = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- MODERN CANVAS GALLERY ---")
        self.collector_name = input("Collector Name: ")
        self.art_title = input("Artwork Title: ")
        self.art_price = float(input("Artwork Price ($): "))
        print("Delivery: 1=Pickup, 2=Domestic, 3=Intl: ")
        self.ship_method = int(input())

    def calculate_fees(self):
        if self.ship_method == 1:  # Pickup
            self.ship_fee = 0.0
            self.handling_fee = 0.0
        elif self.ship_method == 2:  # Domestic
            self.ship_fee = self.art_price * 0.03
            self.handling_fee = 50.00
        elif self.ship_method == 3:  # International
            self.ship_fee = self.art_price * 0.08
            self.handling_fee = 150.00
        else:
            self.ship_fee = 0.0
            self.handling_fee = 0.0

        self.grand_total = self.art_price + self.ship_fee + self.handling_fee

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("           GALLERY INVOICE              ")
        print("=" * 40)
        print(f"Aquired By: {self.collector_name}")
        print(f"Artwork:    {self.art_title}")
        print("-" * 40)
        print(f"Base Price:          ${self.art_price:,.2f}")
        
        if self.ship_fee > 0:
            print(f"Freight Assessed:    ${self.ship_fee:,.2f}")
        
        if self.handling_fee > 0:
            print(f"Crate/Handling:      ${self.handling_fee:,.2f}")
            
        print("-" * 40)
        print(f"TOTAL PAYABLE:       ${self.grand_total:,.2f}")
        print("=" * 40)

    def run_sale(self):
        self.get_input()
        self.calculate_fees()
        self.display_invoice()

if __name__ == "__main__":
    gallery = ArtGallery()
    gallery.run_sale()
