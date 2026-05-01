# TAX-CALCULATOR - Annual Income Tax Calculator
# Converted from COBOL to Python

def main():
    print("--- ANNUAL INCOME TAX CALCULATOR ---")
    full_name = input("Taxpayer Name: ")
    gross_income = float(input("Gross Annual Income ($): "))
    deductions = float(input("Itemized Deductions ($): "))
    dependents = int(input("Number of Dependents ($2000 credit each): "))

    taxable_income = gross_income - deductions
    if taxable_income < 0:
        taxable_income = 0.0

    if taxable_income <= 10000:
        tax_owed = taxable_income * 0.10
    elif taxable_income <= 40000:
        tax_owed = (10000 * 0.10) + ((taxable_income - 10000) * 0.12)
    elif taxable_income <= 85000:
        tax_owed = (10000 * 0.10) + (30000 * 0.12) + ((taxable_income - 40000) * 0.22)
    else:
        tax_owed = (10000 * 0.10) + (30000 * 0.12) + (45000 * 0.22) + ((taxable_income - 85000) * 0.24)

    dependent_ded = dependents * 2000.00
    tax_owed -= dependent_ded
    if tax_owed < 0:
        tax_owed = 0.0

    print("")
    print("========================================")
    print("        TAX RETURN ESTIMATE SUMMARY     ")
    print("========================================")
    print(f"Taxpayer: {full_name}")
    print("----------------------------------------")
    print(f"Gross Income:     ${gross_income:,.2f}")
    print(f"Deductions:      -${deductions:,.2f}")
    print(f"Taxable Income:   ${taxable_income:,.2f}")
    print("----------------------------------------")
    print(f"Dependent Credit:-${dependent_ded:,.2f}")
    print(f"TOTAL TAX OWED:   ${tax_owed:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
