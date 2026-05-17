def main():
    print("--- MORTGAGE CALCULATOR ---")
    prop_address = input("Property Address: ")
    try:
        prop_price = float(input("Property Purchase Price ($): "))
    except ValueError:
        prop_price = 0.0
    try:
        down_pmt_pct = float(input("Down Payment Percentage (e.g., 20 for 20%): "))
    except ValueError:
        down_pmt_pct = 0.0
    try:
        int_rate = float(input("Interest Rate (e.g., 5.5 for 5.5%): "))
    except ValueError:
        int_rate = 5.50
    try:
        loan_years = int(input("Loan Term (Years): "))
    except ValueError:
        loan_years = 30

    down_pmt_amt = prop_price * (down_pmt_pct / 100.0)
    loan_principal = prop_price - down_pmt_amt

    pmi_fee = 0.0
    if down_pmt_pct < 20.0:
        pmi_fee = (loan_principal * 0.01) / 12.0
        print("*** WARNING: PMI applies (Down Payment < 20%) ***")

    # Simplified flat interest calc for demonstration
    total_int = loan_principal * (int_rate / 100.0) * loan_years
    total_payback = loan_principal + total_int
    total_months = loan_years * 12
    
    if total_months > 0:
        monthly_pmt = (total_payback / total_months) + pmi_fee
    else:
        monthly_pmt = 0.0

    print("\n=============================================")
    print("        MORTGAGE BREAKDOWN ESTIMATE          ")
    print("=============================================")
    print(f"Address: {prop_address}")
    print("---------------------------------------------")
    print(f"Purchase Price:   ${prop_price:14.2f}")
    print(f"Down Payment:     -${down_pmt_amt:13.2f}")
    print(f"Loan Principal:   ${loan_principal:14.2f}")
    print("---------------------------------------------")
    print(f"Total Interest:   ${total_int:14.2f}")
    print(f"Total Repayment:  ${total_payback:14.2f}")
    print("---------------------------------------------")
    
    if pmi_fee > 0:
        print(f"Monthly PMI Fee:  ${pmi_fee:14.2f}")
        
    print(f"EST. MONTHLY PMT: ${monthly_pmt:14.2f}")
    print("=============================================")

if __name__ == "__main__":
    main()
