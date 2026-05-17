def utility_bill():
    print("--- CITY UTILITIES BILLING ---")

    # Get account information
    acct_num = input("Account Number: ").strip()
    cust_name = input("Customer Name: ").strip()
    elec_kwh = int(input("Electricity Used (kWh): ").strip())
    water_gal = int(input("Water Used (Gallons): ").strip())
    incl_late = input("Apply late fee? (Y/N): ").strip().upper()

    # Calculate charges
    elec_base = 20.00
    if elec_kwh <= 500:
        elec_chg = elec_kwh * 0.12
    else:
        elec_chg = (500 * 0.12) + ((elec_kwh - 500) * 0.15)

    water_base = 15.00
    water_chg = (water_gal / 100) * 0.25

    total_chg = elec_base + elec_chg + water_base + water_chg

    late_fee = 10.00 if incl_late == 'Y' else 0.00
    final_due = total_chg + late_fee

    # Output invoice
    print("\n****************************************")
    print("        MONTHLY UTILITY BILL            ")
    print("****************************************")
    print(f"Account: {acct_num}")
    print(f"Name:    {cust_name}")
    print("----------------------------------------")
    print(f"ELEC Base Fee:       ${elec_base:,.2f}")
    print(f"ELEC Usage Charge:   ${elec_chg:,.2f}")
    print(f"  (Usage: {elec_kwh} kWh)")
    print("----------------------------------------")
    print(f"WATER Base Fee:      ${water_base:,.2f}")
    print(f"WATER Usage Charge:  ${water_chg:,.2f}")
    print(f"  (Usage: {water_gal} gals)")
    print("----------------------------------------")

    if late_fee > 0:
        print(f"Prior Bal Late Fee:  ${late_fee:,.2f}")

    print(f"TOTAL AMOUNT DUE:    ${final_due:,.2f}")
    print("****************************************")

if __name__ == "__main__":
    utility_bill()
