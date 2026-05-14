class CarMechanic:
    def __init__(self):
        self.customer_name = ""
        self.vehicle_info = ""
        self.wants_oil = False
        self.wants_tire = False
        self.brake_option = 0
        self.oil_fee = 0.0
        self.tire_fee = 0.0
        self.brake_fee = 0.0
        self.shop_supplies = 15.00
        self.grand_total = 0.0

    def get_customer_info(self):
        print("--- GREASE MONKEY AUTO SHOP ---")
        self.customer_name = input("Customer Name: ")
        self.vehicle_info = input("Vehicle Make/Model: ")

    def get_service_choices(self):
        oil_choice = input("Synthetic Oil Change ($65)? (Y/N): ").upper()
        self.wants_oil = oil_choice == 'Y'
        
        tire_choice = input("Tire Rotation & Balance ($40)? (Y/N): ").upper()
        self.wants_tire = tire_choice == 'Y'
        
        print("Brakes (1=Front $150, 2=Rear $150, 3=All $280,")
        self.brake_option = int(input("0=None): "))

    def calculate_costs(self):
        if self.wants_oil:
            self.oil_fee = 65.00
            
        if self.wants_tire:
            self.tire_fee = 40.00
            
        if self.brake_option == 1 or self.brake_option == 2:
            self.brake_fee = 150.00
        elif self.brake_option == 3:
            self.brake_fee = 280.00
        else:
            self.brake_fee = 0.0
            
        self.grand_total = self.oil_fee + self.tire_fee + self.brake_fee + self.shop_supplies

    def display_invoice(self):
        print("\n" + "="*40)
        print("            REPAIR INVOICE              ")
        print("="*40)
        print(f"Customer: {self.customer_name}")
        print(f"Vehicle:  {self.vehicle_info}")
        print("-"*40)
        
        if self.wants_oil:
            print(f"Lube/Oil Change:    ${self.oil_fee:>6.2f}")
        if self.wants_tire:
            print(f"Tire Rotation:      ${self.tire_fee:>6.2f}")
        if self.brake_fee > 0:
            print(f"Brake Pad Service:  ${self.brake_fee:>6.2f}")
            
        print(f"Shop/Disposal Fee:  ${self.shop_supplies:>6.2f}")
        print("-"*40)
        print(f"GRAND TOTAL:        ${self.grand_total:>6.2f}")
        print("="*40)

    def run(self):
        self.get_customer_info()
        self.get_service_choices()
        self.calculate_costs()
        self.display_invoice()

if __name__ == "__main__":
    shop = CarMechanic()
    shop.run()
