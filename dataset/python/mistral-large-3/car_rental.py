def car_rental_system():
    print("### RAPID RENTALS ###")
    is_running = 'Y'

    while is_running.upper() == 'Y':
        customer_name = input("Customer Name: ").strip()
        try:
            car_category = int(input("Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): "))
            days_rented = int(input("Rental Duration (Days): "))
            driver_age = int(input("Driver's Age: "))
            insurance_flag = input("Add Full Insurance ($15/day)? (Y/N): ").strip().upper()
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")
            continue

        base_rate = 0.0
        if car_category == 1:
            base_rate = 30.00
        elif car_category == 2:
            base_rate = 50.00
        elif car_category == 3:
            base_rate = 80.00
        else:
            print("Invalid category, assigning Eco.")
            base_rate = 30.00

        age_surcharge = 20.00 * days_rented if driver_age < 25 else 0.0
        insur_fee = 15.00 * days_rented if insurance_flag == 'Y' else 0.0
        total_cost = (base_rate * days_rented) + age_surcharge + insur_fee

        print("\n=================================")
        print(" RENTAL AGREEMENT")
        print("=================================")
        print(f"Renter: {customer_name}")
        print(f"Days:   {days_rented}")
        print(f"Base Rental:    ${base_rate * days_rented:,.2f}")

        if age_surcharge > 0:
            print(f"Under 25 Fee:   ${age_surcharge:,.2f}")

        if insur_fee > 0:
            print(f"Insurance Addon: ${insur_fee:,.2f}")

        print("---------------------------------")
        print(f"TOTAL CHARGE:   ${total_cost:,.2f}")
        print("=================================")

        is_running = input("New rental? (Y/N): ").strip().upper()

if __name__ == "__main__":
    car_rental_system()
