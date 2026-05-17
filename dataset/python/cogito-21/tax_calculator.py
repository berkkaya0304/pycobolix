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
        tax_owed = 1000 + (taxable_income - 10000) * 0.12
    elif taxable_income <= 85000:
        tax_owed = 4600 + (taxable_income - 40000) * 0.22
    else:
        tax_owed = 14500 + (taxable_income - 85000) * 0.24

    dependent_ded = dependents * 2000.0
    tax_owed -= dependent_ded
    if tax_owed < 0:
        tax_owed = 0.0

    print("\n" + "=" * 40)
    print("        TAX RETURN ESTIMATE SUMMARY     ")
    print("=" * 40)
    print(f"Taxpayer: {full_name}")
    print("-" * 40)
    print(f"Gross Income:     ${gross_income:,.2f}")
    print(f"Deductions:      -${deductions:,.2f}")
    print(f"Taxable Income:   ${taxable_income:,.2f}")
    print("-" * 40)
    print(f"Dependent Credit:-${dependent_ded:,.2f}")
    print(f"TOTAL TAX OWED:   ${tax_owed:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
