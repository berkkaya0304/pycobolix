def main():
    print("--- PLATINUM AUTO SALES ---")

    buyer_name = input("Buyer Name: ").strip()
    base_model = int(input("Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): "))
    trim_level = int(input("Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): "))
    down_payment = float(input("Down Payment Amount ($): "))
    loan_months = int(input("Loan Term (Months): "))

    base_price, trim_upcharge = price_calc(base_model, trim_level)
    total_veh_price = base_price + trim_upcharge
    financed_amt, total_interest, total_payback, monthly_payment = finance_calc(
        total_veh_price, down_payment, loan_months
    )

    output_sheet(
        buyer_name,
        base_price,
        trim_upcharge,
        total_veh_price,
        down_payment,
        financed_amt,
        monthly_payment,
    )

def price_calc(base_model, trim_level):
    if base_model == 1:
        base_price = 25000.00
    elif base_model == 2:
        base_price = 35000.00
    elif base_model == 3:
        base_price = 45000.00
    else:
        base_price = 25000.00

    if trim_level == 1:
        trim_upcharge = 0.00
    elif trim_level == 2:
        trim_upcharge = 5000.00
    elif trim_level == 3:
        trim_upcharge = 10000.00
    else:
        trim_upcharge = 0.00

    return base_price, trim_upcharge

def finance_calc(total_veh_price, down_payment, loan_months):
    financed_amt = total_veh_price - down_payment
    interest_rate = 0.05
    total_interest = financed_amt * interest_rate * (loan_months / 12)
    total_payback = financed_amt + total_interest
    monthly_payment = total_payback / loan_months
    return financed_amt, total_interest, total_payback, monthly_payment

def output_sheet(
    buyer_name,
    base_price,
    trim_upcharge,
    total_veh_price,
    down_payment,
    financed_amt,
    monthly_payment,
):
    print()
    print("=" * 40)
    print("       VEHICLE PURCHASE SHEET           ")
    print("=" * 40)
    print(f"Buyer: {buyer_name}")
    print("-" * 40)
    print(f"Base Price:       ${base_price:,.2f}")
    print(f"Trim Upcharge:    ${trim_upcharge:,.2f}")
    print(f"Total Vehicle:    ${total_veh_price:,.2f}")
    print("-" * 40)
    print(f"Down Payment:    -${down_payment:,.2f}")
    print(f"Amount Financed:  ${financed_amt:,.2f}")
    print("-" * 40)
    print(f"EST. MONTHLY PMT: ${monthly_payment:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
