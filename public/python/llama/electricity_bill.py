# ELECTRIC-BILL - Grid-Connect Energy Billing
# Converted from COBOL to Python

def main():
    PEAK_RATE = 0.25
    OFF_PEAK_RATE = 0.12
    SOLAR_BUYBACK = 0.10

    print("--- GRID-CONNECT ENERGY BILLING ---")
    account_id = input("Account ID: ")
    peak_kwh = int(input("Peak Hours Usage (kWh): "))
    off_peak_kwh = int(input("Off-Peak Hours Usage (kWh): "))
    solar_credit = int(input("Solar Generated Back to Grid (kWh): "))

    peak_cost = peak_kwh * PEAK_RATE
    off_peak_cost = off_peak_kwh * OFF_PEAK_RATE
    sub_total = peak_cost + off_peak_cost
    solar_deduct = solar_credit * SOLAR_BUYBACK
    total_due = sub_total - solar_deduct

    print("")
    print("=========================================")
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
        print(f"CREDIT APPLIED TO ACCT:   ${abs(total_due):,.2f}")
    else:
        print(f"TOTAL CURRENT CHARGES:    ${total_due:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
