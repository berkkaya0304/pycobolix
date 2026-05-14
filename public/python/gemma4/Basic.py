from decimal import Decimal, ROUND_HALF_UP

def main():
    # Data Initialization
    ws_name = "Skye OSBOURNE"
    ws_gross_pay = Decimal("2500.50")
    
    # Calculations
    ws_emp_contrib = ws_gross_pay * Decimal("0.20")
    ws_net_pay = ws_gross_pay - ws_emp_contrib
    
    # Formatting (Z,ZZZ.99 equivalent: comma thousands separator, 2 decimal places)
    ws_net_pay_ed = f"{ws_net_pay:,.2f}"
    
    # Output
    print(f"Employe: {ws_name}")
    print(f"NET: {ws_net_pay_ed}")

if __name__ == "__main__":
    main()
