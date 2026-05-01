def main():
    print("--- SAFE DRIVE INSURANCE QUOTE ---")
    d_name = input("Driver Name: ")
    try:
        d_age = int(input("Driver Age: "))
    except ValueError:
        d_age = 0
    try:
        accidents = int(input("Number of accidents in last 3 years: "))
    except ValueError:
        accidents = 0
    try:
        car_value = float(input("Current Vehicle Value ($): "))
    except ValueError:
        car_value = 0.0

    base_premium = 500.00
    
    if d_age < 25:
        age_risk = 300.00
    elif d_age > 65:
        age_risk = 150.00
    else:
        age_risk = 0.0

    accident_risk = accidents * 250.00
    value_index = car_value * 0.015

    final_quote = base_premium + age_risk + accident_risk + value_index
    monthly_p = final_quote / 12.0

    print("\n=========================================")
    print("       COMPREHENSIVE AUTO POLICY         ")
    print("=========================================")
    print(f"Insured Name: {d_name} (Age: {d_age})")
    print(f"Vehicle Est: ${car_value:.2f}")
    print("-----------------------------------------")
    print(f"Base Premium:       ${base_premium:8.2f}")
    print(f"Value Adjustment:  +${value_index:8.2f}")
    
    if age_risk > 0:
        print(f"Age Surcharge:     +${age_risk:8.2f}")
    if accident_risk > 0:
        print(f"Accident Penalty:  +${accident_risk:8.2f}")
        
    print("-----------------------------------------")
    print(f"ANNUAL PREMIUM:     ${final_quote:8.2f}")
    print(f"MONTHLY RATE:       ${monthly_p:8.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
