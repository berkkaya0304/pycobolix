class BakeryShop:
    def __init__(self):
        self.cake_price = 25.00
        self.bread_price = 4.50
        self.pastry_price = 3.00
        self.customer_name = ""
        self.cake_qty = 0
        self.bread_qty = 0
        self.pastry_qty = 0
        self.cake_total = 0.0
        self.bread_total = 0.0
        self.pastry_total = 0.0
        self.subtotal = 0.0
        self.discount = 0.0
        self.final_total = 0.0

    def get_order(self):
        print("--- SUNRISE BAKERY POS ---")
        self.customer_name = input("Customer Name: ")
        self.cake_qty = int(input("Whole Cakes ($25.00 ea): "))
        self.bread_qty = int(input("Loaves of Bread ($4.50 ea): "))
        self.pastry_qty = int(input("Assorted Pastries ($3.00 ea): "))

    def process_order(self):
        self.cake_total = self.cake_qty * self.cake_price
        self.bread_total = self.bread_qty * self.bread_price
        self.pastry_total = self.pastry_qty * self.pastry_price
        self.subtotal = self.cake_total + self.bread_total + self.pastry_total
        
        if self.subtotal >= 50.00:
            self.discount = self.subtotal * 0.10
            
        self.final_total = self.subtotal - self.discount

    def print_bill(self):
        print("\n=========================================")
        print("          BAKERY ORDER RECEIPT           ")
        print("=========================================")
        print(f"Customer: {self.customer_name}")
        print("-----------------------------------------")
        
        if self.cake_qty > 0:
            print(f"{self.cake_qty} x Cakes:         ${self.cake_total:7.2f}")
        if self.bread_qty > 0:
            print(f"{self.bread_qty} x Bread Loaves:  ${self.bread_total:7.2f}")
        if self.pastry_qty > 0:
            print(f"{self.pastry_qty} x Pastries:      ${self.pastry_total:7.2f}")
            
        print("-----------------------------------------")
        print(f"Subtotal:         ${self.subtotal:7.2f}")
        
        if self.discount > 0:
            print(f"Bulk Discount:   -${self.discount:7.2f}")
            
        print("-----------------------------------------")
        print(f"TOTAL DUE:        ${self.final_total:7.2f}")
        print("=========================================")

def main():
    shop = BakeryShop()
    shop.get_order()
    shop.process_order()
    shop.print_bill()

if __name__ == "__main__":
    main()
