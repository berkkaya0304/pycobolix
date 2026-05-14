def main():
    print("--- ANNUAL INCOME TAX CALCULATOR ---")
    full_name = input("Taxpayer Name: ")
    gross_income = float(input("Gross Annual Income ($): "))
    deductions = float(input("Itemized Deductions ($): "))
    dependents = int(input("Number of Dependents ($2000 credit each): "))

    taxable_income, dependent_ded, tax_owed = calculate_tax(gross_income, deductions, dependents)
    display_return(full_name, gross_income, deductions, taxable_income, dependent_ded, tax_owed)

def calculate_tax(gross_income, deductions, dependents):
    taxable_income = max(gross_income - deductions, 0)

    if taxable_income <= 10000:
        tax_owed = taxable_income * 0.10
    elif taxable_income <= 40000:
        tax_owed = (10000 * 0.10) + ((taxable_income - 10000) * 0.12)
    elif taxable_income <= 85000:
        tax_owed = (10000 * 0.10) + (30000 * 0.12) + ((taxable_income - 40000) * 0.22)
    else:
        tax_owed = (10000 * 0.10) + (30000 * 0.12) + (45000 * 0.22) + ((taxable_income - 85000) * 0.24)

    dependent_ded = dependents * 2000.00
    tax_owed = max(tax_owed - dependent_ded, 0)

    return taxable_income, dependent_ded, tax_owed

def display_return(full_name, gross_income, deductions, taxable_income, dependent_ded, tax_owed):
    def format_currency(value):
        return f"${value:,.2f}"

    print("\n========================================")
    print("        TAX RETURN ESTIMATE SUMMARY     ")
    print("========================================")
    print(f"Taxpayer: {full_name}")
    print("----------------------------------------")
    print(f"Gross Income:     {format_currency(gross_income)}")
    print(f"Deductions:      -{format_currency(deductions)}")
    print(f"Taxable Income:   {format_currency(taxable_income)}")
    print("----------------------------------------")
    print(f"Dependent Credit:-{format_currency(dependent_ded)}")
    print(f"TOTAL TAX OWED:   {format_currency(tax_owed)}")
    print("========================================")

if __name__ == "__main__":
    main()
