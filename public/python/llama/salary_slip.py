# SALARY-SLIP - HR Salary Invoicing
# Converted from COBOL to Python

def main():
    TRANSPORT = 150.00
    MEDICAL = 50.00

    print("--- HR SALARY INVOICING ---")
    emp_name = input("Employee Name: ")
    emp_id = input("Employee ID: ")
    basic_pay = float(input("Basic Pay ($): "))

    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    gross_salary = basic_pay + hra + da + TRANSPORT

    pf = basic_pay * 0.12
    tax = gross_salary * 0.05
    total_ded = pf + tax + MEDICAL
    net_pay = gross_salary - total_ded

    print("")
    print("========================================")
    print("             PAY SLIP SUMMARY           ")
    print("========================================")
    print(f"Employee: {emp_name} (ID: {emp_id})")
    print("----------------------------------------")
    print("EARNINGS:")
    print(f"  Basic Pay:  ${basic_pay:,.2f}")
    print(f"  HRA (20%):  ${hra:,.2f}")
    print(f"  DA (10%):   ${da:,.2f}")
    print(f"  Transport:  ${TRANSPORT:,.2f}")
    print("----------------------------------------")
    print(f"GROSS PAY:    ${gross_salary:,.2f}")
    print("----------------------------------------")
    print("DEDUCTIONS:")
    print(f"  PF (12% Base): ${pf:,.2f}")
    print(f"  Income Tax:    ${tax:,.2f}")
    print(f"  Medical Ins:   ${MEDICAL:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL DEDUCT: ${total_ded:,.2f}")
    print("========================================")
    print(f"NET PAY (TAKE HOME): ${net_pay:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
