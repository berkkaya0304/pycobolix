"""
Employee Payroll System
Converted from COBOL (payroll_system.cbl) to Python
"""


def main():
    tax_rate = 0.15
    ot_multiplier = 1.5
    continue_flag = "Y"

    while continue_flag.upper() == "Y":
        print("--- EMPLOYEE PAYROLL ENTRY ---")
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = float(input("Enter Hours Worked (Regular): "))
        overtime_hours = float(input("Enter Overtime Hours: "))

        regular_pay = hourly_rate * hours_worked
        overtime_pay = hourly_rate * overtime_hours * ot_multiplier
        gross_pay = regular_pay + overtime_pay
        tax_amount = gross_pay * tax_rate
        net_pay = gross_pay - tax_amount

        print("---------------------------------")
        print(f"PAYROLL SUMMARY FOR: {emp_name}")
        print(f"ID: {emp_id}")
        print(f"Gross Pay:   ${gross_pay:>12,.2f}")
        print(f"Tax Deduct:  ${tax_amount:>12,.2f}")
        print(f"Net Pay:     ${net_pay:>12,.2f}")
        print("---------------------------------")

        continue_flag = input("Process another employee? (Y/N): ").strip().upper()

    print("Exiting Payroll System.")


if __name__ == "__main__":
    main()
