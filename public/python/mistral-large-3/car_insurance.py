def car_insurance():
    print("--- SAFE-DRIVE AUTO INSURANCE ---")
    driver_name = input("Driver Name: ").strip()
    driver_age = int(input("Driver Age: ").strip())
    print("Vehicle (1=Sedan, 2=Sports Car, 3=SUV): ")
    car_type = int(input().strip())
    prev_accidents = int(input("Number of Accidents in last 3 years: ").strip())

    base_premium = 600.00
    age_risk = 0.0
    car_risk = 0.0
    accident_risk = 0.0

    if driver_age < 25:
        age_risk = 300.00
    elif driver_age > 65:
        age_risk = 150.00

    if car_type == 1:
        car_risk = 50.00
    elif car_type == 2:
        car_risk = 400.00
    elif car_type == 3:
        car_risk = 120.00
    else:
        car_risk = 50.00

    if prev_accidents > 0:
        accident_risk = prev_accidents * 250.00

    total_annual = base_premium + age_risk + car_risk + accident_risk
    monthly_pay = total_annual / 12

    print("")
    print("========================================")
    print("         ANNUAL POLICY QUOTE            ")
    print("========================================")
    print(f"Driver: {driver_name}")
    print("----------------------------------------")
    print(f"Base Premium Rate:   ${base_premium:,.2f}")
    if age_risk > 0:
        print(f"Age Risk Factor:     ${age_risk:,.2f}")
    print(f"Vehicle Risk Class:  ${car_risk:,.2f}")
    if accident_risk > 0:
        print(f"Accident History:    ${accident_risk:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL ANNUAL COST:   ${total_annual:,.2f}")
    print(f"EST MONTHLY COST:    ${monthly_pay:,.2f}")
    print("========================================")

if __name__ == "__main__":
    car_insurance()
