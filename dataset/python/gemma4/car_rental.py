import sys

def get_input(prompt):
    return input(prompt).strip()

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("### RAPID RENTALS ###")
    is_running = 'Y'

    while is_running.upper() == 'Y':
        # GET-INPUTS
        customer_name = get_input("Customer Name: ")
        car_category = get_input("Car Category (1=Eco $30, 2=Sedan $50, 3=SUV $80): ")
        try:
            days_rented = int(get_input("Rental Duration (Days): "))
            driver_age = int(get_input("Driver's Age: "))
        except ValueError:
            print("Invalid numeric input. Please enter numbers.")
            continue
            
        insurance_flag = get_input("Add Full Insurance ($15/day)? (Y/N): ").upper()

        # CALCULATIONS
        if car_category == '1':
            base_rate = 30.00
        elif car_category == '2':
            base_rate = 50.00
        elif car_category == '3':
            base_rate = 80.00
        else:
            print("Invalid category, assigning Eco.")
            base_rate = 30.00

        age_surcharge = 20.00 * days_rented if driver_age < 25 else 0.00
        insur_fee = 15.00 * days_rented if insurance_flag == 'Y' else 0.00
        
        total_cost = (base_rate * days_rented) + age_surcharge + insur_fee

        # PRINT-AGREEMENT
        print("\n=================================")
        print(" RENTAL AGREEMENT")
        print("=================================")
        print(f"Renter: {customer_name}")
        print(f"Days:   {days_rented}")
        
        rental_base_total = base_rate * days_rented
        print(f"Base Rental:    {format_currency(rental_base_total)}")
        
        if age_surcharge > 0:
            print(f"Under 25 Fee:   {format_currency(age_surcharge)}")
            
        if insur_fee > 0:
            print(f"Insurance Addon:{format_currency(insur_fee)}")
            
        print("---------------------------------")
        print(f"TOTAL CHARGE:   {format_currency(total_cost)}")
        print("=================================")

        is_running = get_input("New rental? (Y/N): ")

if __name__ == "__main__":
    main()
