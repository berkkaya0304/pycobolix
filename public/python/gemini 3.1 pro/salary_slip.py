def main():
    print("--- HR SALARY INVOICING ---")
    emp_name = input("Employee Name: ")
    emp_id = input("Employee ID: ")
    try:
        basic_pay = float(input("Basic Pay ($): "))
    except ValueError:
        basic_pay = 0.0

    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    transport = 150.00

    gross_salary = basic_pay + hra + da + transport

    pf = basic_pay * 0.12
    tax = gross_salary * 0.05
    medical = 50.00

    total_ded = pf + tax + medical
    net_pay = gross_salary - total_ded

    print("\n========================================")
    print("             PAY SLIP SUMMARY           ")
    print("========================================")
    print(f"Employee: {emp_name} (ID: {emp_id})")
    print("----------------------------------------")
    print("EARNINGS:")
    print(f"  Basic Pay:  ${basic_pay:10.2f}")
    print(f"  HRA (20%):  ${hra:10.2f}")
    print(f"  DA (10%):   ${da:10.2f}")
    print(f"  Transport:  ${transport:10.2f}")
    print("----------------------------------------")
    print(f"GROSS PAY:    ${gross_salary:10.2f}")
    print("----------------------------------------")
    print("DEDUCTIONS:")
    print(f"  PF (12% Base): ${pf:9.2f}")
    print(f"  Income Tax:    ${tax:9.2f}")
    print(f"  Medical Ins:   ${medical:9.2f}")
    print("----------------------------------------")
    print(f"TOTAL DEDUCT: ${total_ded:10.2f}")
    print("========================================")
    print(f"NET PAY (TAKE HOME): ${net_pay:10.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
