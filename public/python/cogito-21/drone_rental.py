class DroneRental:
    def __init__(self):
        self.rental_info = {
            'customer_name': '',
            'drone_model': 0,
            'days_rented': 0,
            'extra_batteries': 0,
            'wants_insurance': False
        }
        self.fees = {
            'daily_rate': 0.0,
            'drone_total': 0.0,
            'battery_total': 0.0,
            'insurance_total': 0.0,
            'grand_total': 0.0
        }
        self.drone_rates = {
            1: 40.00,
            2: 90.00,
            3: 250.00
        }

    def get_input(self):
        print("--- AERO CAPTURE DRONE RENTALS ---")
        self.rental_info['customer_name'] = input("Renter Name: ")
        
        while True:
            try:
                self.rental_info['drone_model'] = int(input(
                    "Drone (1=Basic $40, 2=Pro 4K $90, 3=Cinema $250): "))
                if self.rental_info['drone_model'] not in self.drone_rates:
                    print("Invalid selection. Please choose 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.rental_info['days_rented'] = int(input("Days to Rent: "))
                if self.rental_info['days_rented'] <= 0:
                    print("Please enter a positive number of days.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.rental_info['extra_batteries'] = int(input(
                    "Extra Battery Packs ($10/day ea): "))
                if self.rental_info['extra_batteries'] < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            insurance = input("Add Crash Insurance ($25/day)? (Y/N): ").upper()
            if insurance in ['Y', 'N']:
                self.rental_info['wants_insurance'] = (insurance == 'Y')
                break
            print("Please enter Y or N.")

    def calculate_charges(self):
        self.fees['daily_rate'] = self.drone_rates.get(
            self.rental_info['drone_model'], 40.00)
        
        self.fees['drone_total'] = (self.fees['daily_rate'] * 
                                   self.rental_info['days_rented'])
        
        self.fees['battery_total'] = (self.rental_info['extra_batteries'] * 10.00 * 
                                     self.rental_info['days_rented'])
        
        if self.rental_info['wants_insurance']:
            self.fees['insurance_total'] = 25.00 * self.rental_info['days_rented']
        
        self.fees['grand_total'] = (self.fees['drone_total'] + 
                                   self.fees['battery_total'] + 
                                   self.fees['insurance_total'])

    def display_receipt(self):
        print("\n" + "="*40)
        print("          RENTAL AGREEMENT              ")
        print("="*40)
        print(f"Renter: {self.rental_info['customer_name']}")
        print(f"Terms:  {self.rental_info['days_rented']} Day(s)")
        print("-"*40)
        
        print(f"Drone Flight Time:  ${self.fees['drone_total']:,.2f}")
        
        if self.rental_info['extra_batteries'] > 0:
            print(f"Extra Power Packs:  ${self.fees['battery_total']:,.2f}")
        
        if self.rental_info['wants_insurance']:
            print(f"Crash Insurance:    ${self.fees['insurance_total']:,.2f}")
        
        print("-"*40)
        print(f"TOTAL BALANCE:      ${self.fees['grand_total']:,.2f}")
        print("="*40)

    def run(self):
        self.get_input()
        self.calculate_charges()
        self.display_receipt()

if __name__ == "__main__":
    rental = DroneRental()
    rental.run()
