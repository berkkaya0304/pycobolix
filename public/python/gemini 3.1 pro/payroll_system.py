def main():
    continue_flag = 'Y'

    while continue_flag in ('Y', 'y'):
        print("--- EMPLOYEE PAYROLL ENTRY ---")
        try:
            emp_id = int(input("Enter Employee ID: "))
        except ValueError:
            emp_id = 0
            
        emp_name = input("Enter Employee Name: ")
        
        try:
            hourly_rate = float(input("Enter Hourly Rate: "))
        except ValueError:
            hourly_rate = 0.0
            
        try:
            hours_worked = int(input("Enter Hours Worked (Regular): "))
        except ValueError:
            hours_worked = 0
            
        try:
            overtime_hours = int(input("Enter Overtime Hours: "))
        except ValueError:
            overtime_hours = 0

        tax_rate = 0.15
        ot_multiplier = 1.5

        regular_pay = hourly_rate * hours_worked
        overtime_pay = hourly_rate * overtime_hours * ot_multiplier
        gross_pay = regular_pay + overtime_pay
        tax_amount = gross_pay * tax_rate
        net_pay = gross_pay - tax_amount

        print("---------------------------------")
        print(f"PAYROLL SUMMARY FOR: {emp_name}")
        print(f"ID: {emp_id:05d}")
        print(f"Gross Pay:   ${gross_pay:10.2f}")
        print(f"Tax Deduct:  ${tax_amount:10.2f}")
        print(f"Net Pay:     ${net_pay:10.2f}")
        print("---------------------------------")

        continue_flag = input("Process another employee? (Y/N): ").strip()
        
    print("Exiting Payroll System.")

if __name__ == "__main__":
    main()
