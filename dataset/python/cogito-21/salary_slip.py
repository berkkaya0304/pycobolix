def main():
    print("--- HR SALARY INVOICING ---")
    emp_name = input("Employee Name: ")
    emp_id = input("Employee ID: ")
    basic_pay = float(input("Basic Pay ($): "))

    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    transport = 150.00
    gross_salary = basic_pay + hra + da + transport

    pf = basic_pay * 0.12
    tax = gross_salary * 0.05
    medical = 50.00
    total_ded = pf + tax + medical

    net_pay = gross_salary - total_ded

    print("\n" + "=" * 40)
    print("             PAY SLIP SUMMARY           ")
    print("=" * 40)
    print(f"Employee: {emp_name} (ID: {emp_id})")
    print("-" * 40)
    print("EARNINGS:")
    print(f"  Basic Pay:  ${basic_pay:,.2f}")
    print(f"  HRA (20%):  ${hra:,.2f}")
    print(f"  DA (10%):   ${da:,.2f}")
    print(f"  Transport:  ${transport:,.2f}")
    print("-" * 40)
    print(f"GROSS PAY:    ${gross_salary:,.2f}")
    print("-" * 40)
    print("DEDUCTIONS:")
    print(f"  PF (12% Base): ${pf:,.2f}")
    print(f"  Income Tax:    ${tax:,.2f}")
    print(f"  Medical Ins:   ${medical:,.2f}")
    print("-" * 40)
    print(f"TOTAL DEDUCT: ${total_ded:,.2f}")
    print("=" * 40)
    print(f"NET PAY (TAKE HOME): ${net_pay:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
