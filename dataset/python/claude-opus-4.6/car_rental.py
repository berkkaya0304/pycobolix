"""
Rapid Rentals - Car Rental System
Converted from COBOL (car_rental.cbl) to Python
"""


def main():
    print("### RAPID RENTALS ###")
    is_running = "Y"

    while is_running.upper() in ("Y",):
        # Get inputs
        customer_name = input("Customer Name: ")
        car_category = int(input("Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): "))
        days_rented = int(input("Rental Duration (Days): "))
        driver_age = int(input("Driver's Age: "))
        insurance_flag = input("Add Full Insurance ($15/day)? (Y/N): ").strip().upper()

        # Calculations
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
        insur_fee = 15.00 * days_rented if insurance_flag == "Y" else 0.0

        total_cost = (base_rate * days_rented) + age_surcharge + insur_fee
        base_rental_total = base_rate * days_rented

        # Print agreement
        print()
        print("=================================")
        print(" RENTAL AGREEMENT")
        print("=================================")
        print(f"Renter: {customer_name}")
        print(f"Days:   {days_rented}")
        print(f"Base Rental:    ${base_rental_total:>12,.2f}")
        if age_surcharge > 0:
            print(f"Under 25 Fee:   ${age_surcharge:>12,.2f}")
        if insur_fee > 0:
            print(f"Insurance Addon:${insur_fee:>12,.2f}")
        print("---------------------------------")
        print(f"TOTAL CHARGE:   ${total_cost:>12,.2f}")
        print("=================================")

        is_running = input("New rental? (Y/N): ").strip().upper()


if __name__ == "__main__":
    main()
