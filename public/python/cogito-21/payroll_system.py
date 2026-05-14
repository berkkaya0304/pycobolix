class Employee:
    def __init__(self):
        self.emp_id = 0
        self.name = ""
        self.hourly_rate = 0.0
        self.hours_worked = 0
        self.overtime_hours = 0

def get_employee_data():
    emp = Employee()
    print("--- EMPLOYEE PAYROLL ENTRY ---")
    emp.emp_id = int(input("Enter Employee ID: "))
    emp.name = input("Enter Employee Name: ")
    emp.hourly_rate = float(input("Enter Hourly Rate: "))
    emp.hours_worked = int(input("Enter Hours Worked (Regular): "))
    emp.overtime_hours = int(input("Enter Overtime Hours: "))
    return emp

def calculate_pay(emp):
    TAX_RATE = 0.15
    OT_MULTIPLIER = 1.5
    
    regular_pay = emp.hourly_rate * emp.hours_worked
    overtime_pay = emp.hourly_rate * emp.overtime_hours * OT_MULTIPLIER
    gross_pay = regular_pay + overtime_pay
    tax_amount = gross_pay * TAX_RATE
    net_pay = gross_pay - tax_amount
    
    return {
        'regular_pay': regular_pay,
        'overtime_pay': overtime_pay,
        'gross_pay': gross_pay,
        'tax_amount': tax_amount,
        'net_pay': net_pay
    }

def display_results(emp, pay_data):
    print("---------------------------------")
    print(f"PAYROLL SUMMARY FOR: {emp.name}")
    print(f"ID: {emp.emp_id}")
    print(f"Gross Pay:   ${pay_data['gross_pay']:,.2f}")
    print(f"Tax Deduct:  ${pay_data['tax_amount']:,.2f}")
    print(f"Net Pay:     ${pay_data['net_pay']:,.2f}")
    print("---------------------------------")

def main():
    print("Payroll System")
    print("=============")
    
    while True:
        employee = get_employee_data()
        pay_data = calculate_pay(employee)
        display_results(employee, pay_data)
        
        continue_flag = input("Process another employee? (Y/N): ").strip().upper()
        if continue_flag != 'Y':
            break
    
    print("Exiting Payroll System.")

if __name__ == "__main__":
    main()
