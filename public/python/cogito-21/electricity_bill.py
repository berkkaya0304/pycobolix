def format_currency(amount):
    return f"${amount:,.2f}"

def compute_bill(peak_kwh, off_peak_kwh, solar_credit):
    PEAK_RATE = 0.25
    OFF_PEAK_RATE = 0.12
    SOLAR_BUYBACK = 0.10
    
    peak_cost = peak_kwh * PEAK_RATE
    off_peak_cost = off_peak_kwh * OFF_PEAK_RATE
    sub_total = peak_cost + off_peak_cost
    
    solar_deduct = solar_credit * SOLAR_BUYBACK
    total_due = sub_total - solar_deduct
    
    return {
        'peak_cost': peak_cost,
        'off_peak_cost': off_peak_cost,
        'sub_total': sub_total,
        'solar_deduct': solar_deduct,
        'total_due': total_due
    }

def print_bill(account_id, peak_kwh, off_peak_kwh, solar_credit, bill_data):
    print("\n=========================================")
    print("        MONTHLY ELECTRIC STATEMENT       ")
    print("=========================================")
    print(f"Account No: {account_id}")
    print("-----------------------------------------")
    print(f"Peak Usage ({peak_kwh} kWh):     {format_currency(bill_data['peak_cost'])}")
    print(f"Off-Peak Usage ({off_peak_kwh} kWh): {format_currency(bill_data['off_peak_cost'])}")
    print("-----------------------------------------")
    print(f"Gross Energy Charge:      {format_currency(bill_data['sub_total'])}")
    print(f"Solar Credit ({solar_credit} kWh): -{format_currency(bill_data['solar_deduct'])}")
    print("-----------------------------------------")
    if bill_data['total_due'] < 0:
        print(f"CREDIT APPLIED TO ACCT:   {format_currency(abs(bill_data['total_due']))}")
    else:
        print(f"TOTAL CURRENT CHARGES:    {format_currency(bill_data['total_due'])}")
    print("=========================================")

def main():
    print("--- GRID-CONNECT ENERGY BILLING ---")
    account_id = input("Account ID: ")
    peak_kwh = float(input("Peak Hours Usage (kWh): "))
    off_peak_kwh = float(input("Off-Peak Hours Usage (kWh): "))
    solar_credit = float(input("Solar Generated Back to Grid (kWh): "))
    
    bill_data = compute_bill(peak_kwh, off_peak_kwh, solar_credit)
    print_bill(account_id, peak_kwh, off_peak_kwh, solar_credit, bill_data)

if __name__ == "__main__":
    main()
