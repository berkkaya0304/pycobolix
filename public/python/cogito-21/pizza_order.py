class PizzaOrder:
    def __init__(self):
        self.customer_name = ""
        self.pizza_size = ""
        self.crust_type = 0
        self.topping_qty = 0
        self.base_price = 0.0
        self.crust_fee = 0.0
        self.topping_fee = 0.0
        self.sub_total = 0.0
        self.tax_amt = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- MARIO'S PIZZERIA ---")
        self.customer_name = input("Customer Name: ")
        
        while True:
            self.pizza_size = input("Size (S=Small $10, M=Medium $14, L=Large $18): ").upper()
            if self.pizza_size in ['S', 'M', 'L']:
                break
            print("Invalid size. Please enter S, M, or L.")
        
        while True:
            try:
                self.crust_type = int(input("Crust (1=Thin, 2=Thick, 3=Stuffed +$3): "))
                if self.crust_type in [1, 2, 3]:
                    break
                print("Invalid crust type. Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a number.")
        
        while True:
            try:
                self.topping_qty = int(input("Number of Extra Toppings ($1.50 ea): "))
                if self.topping_qty >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")

    def calculate_order(self):
        size_prices = {'S': 10.00, 'M': 14.00, 'L': 18.00}
        self.base_price = size_prices.get(self.pizza_size, 10.00)
        
        if self.crust_type == 3:
            self.crust_fee = 3.00
        else:
            self.crust_fee = 0.0
            
        self.topping_fee = self.topping_qty * 1.50
        self.sub_total = self.base_price + self.crust_fee + self.topping_fee
        self.tax_amt = self.sub_total * 0.08
        self.grand_total = self.sub_total + self.tax_amt

    def print_receipt(self):
        print("\n" + "=" * 40)
        print("          PIZZA ORDER RECEIPT           ")
        print("=" * 40)
        print(f"Order for: {self.customer_name}")
        print("-" * 40)
        print(f"Base Pizza:       ${self.base_price:.2f}")
        
        if self.crust_fee > 0:
            print(f"Stuffed Crust:    ${self.crust_fee:.2f}")
            
        if self.topping_qty > 0:
            print(f"Toppings ({self.topping_qty}):    ${self.topping_fee:.2f}")
            
        print("-" * 40)
        print(f"Subtotal:         ${self.sub_total:.2f}")
        print(f"Tax (8%):         ${self.tax_amt:.2f}")
        print("=" * 40)
        print(f"TOTAL AMOUNT DUE: ${self.grand_total:.2f}")
        print("=" * 40)

def main():
    order = PizzaOrder()
    order.get_input()
    order.calculate_order()
    order.print_receipt()

if __name__ == "__main__":
    main()
