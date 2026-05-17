class LaundryService:
    def __init__(self):
        self.customer_name = ""
        self.phone_number = ""
        self.shirts_qty = 0
        self.pants_qty = 0
        self.suits_qty = 0
        self.rush_service = False
        self.shirt_cost = 0.0
        self.pant_cost = 0.0
        self.suit_cost = 0.0
        self.rush_fee = 0.0
        self.total_bill = 0.0

    def get_customer_info(self):
        print("=== FRESH & CLEAN DRY CLEANERS ===")
        self.customer_name = input("Customer Name: ")
        self.phone_number = input("Phone Number: ")

    def get_order_details(self):
        self.shirts_qty = int(input("Number of Shirts ($4.50 ea): "))
        self.pants_qty = int(input("Number of Pants ($6.00 ea): "))
        self.suits_qty = int(input("Number of Suits ($15.00 ea): "))
        rush = input("Rush 24-hour service? (+$10 flat) (Y/N): ").upper()
        self.rush_service = (rush == 'Y')

    def calculate_bill(self):
        self.shirt_cost = self.shirts_qty * 4.50
        self.pant_cost = self.pants_qty * 6.00
        self.suit_cost = self.suits_qty * 15.00
        
        self.total_bill = self.shirt_cost + self.pant_cost + self.suit_cost
        
        if self.rush_service:
            self.rush_fee = 10.00
            self.total_bill += self.rush_fee

    def print_ticket(self):
        print("\n" + "-" * 41)
        print("          LAUNDRY CLAIM TICKET           ")
        print("-" * 41)
        print(f"Name: {self.customer_name} | Ph: {self.phone_number}")
        print("-" * 41)
        
        if self.shirts_qty > 0:
            print(f"{self.shirts_qty} x Shirts:       ${self.shirt_cost:7.2f}")
        if self.pants_qty > 0:
            print(f"{self.pants_qty} x Pants:        ${self.pant_cost:7.2f}")
        if self.suits_qty > 0:
            print(f"{self.suits_qty} x Suits:        ${self.suit_cost:7.2f}")
            
        print("-" * 41)
        if self.rush_fee > 0:
            print(f"Rush Service Fee: ${self.rush_fee:7.2f}")
            
        print(f"GRAND TOTAL:      ${self.total_bill:7.2f}")
        print("-" * 41)

    def run(self):
        self.get_customer_info()
        self.get_order_details()
        self.calculate_bill()
        self.print_ticket()

if __name__ == "__main__":
    service = LaundryService()
    service.run()
