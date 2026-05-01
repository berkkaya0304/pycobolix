# PAYROLL-SYSTEM - Employee Payroll System
# Converted from COBOL to Python

def main():
    TAX_RATE = 0.15
    OT_MULTIPLIER = 1.5

    continue_flag = 'Y'
    while continue_flag.upper() == 'Y':
        print("--- EMPLOYEE PAYROLL ENTRY ---")
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = int(input("Enter Hours Worked (Regular): "))
        overtime_hours = int(input("Enter Overtime Hours: "))

        regular_pay = hourly_rate * hours_worked
        overtime_pay = hourly_rate * overtime_hours * OT_MULTIPLIER
        gross_pay = regular_pay + overtime_pay
        tax_amount = gross_pay * TAX_RATE
        net_pay = gross_pay - tax_amount

        print("---------------------------------")
        print(f"PAYROLL SUMMARY FOR: {emp_name}")
        print(f"ID: {emp_id}")
        print(f"Gross Pay:   ${gross_pay:,.2f}")
        print(f"Tax Deduct:  ${tax_amount:,.2f}")
        print(f"Net Pay:     ${net_pay:,.2f}")
        print("---------------------------------")

        continue_flag = input("Process another employee? (Y/N): ").strip()

    print("Exiting Payroll System.")

if __name__ == "__main__":
    main()
