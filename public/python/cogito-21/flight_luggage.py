class FlightLuggage:
    def __init__(self):
        self.MAX_WEIGHT = 23
        self.MAX_DIM = 158
        self.flight_num = ""
        self.passenger_id = ""
        self.bag_weight_kg = 0.0
        self.bag_length = 0
        self.bag_width = 0
        self.bag_height = 0
        self.total_dim = 0
        self.over_wt_fee = 0.0
        self.over_sz_fee = 0.0
        self.total_fee = 0.0

    def get_input(self):
        print("--- AIRPORT LUGGAGE SCANNER ---")
        self.flight_num = input("Flight Number: ")
        self.passenger_id = input("Passenger ID: ")
        self.bag_weight_kg = float(input("Bag Weight (kg): "))
        self.bag_length = int(input("Bag Length (cm): "))
        self.bag_width = int(input("Bag Width (cm): "))
        self.bag_height = int(input("Bag Height (cm): "))

    def check_bag(self):
        self.total_dim = self.bag_length + self.bag_width + self.bag_height
        weight_ovr = self.bag_weight_kg - self.MAX_WEIGHT
        dim_ovr = self.total_dim - self.MAX_DIM

        if weight_ovr > 0:
            self.over_wt_fee = weight_ovr * 15.00

        if dim_ovr > 0:
            self.over_sz_fee = 50.00

        self.total_fee = self.over_wt_fee + self.over_sz_fee

    def print_tag(self):
        print("\n" + "=" * 40)
        print("           LUGGAGE TAG & FEE           ")
        print("=" * 40)
        print(f"Flight: {self.flight_num} | Pass ID: {self.passenger_id}")
        print("-" * 40)
        print(f"Bag Weight: {self.bag_weight_kg} kg")
        print(f"Bag Dims:   {self.total_dim} cm total")

        if self.over_wt_fee > 0 or self.over_sz_fee > 0:
            print("-" * 40)
            print(">>> BAG EXCEEDS ALLOWANCE <<<")
            if self.over_wt_fee > 0:
                print(f"Overweight Fee: ${self.over_wt_fee:,.2f}")
            if self.over_sz_fee > 0:
                print(f"Oversized Fee:  ${self.over_sz_fee:,.2f}")
            print("-" * 40)
            print(f"EXCESS FEES TO PAY: ${self.total_fee:,.2f}")
        else:
            print("-" * 40)
            print("Status: OK TO LOAD (No Fees)")
        print("=" * 40)

    def run(self):
        self.get_input()
        self.check_bag()
        self.print_tag()

if __name__ == "__main__":
    app = FlightLuggage()
    app.run()
