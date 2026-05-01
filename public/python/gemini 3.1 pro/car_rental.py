def main():
    print("### RAPID RENTALS ###")
    is_running = True
    
    while is_running:
        customer_name = input("Customer Name: ")
        car_category = input("Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): ").strip()
        try:
            days_rented = int(input("Rental Duration (Days): "))
        except ValueError:
            days_rented = 1
        try:
            driver_age = int(input("Driver's Age: "))
        except ValueError:
            driver_age = 25
        wants_insurance = input("Add Full Insurance ($15/day)? (Y/N): ").strip().upper() == 'Y'

        if car_category == '1':
            base_rate = 30.00
        elif car_category == '2':
            base_rate = 50.00
        elif car_category == '3':
            base_rate = 80.00
        else:
            print("Invalid category, assigning Eco.")
            base_rate = 30.00

        age_surcharge = 20.00 * days_rented if driver_age < 25 else 0.0
        insur_fee = 15.00 * days_rented if wants_insurance else 0.0
        total_cost = (base_rate * days_rented) + age_surcharge + insur_fee
        base_rate_total = base_rate * days_rented

        print("\n=================================")
        print(" RENTAL AGREEMENT")
        print("=================================")
        print(f"Renter: {customer_name}")
        print(f"Days:   {days_rented}")
        print(f"Base Rental:    ${base_rate_total:10.2f}")
        
        if age_surcharge > 0:
            print(f"Under 25 Fee:   ${age_surcharge:10.2f}")
            
        if insur_fee > 0:
            print(f"Insurance Addon:${insur_fee:10.2f}")
            
        print("---------------------------------")
        print(f"TOTAL CHARGE:   ${total_cost:10.2f}")
        print("=================================")

        repeat = input("New rental? (Y/N): ").strip().upper()
        if repeat not in ('Y', 'YES'):
            is_running = False

if __name__ == "__main__":
    main()
