class TailorShop:
    def __init__(self):
        self.hem_rate = 15.00
        self.zip_rate = 25.00
        self.suit_rate = 120.00
        self.rush_fee_rate = 0.30

    def get_customer_input(self):
        print("--- FINE STITCHES ALTERATIONS ---")
        self.cust_name = input("Customer Name: ")
        self.hemming_qty = int(input("Pants/Skirts Hemming QTY ($15 ea): "))
        self.zipper_qty = int(input("Zipper Replacements QTY ($25 ea): "))
        self.suit_fit_qty = int(input("Full Suit Tailoring QTY ($120 ea): "))
        rush_input = input("Rush Order (Next Day +30%)? (Y/N): ")
        self.is_rush = rush_input.upper() == 'Y'

    def calculate_totals(self):
        self.hem_tot = self.hemming_qty * self.hem_rate
        self.zip_tot = self.zipper_qty * self.zip_rate
        self.suit_tot = self.suit_fit_qty * self.suit_rate
        
        self.sub_total = self.hem_tot + self.zip_tot + self.suit_tot
        self.rush_fee = self.sub_total * self.rush_fee_rate if self.is_rush else 0
        self.grand_total = self.sub_total + self.rush_fee

    def display_receipt(self):
        print("\n" + "=" * 40)
        print("          ALTERATION TICKET             ")
        print("=" * 40)
        print(f"Name: {self.cust_name}")
        print("-" * 40)
        
        if self.hemming_qty > 0:
            print(f"{self.hemming_qty}x Hemming:          ${self.hem_tot:,.2f}")
        if self.zipper_qty > 0:
            print(f"{self.zipper_qty}x Zipper Fix:       ${self.zip_tot:,.2f}")
        if self.suit_fit_qty > 0:
            print(f"{self.suit_fit_qty}x Suit Tailoring:   ${self.suit_tot:,.2f}")
            
        print("-" * 40)
        print(f"Subtotal:           ${self.sub_total:,.2f}")
        
        if self.is_rush:
            print(f"Rush Charge (30%):  ${self.rush_fee:,.2f}")
            
        print("-" * 40)
        print(f"TOTAL BALANCE:      ${self.grand_total:,.2f}")
        print("=" * 40)

    def run(self):
        self.get_customer_input()
        self.calculate_totals()
        self.display_receipt()

if __name__ == "__main__":
    shop = TailorShop()
    shop.run()
