def format_currency(amount):
    return f"${amount:,.2f}"

def get_valid_input(prompt, input_type, valid_range=None):
    while True:
        try:
            value = input_type(input(prompt))
            if valid_range:
                if value not in valid_range:
                    print(f"Please enter a value between {valid_range[0]} and {valid_range[-1]}")
                    continue
            return value
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    print("--- SAFE-DRIVE AUTO INSURANCE ---")
    
    driver_name = input("Driver Name: ")
    
    driver_age = get_valid_input("Driver Age: ", int)
    
    print("Vehicle (1=Sedan, 2=Sports Car, 3=SUV): ")
    car_type = get_valid_input("", int, [1, 2, 3])
    
    prev_accidents = get_valid_input("Number of Accidents in last 3 years: ", int)
    
    base_premium = 600.00
    age_risk = 0.0
    car_risk = 0.0
    accident_risk = 0.0
    
    if driver_age < 25:
        age_risk = 300.00
    elif driver_age > 65:
        age_risk = 150.00
    
    if car_type == 1:    # Sedan
        car_risk = 50.00
    elif car_type == 2:  # Sports
        car_risk = 400.00
    elif car_type == 3:  # SUV
        car_risk = 120.00
    
    accident_risk = prev_accidents * 250.00
    
    total_annual = base_premium + age_risk + car_risk + accident_risk
    monthly_pay = total_annual / 12
    
    print("\n" + "=" * 40)
    print("         ANNUAL POLICY QUOTE            ")
    print("=" * 40)
    print(f"Driver: {driver_name}")
    print("-" * 40)
    print(f"Base Premium Rate:  {format_currency(base_premium)}")
    
    if age_risk > 0:
        print(f"Age Risk Factor:    {format_currency(age_risk)}")
    
    print(f"Vehicle Risk Class: {format_currency(car_risk)}")
    
    if accident_risk > 0:
        print(f"Accident History:   {format_currency(accident_risk)}")
    
    print("-" * 40)
    print(f"TOTAL ANNUAL COST:  {format_currency(total_annual)}")
    print(f"EST MONTHLY COST:   {format_currency(monthly_pay)}")
    print("=" * 40)

if __name__ == "__main__":
    main()
