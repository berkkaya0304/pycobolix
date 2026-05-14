class OrderProcessing:
    def __init__(self):
        self.order_header = {
            'order_number': '',
            'customer_name': '',
            'order_date': ''
        }
        self.items = [{
            'product_name': '',
            'quantity': 0,
            'price': 0.0,
            'subtotal': 0.0
        } for _ in range(3)]
        self.totals = {
            'grand_subtotal': 0.0,
            'tax_amount': 0.0,
            'shipping': 15.0,
            'final_total': 0.0
        }

    def get_input(self):
        print("*** ONLINE ORDER SYSTEM ***")
        self.order_header['order_number'] = input("Order Number: ")
        self.order_header['customer_name'] = input("Customer Name: ")
        self.order_header['order_date'] = input("Date (YYYY-MM-DD): ")

        for i in range(3):
            print(f"--- Enter Item {i+1} ---")
            self.items[i]['product_name'] = input("Product Name: ")
            self.items[i]['quantity'] = int(input("Quantity: "))
            self.items[i]['price'] = float(input("Unit Price: "))
            self.items[i]['subtotal'] = self.items[i]['quantity'] * self.items[i]['price']
            self.totals['grand_subtotal'] += self.items[i]['subtotal']

    def calculate_totals(self):
        self.totals['tax_amount'] = self.totals['grand_subtotal'] * 0.08
        if self.totals['grand_subtotal'] > 500:
            self.totals['shipping'] = 0.0
        self.totals['final_total'] = (self.totals['grand_subtotal'] + 
                                     self.totals['tax_amount'] + 
                                     self.totals['shipping'])

    def print_invoice(self):
        print("\n=============================================")
        print(f"  INVOICE #{self.order_header['order_number']}    DATE: {self.order_header['order_date']}")
        print(f"  BILL TO: {self.order_header['customer_name']}")
        print("---------------------------------------------")
        print("ITEM            QTY         PRICE       SUBTOTAL")
        print("---------------------------------------------")
        
        for item in self.items:
            print(f"{item['product_name']:15} {item['quantity']:3}         "
                  f"${item['price']:7.2f}     ${item['subtotal']:8.2f}")
        
        print("---------------------------------------------")
        print(f"  Goods Total:   ${self.totals['grand_subtotal']:10,.2f}")
        print(f"  Tax (8%):      ${self.totals['tax_amount']:10,.2f}")
        print(f"  Shipping:      ${self.totals['shipping']:10,.2f}")
        print("=============================================")
        print(f"  FINAL PAYABLE: ${self.totals['final_total']:11,.2f}")
        print("=============================================")

    def run(self):
        self.get_input()
        self.calculate_totals()
        self.print_invoice()

if __name__ == "__main__":
    order = OrderProcessing()
    order.run()
