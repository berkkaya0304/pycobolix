def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- SAFE DRIVE INSURANCE QUOTE ---")
    driver_name = input("Driver Name: ")
    driver_age = int(input("Driver Age: "))
    accidents = int(input("Number of accidents in last 3 years: "))
    car_value = float(input("Current Vehicle Value ($): "))

    base_premium = 500.00
    age_risk = 0.0
    accident_risk = 0.0
    value_index = 0.0

    if driver_age < 25:
        age_risk = 300.00
    elif driver_age > 65:
        age_risk = 150.00

    accident_risk = accidents * 250.00
    value_index = car_value * 0.015

    final_quote = base_premium + age_risk + accident_risk + value_index
    monthly_payment = final_quote / 12

    print("\n=========================================")
    print("       COMPREHENSIVE AUTO POLICY         ")
    print("=========================================")
    print(f"Insured Name: {driver_name} (Age: {driver_age})")
    print(f"Vehicle Est: {format_currency(car_value)}")
    print("-----------------------------------------")
    print(f"Base Premium:       {format_currency(base_premium)}")
    print(f"Value Adjustment:  +{format_currency(value_index)}")
    if age_risk > 0:
        print(f"Age Surcharge:     +{format_currency(age_risk)}")
    if accident_risk > 0:
        print(f"Accident Penalty:  +{format_currency(accident_risk)}")
    print("-----------------------------------------")
    print(f"ANNUAL PREMIUM:     {format_currency(final_quote)}")
    print(f"MONTHLY RATE:       {format_currency(monthly_payment)}")
    print("=========================================")

if __name__ == "__main__":
    main()
