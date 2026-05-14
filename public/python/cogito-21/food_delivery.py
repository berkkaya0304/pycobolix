class FoodDelivery:
    def __init__(self):
        self.order_num = 0
        self.food_subtotal = 0.0
        self.miles_away = 0.0
        self.tip_percent = 0
        self.delivery_fee = 0.0
        self.service_fee = 0.0
        self.tax_amt = 0.0
        self.driver_tip = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- QUICK DASH FOOD DELIVERY ---")
        self.order_num = int(input("Order Number: "))
        self.food_subtotal = float(input("Restaurant Food Subtotal ($): "))
        self.miles_away = float(input("Distance from Restaurant (Miles): "))
        self.tip_percent = int(input("Tip Percentage for Driver (e.g. 15, 20): "))

    def calculate_fees(self):
        self.delivery_fee = 2.00 + (self.miles_away * 1.50)
        self.service_fee = self.food_subtotal * 0.15
        self.tax_amt = self.food_subtotal * 0.08
        self.driver_tip = self.food_subtotal * (self.tip_percent / 100)
        self.grand_total = (self.food_subtotal + self.delivery_fee + 
                           self.service_fee + self.tax_amt + self.driver_tip)

    def display_invoice(self):
        print("\n" + "="*40)
        print("           DELIVERY INVOICE             ")
        print("="*40)
        print(f"Order ID: #{self.order_num}")
        print("-"*40)
        print(f"Food Subtotal:      ${self.food_subtotal:,.2f}")
        print(f"Delivery Fee:       ${self.delivery_fee:,.2f}")
        print(f"App Service Fee:    ${self.service_fee:,.2f}")
        print(f"Local Taxes:        ${self.tax_amt:,.2f}")
        print(f"Driver Tip:         ${self.driver_tip:,.2f}")
        print("-"*40)
        print(f"TOTAL CHARGE:       ${self.grand_total:,.2f}")
        print("="*40)

def main():
    order = FoodDelivery()
    order.get_input()
    order.calculate_fees()
    order.display_invoice()

if __name__ == "__main__":
    main()
