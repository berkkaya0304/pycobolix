# CAR-DEALER - Platinum Auto Sales
# Converted from COBOL to Python

def main():
    INTEREST_RATE = 0.05

    print("--- PLATINUM AUTO SALES ---")
    buyer_name = input("Buyer Name: ")
    base_model = int(input("Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): "))
    trim_level = int(input("Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): "))
    down_payment = float(input("Down Payment Amount ($): "))
    loan_months = int(input("Loan Term (Months): "))

    # Price Calculation
    if base_model == 1:
        base_price = 25000.00
    elif base_model == 2:
        base_price = 35000.00
    elif base_model == 3:
        base_price = 45000.00
    else:
        base_price = 25000.00

    if trim_level == 1:
        trim_upcharge = 0.0
    elif trim_level == 2:
        trim_upcharge = 5000.00
    elif trim_level == 3:
        trim_upcharge = 10000.00
    else:
        trim_upcharge = 0.0

    total_veh_price = base_price + trim_upcharge

    # Finance Calculation
    financed_amt = total_veh_price - down_payment
    total_interest = financed_amt * INTEREST_RATE * (loan_months / 12)
    total_payback = financed_amt + total_interest
    monthly_payment = total_payback / loan_months

    print("")
    print("========================================")
    print("       VEHICLE PURCHASE SHEET           ")
    print("========================================")
    print(f"Buyer: {buyer_name}")
    print("----------------------------------------")
    print(f"Base Price:       ${base_price:,.2f}")
    print(f"Trim Upcharge:    ${trim_upcharge:,.2f}")
    print(f"Total Vehicle:    ${total_veh_price:,.2f}")
    print("----------------------------------------")
    print(f"Down Payment:    -${down_payment:,.2f}")
    print(f"Amount Financed:  ${financed_amt:,.2f}")
    print("----------------------------------------")
    print(f"EST. MONTHLY PMT: ${monthly_payment:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
