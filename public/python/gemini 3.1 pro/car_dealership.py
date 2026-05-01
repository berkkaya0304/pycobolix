def main():
    print("--- PLATINUM AUTO SALES ---")
    buyer_name = input("Buyer Name: ")
    base_model = input("Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): ").strip()
    trim_level = input("Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): ").strip()
    try:
        down_payment = float(input("Down Payment Amount ($): "))
    except ValueError:
        down_payment = 0.0
    try:
        loan_months = int(input("Loan Term (Months): "))
    except ValueError:
        loan_months = 1

    if loan_months <= 0:
        loan_months = 1

    if base_model == '1':
        base_price = 25000.00
    elif base_model == '2':
        base_price = 35000.00
    elif base_model == '3':
        base_price = 45000.00
    else:
        base_price = 25000.00

    if trim_level == '1':
        trim_upcharge = 0.0
    elif trim_level == '2':
        trim_upcharge = 5000.00
    elif trim_level == '3':
        trim_upcharge = 10000.00
    else:
        trim_upcharge = 0.0

    total_veh_price = base_price + trim_upcharge

    financed_amt = total_veh_price - down_payment
    interest_rate = 0.05
    total_interest = financed_amt * interest_rate * (loan_months / 12)
    total_payback = financed_amt + total_interest
    monthly_payment = total_payback / loan_months

    print("\n========================================")
    print("       VEHICLE PURCHASE SHEET           ")
    print("========================================")
    print(f"Buyer: {buyer_name}")
    print("----------------------------------------")
    print(f"Base Price:       ${base_price:10.2f}")
    print(f"Trim Upcharge:    ${trim_upcharge:10.2f}")
    print(f"Total Vehicle:    ${total_veh_price:10.2f}")
    print("----------------------------------------")
    print(f"Down Payment:    -${down_payment:10.2f}")
    print(f"Amount Financed:  ${financed_amt:10.2f}")
    print("----------------------------------------")
    print(f"EST. MONTHLY PMT: ${monthly_payment:10.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
