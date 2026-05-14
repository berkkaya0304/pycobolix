class CarRentalSystem:
    def __init__(self):
        self.customer_name = ""
        self.car_category = 0
        self.days_rented = 0
        self.driver_age = 0
        self.wants_insurance = False
        self.base_rate = 0.0
        self.age_surcharge = 0.0
        self.insurance_fee = 0.0
        self.total_cost = 0.0

    def get_inputs(self):
        self.customer_name = input("Customer Name: ").strip()
        
        while True:
            try:
                self.car_category = int(input("Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): ").strip())
                if self.car_category not in (1, 2, 3):
                    print("Invalid category. Please enter 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.days_rented = int(input("Rental Duration (Days): ").strip())
                if self.days_rented <= 0:
                    print("Please enter a positive number of days.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                self.driver_age = int(input("Driver's Age: ").strip())
                if self.driver_age < 18:
                    print("Driver must be at least 18 years old.")
                    continue
                break
            except ValueError:
                print("Please enter a valid age.")
        
        insurance_input = input("Add Full Insurance ($15/day)? (Y/N): ").strip().upper()
        self.wants_insurance = insurance_input == 'Y'

    def calculate_costs(self):
        category_rates = {1: 30.00, 2: 50.00, 3: 80.00}
        self.base_rate = category_rates.get(self.car_category, 30.00)
        
        base_rental = self.base_rate * self.days_rented
        self.age_surcharge = 20.00 * self.days_rented if self.driver_age < 25 else 0.0
        self.insurance_fee = 15.00 * self.days_rented if self.wants_insurance else 0.0
        self.total_cost = base_rental + self.age_surcharge + self.insurance_fee
        return base_rental

    def print_agreement(self):
        base_rental = self.calculate_costs()
        
        print("\n=================================")
        print(" RENTAL AGREEMENT")
        print("=================================")
        print(f"Renter: {self.customer_name}")
        print(f"Days:   {self.days_rented}")
        
        print(f"Base Rental:    ${base_rental:,.2f}")
        
        if self.age_surcharge > 0:
            print(f"Under 25 Fee:   ${self.age_surcharge:,.2f}")
        
        if self.insurance_fee > 0:
            print(f"Insurance Addon: ${self.insurance_fee:,.2f}")
        
        print("---------------------------------")
        print(f"TOTAL CHARGE:   ${self.total_cost:,.2f}")
        print("=================================")

def main():
    print("### RAPID RENTALS ###")
    
    while True:
        rental = CarRentalSystem()
        rental.get_inputs()
        rental.print_agreement()
        
        continue_rental = input("New rental? (Y/N): ").strip().upper()
        if continue_rental != 'Y':
            break

if __name__ == "__main__":
    main()
