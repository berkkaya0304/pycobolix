class FlightBooking:
    def __init__(self):
        self.passenger_name = ""
        self.destination = 0
        self.ticket_class = ""
        self.luggage_count = 0
        self.base_fare = 0.0
        self.class_surcharge = 0.0
        self.luggage_fee = 0.0
        self.total_cost = 0.0
        self.tax_amount = 0.0
        self.grand_total = 0.0

    def get_details(self):
        self.passenger_name = input("Passenger Name: ")
        print("Destinations: 1=New York($300), 2=London($600), 3=Tokyo($900)")
        self.destination = int(input("Select Destination (1/2/3): "))
        self.ticket_class = input("Class (E=Economy, B=Business +50%, F=First +100%): ").upper()
        self.luggage_count = int(input("Number of checked bags ($50 each): "))

    def calculate_fare(self):
        if self.destination == 1:
            self.base_fare = 300.00
        elif self.destination == 2:
            self.base_fare = 600.00
        elif self.destination == 3:
            self.base_fare = 900.00
        else:
            self.base_fare = 300.00
            print("Invalid destination, defaulted to NY.")

        if self.ticket_class == 'E':
            self.class_surcharge = 0.0
        elif self.ticket_class == 'B':
            self.class_surcharge = self.base_fare * 0.50
        elif self.ticket_class == 'F':
            self.class_surcharge = self.base_fare * 1.00
        else:
            self.class_surcharge = 0.0

        self.luggage_fee = self.luggage_count * 50.00
        self.total_cost = self.base_fare + self.class_surcharge + self.luggage_fee
        self.tax_amount = self.total_cost * 0.10
        self.grand_total = self.total_cost + self.tax_amount

    def print_ticket(self):
        print("\n=============================================")
        print("               BOARDING PASS                 ")
        print("=============================================")
        print(f"Name: {self.passenger_name}")
        
        print(f"Base Fare:       ${self.base_fare:,.2f}")
        if self.class_surcharge > 0:
            print(f"Class Upgrade:   ${self.class_surcharge:,.2f}")
        if self.luggage_fee > 0:
            print(f"Baggage Fees:    ${self.luggage_fee:,.2f}")
        print("---------------------------------------------")
        print(f"Taxes (10%):     ${self.tax_amount:,.2f}")
        print(f"TOTAL FARE:      ${self.grand_total:,.2f}")
        print("=============================================")

def main():
    print("--- AIRLINE RESERVATION ---")
    while True:
        booking = FlightBooking()
        booking.get_details()
        booking.calculate_fare()
        booking.print_ticket()
        
        continue_prog = input("Book another flight? (Y/N): ").upper()
        if continue_prog != 'Y':
            print("System Terminated.")
            break

if __name__ == "__main__":
    main()
