from decimal import Decimal, ROUND_HALF_UP

def format_currency(value):
    """Formats a number to match the COBOL $Z,ZZZ,ZZ9.99 format."""
    return f"${value:,.2f}"

def calculate_salary(basic_pay):
    # Constants
    TRANSPORT = Decimal("150.00")
    MEDICAL = Decimal("50.00")
    
    # Earnings
    hra = basic_pay * Decimal("0.20")
    da = basic_pay * Decimal("0.10")
    gross_salary = basic_pay + hra + da + TRANSPORT
    
    # Deductions
    pf = basic_pay * Decimal("0.12")
    tax = gross_salary * Decimal("0.05")
    total_deductions = pf + tax + MEDICAL
    
    # Net Pay
    net_pay = gross_salary - total_deductions
    
    return {
        "basic_pay": basic_pay,
        "hra": hra,
        "da": da,
        "transport": TRANSPORT,
        "gross_salary": gross_salary,
        "pf": pf,
        "tax": tax,
        "medical": MEDICAL,
        "total_deductions": total_deductions,
        "net_pay": net_pay
    }

def print_payslip(emp_name, emp_id, data):
    print("\n========================================")
    print("             PAY SLIP SUMMARY           ")
    print("========================================")
    print(f"Employee: {emp_name} (ID: {emp_id})")
    print("----------------------------------------")
    print("EARNINGS:")
    print(f"  Basic Pay:  {format_currency(data['basic_pay'])}")
    print(f"  HRA (20%):  {format_currency(data['hra'])}")
    print(f"  DA (10%):   {format_currency(data['da'])}")
    print(f"  Transport:  {format_currency(data['transport'])}")
    print("----------------------------------------")
    print(f"GROSS PAY:    {format_currency(data['gross_salary'])}")
    print("----------------------------------------")
    print("DEDUCTIONS:")
    print(f"  PF (12% Base): {format_currency(data['pf'])}")
    print(f"  Income Tax:    {format_currency(data['tax'])}")
    print(f"  Medical Ins:   {format_currency(data['medical'])}")
    print("----------------------------------------")
    print(f"TOTAL DEDUCT: {format_currency(data['total_deductions'])}")
    print("========================================")
    print(f"NET PAY (TAKE HOME): {format_currency(data['net_pay'])}")
    print("========================================")

def main():
    print("--- HR SALARY INVOICING ---")
    emp_name = input("Employee Name: ")
    emp_id = input("Employee ID: ")
    try:
        basic_pay_input = input("Basic Pay ($): ")
        basic_pay = Decimal(basic_pay_input).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except Exception as e:
        print(f"Invalid input for Basic Pay: {e}")
        return

    salary_data = calculate_salary(basic_pay)
    print_payslip(emp_name, emp_id, salary_data)

if __name__ == "__main__":
    main()
