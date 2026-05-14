class HairSalon:
    def __init__(self):
        self.client_name = ""
        self.wants_cut = False
        self.wants_color = False
        self.stylist_level = 1
        self.tip_percent = 0
        self.cut_fee = 0.0
        self.color_fee = 0.0
        self.level_rate = 1.0
        self.subtotal = 0.0
        self.tip_amount = 0.0
        self.total_due = 0.0

    def get_client_info(self):
        print("--- GLAMOUR STUDIO TICKET ---")
        self.client_name = input("Client: ").strip()
        
        cut_input = input("Haircut? (Y/N): ").strip().upper()
        self.wants_cut = cut_input == 'Y'
        
        color_input = input("Color/Dye? (Y/N): ").strip().upper()
        self.wants_color = color_input == 'Y'
        
        stylist_input = input("Stylist Level (1=Jr, 2=Sr, 3=Master): ").strip()
        self.stylist_level = int(stylist_input) if stylist_input.isdigit() else 1
        
        tip_input = input("Tip Percentage (e.g. 15, 20): ").strip()
        self.tip_percent = int(tip_input) if tip_input.isdigit() else 0

    def calculate_charges(self):
        if self.stylist_level == 1:
            self.level_rate = 1.00
        elif self.stylist_level == 2:
            self.level_rate = 1.30
        elif self.stylist_level == 3:
            self.level_rate = 1.80
        else:
            self.level_rate = 1.00

        if self.wants_cut:
            self.cut_fee = 35.00 * self.level_rate

        if self.wants_color:
            self.color_fee = 85.00 * self.level_rate

        self.subtotal = self.cut_fee + self.color_fee
        self.tip_amount = self.subtotal * (self.tip_percent / 100)
        self.total_due = self.subtotal + self.tip_amount

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("             SALON INVOICE              ")
        print("=" * 40)
        print(f"Client: {self.client_name}")
        print("-" * 40)
        
        if self.wants_cut:
            print(f"Haircut Service:    ${self.cut_fee:,.2f}")
        if self.wants_color:
            print(f"Coloring Service:   ${self.color_fee:,.2f}")
            
        print("-" * 40)
        print(f"Services Total:     ${self.subtotal:,.2f}")
        
        if self.tip_amount > 0:
            print(f"Stylist Tip ({self.tip_percent}%):  ${self.tip_amount:,.2f}")
            
        print("-" * 40)
        print(f"TOTAL CHARGED:      ${self.total_due:,.2f}")
        print("=" * 40)

def main():
    salon = HairSalon()
    salon.get_client_info()
    salon.calculate_charges()
    salon.display_invoice()

if __name__ == "__main__":
    main()
