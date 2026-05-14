"""
Safe Drive Insurance Quote
Converted from COBOL (insurance_quote.cbl) to Python
"""


def main():
    base_premium = 500.00

    print("--- SAFE DRIVE INSURANCE QUOTE ---")
    d_name = input("Driver Name: ")
    d_age = int(input("Driver Age: "))
    accidents = int(input("Number of accidents in last 3 years: "))
    car_value = float(input("Current Vehicle Value ($): "))

    if d_age < 25:
        age_risk = 300.00
    elif d_age > 65:
        age_risk = 150.00
    else:
        age_risk = 0.0

    accident_risk = accidents * 250.00
    value_index = car_value * 0.015

    final_quote = base_premium + age_risk + accident_risk + value_index
    monthly_p = final_quote / 12

    print()
    print("=========================================")
    print("       COMPREHENSIVE AUTO POLICY         ")
    print("=========================================")
    print(f"Insured Name: {d_name} (Age: {d_age})")
    print(f"Vehicle Est: ${car_value:,.2f}")
    print("-----------------------------------------")
    print(f"Base Premium:       ${base_premium:>9,.2f}")
    print(f"Value Adjustment:  +${value_index:>9,.2f}")
    if age_risk > 0:
        print(f"Age Surcharge:     +${age_risk:>9,.2f}")
    if accident_risk > 0:
        print(f"Accident Penalty:  +${accident_risk:>9,.2f}")
    print("-----------------------------------------")
    print(f"ANNUAL PREMIUM:     ${final_quote:>9,.2f}")
    print(f"MONTHLY RATE:       ${monthly_p:>9,.2f}")
    print("=========================================")


if __name__ == "__main__":
    main()
