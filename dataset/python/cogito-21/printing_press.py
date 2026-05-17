class PrintingPress:
    def __init__(self):
        self.business_name = ""
        self.flyer_qty = 0
        self.bcard_qty = 0
        self.color_ink = False
        self.rush_print = False
        self.flyer_rate = 0.05
        self.bcard_rate = 0.02
        self.flyer_total = 0.0
        self.bcard_total = 0.0
        self.color_fee = 0.0
        self.rush_fee = 0.0
        self.subtotal = 0.0
        self.grand_total = 0.0

    def get_input(self):
        print("--- INKWELL PRINTING SERVICES ---")
        self.business_name = input("Business Name: ").strip()
        
        while True:
            try:
                self.flyer_qty = int(input("Flyers QTY ($0.05 B&W): ").strip())
                if self.flyer_qty < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.bcard_qty = int(input("Business Cards QTY ($0.02 B&W): ").strip())
                if self.bcard_qty < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        color_input = input("Upgrade to Full Color (+50% base)? (Y/N): ").strip().upper()
        self.color_ink = color_input == 'Y'
        
        rush_input = input("Rush 24Hr Turnaround (+$25 flat)? (Y/N): ").strip().upper()
        self.rush_print = rush_input == 'Y'

    def calculate_totals(self):
        self.flyer_total = self.flyer_qty * self.flyer_rate
        self.bcard_total = self.bcard_qty * self.bcard_rate
        self.subtotal = self.flyer_total + self.bcard_total
        
        if self.color_ink:
            self.color_fee = self.subtotal * 0.50
        
        if self.rush_print:
            self.rush_fee = 25.00
        
        self.grand_total = self.subtotal + self.color_fee + self.rush_fee

    def format_currency(self, amount):
        return f"${amount:,.2f}"

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("             PRINT INVOICE              ")
        print("=" * 40)
        print(f"Account: {self.business_name}")
        print("-" * 40)
        
        if self.flyer_qty > 0:
            print(f"Flyers (x{self.flyer_qty}):  {self.format_currency(self.flyer_total)}")
        
        if self.bcard_qty > 0:
            print(f"Biz Cards (x{self.bcard_qty}):{self.format_currency(self.bcard_total)}")
        
        if self.color_ink:
            print(f"Color Ink (+50%):  {self.format_currency(self.color_fee)}")
        
        if self.rush_print:
            print(f"Rush Handling:     {self.format_currency(self.rush_fee)}")
        
        print("-" * 40)
        print(f"TOTAL ORDER COST:  {self.format_currency(self.grand_total)}")
        print("=" * 40)

def main():
    press = PrintingPress()
    press.get_input()
    press.calculate_totals()
    press.display_invoice()

if __name__ == "__main__":
    main()
