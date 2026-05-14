from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- MORTGAGE CALCULATOR ---")
    
    prop_address = input("Property Address: ")
    prop_price = Decimal(input("Property Purchase Price ($): "))
    down_pmt_pct = Decimal(input("Down Payment Percentage (e.g., 20 for 20%): "))
    int_rate = Decimal(input("Interest Rate (e.g., 5.5 for 5.5%): "))
    loan_years = int(input("Loan Term (Years): "))

    # Process Loan
    down_pmt_amt = prop_price * (down_pmt_pct / 100)
    loan_principal = prop_price - down_pmt_amt
    
    pmi_fee = Decimal('0.00')
    if down_pmt_pct < 20:
        pmi_fee = (loan_principal * Decimal('0.01')) / 12
        print("*** WARNING: PMI applies (Down Payment < 20%) ***")

    # Simplified flat interest calculation as per COBOL logic
    total_int = loan_principal * (int_rate / 100) * loan_years
    total_payback = loan_principal + total_int
    total_months = loan_years * 12
    
    monthly_pmt = (total_payback / total_months) + pmi_fee

    # Print Breakdown
    print("\n=============================================")
    print("        MORTGAGE BREAKDOWN ESTIMATE          ")
    print("=============================================")
    print(f"Address: {prop_address}")
    print("---------------------------------------------")
    print(f"Purchase Price:   {format_currency(prop_price)}")
    print(f"Down Payment:     -{format_currency(down_pmt_amt)}")
    print(f"Loan Principal:   {format_currency(loan_principal)}")
    print("---------------------------------------------")
    print(f"Total Interest:   {format_currency(total_int)}")
    print(f"Total Repayment:  {format_currency(total_payback)}")
    print("---------------------------------------------")
    
    if pmi_fee > 0:
        print(f"Monthly PMI Fee:  {format_currency(pmi_fee)}")
        
    print(f"EST. MONTHLY PMT: {format_currency(monthly_pmt)}")
    print("=============================================")

if __name__ == "__main__":
    main()
