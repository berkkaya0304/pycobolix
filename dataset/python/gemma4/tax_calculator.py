import decimal

def calculate_tax():
    print("--- ANNUAL INCOME TAX CALCULATOR ---")
    
    full_name = input("Taxpayer Name: ")
    try:
        gross_income = decimal.Decimal(input("Gross Annual Income ($): "))
        deductions = decimal.Decimal(input("Itemized Deductions ($): "))
        dependents = int(input("Number of Dependents ($2000 credit each): "))
    except (decimal.InvalidOperation, ValueError):
        print("Invalid numeric input. Please restart and enter valid numbers.")
        return

    # Calculate Taxable Income
    taxable_income = gross_income - deductions
    if taxable_income < 0:
        taxable_income = decimal.Decimal('0.00')

    # Calculate Tax Owed based on brackets
    if taxable_income <= 10000:
        tax_owed = taxable_income * decimal.Decimal('0.10')
    elif taxable_income <= 40000:
        tax_owed = (decimal.Decimal('10000') * decimal.Decimal('0.10')) + \
                   ((taxable_income - 10000) * decimal.Decimal('0.12'))
    elif taxable_income <= 85000:
        tax_owed = (decimal.Decimal('10000') * decimal.Decimal('0.10')) + \
                   (decimal.Decimal('30000') * decimal.Decimal('0.12')) + \
                   ((taxable_income - 40000) * decimal.Decimal('0.22'))
    else:
        tax_owed = (decimal.Decimal('10000') * decimal.Decimal('0.10')) + \
                   (decimal.Decimal('30000') * decimal.Decimal('0.12')) + \
                   (decimal.Decimal('45000') * decimal.Decimal('0.22')) + \
                   ((taxable_income - 85000) * decimal.Decimal('0.24'))

    # Apply Dependent Credits
    dependent_ded = dependents * decimal.Decimal('2000.00')
    tax_owed -= dependent_ded
    
    if tax_owed < 0:
        tax_owed = decimal.Decimal('0.00')

    # Formatting helper for currency
    def fmt_val(val):
        return f"${val:,.2f}"

    print("\n========================================")
    print("        TAX RETURN ESTIMATE SUMMARY     ")
    print("========================================")
    print(f"Taxpayer: {full_name}")
    print("----------------------------------------")
    print(f"Gross Income:     {fmt_val(gross_income)}")
    print(f"Deductions:      -{fmt_val(deductions)}")
    print(f"Taxable Income:   {fmt_val(taxable_income)}")
    print("----------------------------------------")
    print(f"Dependent Credit:-{fmt_val(dependent_ded)}")
    print(f"TOTAL TAX OWED:   {fmt_val(tax_owed)}")
    print("========================================")

if __name__ == "__main__":
    calculate_tax()
