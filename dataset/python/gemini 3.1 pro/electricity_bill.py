def main():
    print("--- GRID-CONNECT ENERGY BILLING ---")
    account_id = input("Account ID: ")
    try:
        peak_kwh = float(input("Peak Hours Usage (kWh): "))
    except ValueError:
        peak_kwh = 0.0
    try:
        off_peak_kwh = float(input("Off-Peak Hours Usage (kWh): "))
    except ValueError:
        off_peak_kwh = 0.0
    try:
        solar_credit = float(input("Solar Generated Back to Grid (kWh): "))
    except ValueError:
        solar_credit = 0.0

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
    print(f"Peak Usage ({int(peak_kwh)} kWh):     ${peak_cost:11.2f}")
    print(f"Off-Peak Usage ({int(off_peak_kwh)} kWh): ${off_peak_cost:11.2f}")
    print("-----------------------------------------")
    print(f"Gross Energy Charge:      ${sub_total:11.2f}")
    print(f"Solar Credit ({int(solar_credit)} kWh): -${solar_deduct:11.2f}")
    print("-----------------------------------------")
    
    if total_due < 0:
        print(f"CREDIT APPLIED TO ACCT:   -${abs(total_due):11.2f}")
    else:
        print(f"TOTAL CURRENT CHARGES:    ${total_due:11.2f}")
        
    print("=========================================")

if __name__ == "__main__":
    main()
