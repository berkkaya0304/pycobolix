from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    """Simulates the COBOL PIC -$Z,ZZZ,ZZ9.99 format."""
    return f"{amount:,.2f}"

def main():
    # Constants (Rates)
    PEAK_RATE = Decimal("0.25")
    OFF_PEAK_RATE = Decimal("0.12")
    SOLAR_BUYBACK = Decimal("0.10")

    print("--- GRID-CONNECT ENERGY BILLING ---")
    
    # Input Section
    account_id = input("Account ID: ").strip()
    try:
        peak_kwh = Decimal(input("Peak Hours Usage (kWh): ") or "0")
        off_peak_kwh = Decimal(input("Off-Peak Hours Usage (kWh): ") or "0")
        solar_credit = Decimal(input("Solar Generated Back to Grid (kWh): ") or "0")
    except Exception as e:
        print(f"Invalid input: {e}")
        return

    # Compute Bill
    peak_cost = (peak_kwh * PEAK_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    off_peak_cost = (off_peak_kwh * OFF_PEAK_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    sub_total = peak_cost + off_peak_cost
    
    solar_deduct = (solar_credit * SOLAR_BUYBACK).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total_due = sub_total - solar_deduct

    # Print Bill
    print("\n=========================================")
    print("        MONTHLY ELECTRIC STATEMENT       ")
    print("=========================================")
    print(f"Account No: {account_id}")
    print("-----------------------------------------")
    print(f"Peak Usage ({peak_kwh} kWh):     {format_currency(peak_cost)}")
    print(f"Off-Peak Usage ({off_peak_kwh} kWh): {format_currency(off_peak_cost)}")
    print("-----------------------------------------")
    print(f"Gross Energy Charge:      {format_currency(sub_total)}")
    print(f"Solar Credit ({solar_credit} kWh): -{format_currency(solar_deduct)}")
    print("-----------------------------------------")
    
    if total_due < 0:
        print(f"CREDIT APPLIED TO ACCT:   {format_currency(total_due)}")
    else:
        print(f"TOTAL CURRENT CHARGES:    {format_currency(total_due)}")
    print("=========================================")

if __name__ == "__main__":
    main()
