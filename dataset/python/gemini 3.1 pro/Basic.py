def main():
    ws_name = "Skye OSBOURNE"
    ws_gross_pay = 2500.50

    ws_emp_contrib = ws_gross_pay * 0.20
    ws_net_pay = ws_gross_pay - ws_emp_contrib

    print(f"Employe: {ws_name}")
    print(f"NET: {ws_net_pay:,.2f}")

if __name__ == "__main__":
    main()
