def calculate_charges(elec_kwh, water_gal, incl_late):
    elec_base = 20.00
    water_base = 15.00
    late_fee_amount = 10.00

    if elec_kwh <= 500:
        elec_chg = elec_kwh * 0.12
    else:
        elec_chg = (500 * 0.12) + ((elec_kwh - 500) * 0.15)

    water_chg = (water_gal / 100) * 0.25
    total_chg = elec_base + elec_chg + water_base + water_chg

    applied_late_fee = 0.0
    if incl_late.upper() == 'Y':
        applied_late_fee = late_fee_amount
    
    final_due = total_chg + applied_late_fee

    return {
        "elec_base": elec_base,
        "elec_chg": elec_chg,
        "water_base": water_base,
        "water_chg": water_chg,
        "late_fee": applied_late_fee,
        "final_due": final_due
    }

def main():
    print("--- CITY UTILITIES BILLING ---")
    
    try:
        acct_num = input("Account Number: ")
        cust_name = input("Customer Name: ")
        elec_kwh = int(input("Electricity Used (kWh): "))
        water_gal = int(input("Water Used (Gallons): "))
        incl_late = input("Apply late fee? (Y/N): ")
    except ValueError:
        print("Invalid input. Please enter numeric values for usage.")
        return

    results = calculate_charges(elec_kwh, water_gal, incl_late)

    print("\n****************************************")
    print("        MONTHLY UTILITY BILL            ")
    print("****************************************")
    print(f"Account: {acct_num}")
    print(f"Name:    {cust_name}")
    print("----------------------------------------")
    print(f"ELEC Base Fee:       ${results['elec_base']:>8.2f}")
    print(f"ELEC Usage Charge:   ${results['elec_chg']:>8.2f}")
    print(f"  (Usage: {elec_kwh} kWh)")
    print("----------------------------------------")
    print(f"WATER Base Fee:      ${results['water_base']:>8.2f}")
    print(f"WATER Usage Charge:  ${results['water_chg']:>8.2f}")
    print(f"  (Usage: {water_gal} gals)")
    print("----------------------------------------")
    
    if results['late_fee'] > 0:
        print(f"Prior Bal Late Fee:  ${results['late_fee']:>8.2f}")
    
    print(f"TOTAL AMOUNT DUE:    ${results['final_due']:>8.2f}")
    print("****************************************")

if __name__ == "__main__":
    main()
