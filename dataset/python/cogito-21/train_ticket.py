class TrainTicket:
    def __init__(self):
        self.passenger_name = ""
        self.age = 0
        self.distance_km = 0
        self.class_type = ""
        self.base_fare = 0.0
        self.concession = 0.0
        self.reservation_fee = 20.0
        self.total_fare = 0.0

    def get_input(self):
        print("--- RAILWAY TICKET BOOKING ---")
        self.passenger_name = input("Passenger Name: ")
        self.age = int(input("Passenger Age: "))
        self.distance_km = int(input("Travel Distance (KM): "))
        self.class_type = input("Class (1=1AC, 2=2AC, S=Sleeper, G=General): ").upper()

    def calculate_fare(self):
        if self.class_type == '1':
            self.base_fare = self.distance_km * 3.50
        elif self.class_type == '2':
            self.base_fare = self.distance_km * 2.00
        elif self.class_type == 'S':
            self.base_fare = self.distance_km * 1.00
        elif self.class_type == 'G':
            self.base_fare = self.distance_km * 0.50
            self.reservation_fee = 0.0
        else:
            self.base_fare = self.distance_km * 0.50
            self.reservation_fee = 0.0

        if self.age >= 60:
            self.concession = self.base_fare * 0.40
        elif self.age <= 12:
            self.concession = self.base_fare * 0.50

        self.total_fare = self.base_fare + self.reservation_fee - self.concession

    def display_ticket(self):
        print("\n===========================================")
        print("          E-TICKET CONFIRMATION            ")
        print("===========================================")
        print(f"Name: {self.passenger_name:<25} Age: {self.age} yrs")
        print(f"Distance: {self.distance_km} km")
        print("-------------------------------------------")
        print(f"Base Distance Fare: ${self.base_fare:,.2f}")
        
        if self.reservation_fee > 0:
            print(f"Reservation Fee:    ${self.reservation_fee:,.2f}")
        
        if self.concession > 0:
            print(f"Age Concession:    -${self.concession:,.2f}")
            
        print("-------------------------------------------")
        print(f"TOTAL FARE PAYABLE: ${self.total_fare:,.2f}")
        print("===========================================")

    def process_ticket(self):
        self.get_input()
        self.calculate_fare()
        self.display_ticket()

if __name__ == "__main__":
    ticket = TrainTicket()
    ticket.process_ticket()
