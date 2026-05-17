from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- PLATINUM AUTO SALES ---")
    
    buyer_name = input("Buyer Name: ")
    
    try:
        base_model = int(input("Model (1=Sedan $25k, 2=SUV $35k, 3=Truck $45k): "))
        trim_level = int(input("Trim (1=Base $0, 2=Sport $5k, 3=Luxury $10k): "))
        down_payment = Decimal(input("Down Payment Amount ($): "))
        loan_months = int(input("Loan Term (Months): "))
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return

    # Price Calculation
    if base_model == 1:
        base_price = Decimal("25000.00")
    elif base_model == 2:
        base_price = Decimal("35000.00")
    elif base_model == 3:
        base_price = Decimal("45000.00")
    else:
        base_price = Decimal("25000.00")

    if trim_level == 1:
        trim_upcharge = Decimal("0.00")
    elif trim_level == 2:
        trim_upcharge = Decimal("5000.00")
    elif trim_level == 3:
        trim_upcharge = Decimal("10000.00")
    else:
        trim_upcharge = Decimal("0.00")

    total_veh_price = base_price + trim_upcharge

    # Finance Calculation
    interest_rate = Decimal("0.05")
    financed_amt = total_veh_price - down_payment
    
    # Total Interest = Principal * Rate * (Months / 12)
    total_interest = financed_amt * interest_rate * (Decimal(loan_months) / Decimal("12"))
    total_payback = financed_amt + total_interest
    
    if loan_months > 0:
        monthly_payment = total_payback / Decimal(loan_months)
    else:
        monthly_payment = Decimal("0.00")

    # Output Sheet
    print("\n========================================")
    print("       VEHICLE PURCHASE SHEET           ")
    print("========================================")
    print(f"Buyer: {buyer_name}")
    print("----------------------------------------")
    print(f"Base Price:       {format_currency(base_price)}")
    print(f"Trim Upcharge:    {format_currency(trim_upcharge)}")
    print(f"Total Vehicle:    {format_currency(total_veh_price)}")
    print("----------------------------------------")
    print(f"Down Payment:    -{format_currency(down_payment)}")
    print(f"Amount Financed:  {format_currency(financed_amt)}")
    print("----------------------------------------")
    print(f"EST. MONTHLY PMT: {format_currency(monthly_payment)}")
    print("========================================")

if __name__ == "__main__":
    main()
