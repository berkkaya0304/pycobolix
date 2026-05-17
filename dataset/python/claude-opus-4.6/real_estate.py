"""
Mortgage Calculator - Real Estate
Converted from COBOL (real_estate.cbl) to Python
"""


def main():
    print("--- MORTGAGE CALCULATOR ---")
    prop_address = input("Property Address: ")
    prop_price = float(input("Property Purchase Price ($): "))
    down_pmt_pct = float(input("Down Payment Percentage (e.g., 20 for 20%): "))
    int_rate = float(input("Interest Rate (e.g., 5.5 for 5.5%): "))
    loan_years = int(input("Loan Term (Years): "))

    down_pmt_amt = prop_price * (down_pmt_pct / 100)
    loan_principal = prop_price - down_pmt_amt

    pmi_fee = 0.0
    if down_pmt_pct < 20:
        pmi_fee = (loan_principal * 0.01) / 12
        print("*** WARNING: PMI applies (Down Payment < 20%) ***")

    total_int = loan_principal * (int_rate / 100) * loan_years
    total_payback = loan_principal + total_int
    total_months = loan_years * 12
    monthly_pmt = (total_payback / total_months) + pmi_fee

    print()
    print("=============================================")
    print("        MORTGAGE BREAKDOWN ESTIMATE          ")
    print("=============================================")
    print(f"Address: {prop_address}")
    print("---------------------------------------------")
    print(f"Purchase Price:   ${prop_price:>16,.2f}")
    print(f"Down Payment:     -${down_pmt_amt:>15,.2f}")
    print(f"Loan Principal:   ${loan_principal:>16,.2f}")
    print("---------------------------------------------")
    print(f"Total Interest:   ${total_int:>16,.2f}")
    print(f"Total Repayment:  ${total_payback:>16,.2f}")
    print("---------------------------------------------")
    if pmi_fee > 0:
        print(f"Monthly PMI Fee:  ${pmi_fee:>16,.2f}")
    print(f"EST. MONTHLY PMT: ${monthly_pmt:>16,.2f}")
    print("=============================================")


if __name__ == "__main__":
    main()
