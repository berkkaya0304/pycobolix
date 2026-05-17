def main():
    print("--- GRID-CONNECT ENERGY BILLING ---")
    account_id = input("Account ID: ")
    peak_kwh = int(input("Peak Hours Usage (kWh): "))
    off_peak_kwh = int(input("Off-Peak Hours Usage (kWh): "))
    solar_credit = int(input("Solar Generated Back to Grid (kWh): "))

    peak_rate = 0.25
    off_peak_rate = 0.12
    solar_buyback = 0.10

    peak_cost = peak_kwh * peak_rate
    off_peak_cost = off_peak_kwh * off_peak_rate
    sub_total = peak_cost + off_peak_cost
    solar_deduct = solar_credit * solar_buyback
    total_due = sub_total - solar_deduct

    print("\n=========================================")
    print("        MONTHLY ELECTRIC STATEMENT       ")
    print("=========================================")
    print(f"Account No: {account_id}")
    print("-----------------------------------------")
    print(f"Peak Usage ({peak_kwh} kWh):     ${peak_cost:,.2f}")
    print(f"Off-Peak Usage ({off_peak_kwh} kWh): ${off_peak_cost:,.2f}")
    print("-----------------------------------------")
    print(f"Gross Energy Charge:      ${sub_total:,.2f}")
    print(f"Solar Credit ({solar_credit} kWh): -${solar_deduct:,.2f}")
    print("-----------------------------------------")
    if total_due < 0:
        print(f"CREDIT APPLIED TO ACCT:   ${total_due:,.2f}")
    else:
        print(f"TOTAL CURRENT CHARGES:    ${total_due:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
