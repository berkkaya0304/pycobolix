def main():
    print("--- CITY UTILITIES BILLING ---")
    try:
        acct_num = int(input("Account Number: "))
    except ValueError:
        acct_num = 0
    cust_name = input("Customer Name: ")
    try:
        elec_kwh = int(input("Electricity Used (kWh): "))
    except ValueError:
        elec_kwh = 0
    try:
        water_gal = int(input("Water Used (Gallons): "))
    except ValueError:
        water_gal = 0
    incl_late = input("Apply late fee? (Y/N): ").strip().upper() == 'Y'

    elec_base = 20.00
    water_base = 15.00
    late_fee = 10.00 if incl_late else 0.0

    if elec_kwh <= 500:
        elec_chg = elec_kwh * 0.12
    else:
        elec_chg = (500 * 0.12) + ((elec_kwh - 500) * 0.15)

    water_chg = (water_gal / 100.0) * 0.25

    total_chg = elec_base + elec_chg + water_base + water_chg
    final_due = total_chg + late_fee

    print("\n****************************************")
    print("        MONTHLY UTILITY BILL            ")
    print("****************************************")
    print(f"Account: {acct_num:08d}")
    print(f"Name:    {cust_name}")
    print("----------------------------------------")
    print(f"ELEC Base Fee:       ${elec_base:9.2f}")
    print(f"ELEC Usage Charge:   ${elec_chg:9.2f}")
    print(f"  (Usage: {elec_kwh:05d} kWh)")
    print("----------------------------------------")
    print(f"WATER Base Fee:      ${water_base:9.2f}")
    print(f"WATER Usage Charge:  ${water_chg:9.2f}")
    print(f"  (Usage: {water_gal:05d} gals)")
    print("----------------------------------------")
    
    if late_fee > 0:
        print(f"Prior Bal Late Fee:  ${late_fee:9.2f}")
        
    print(f"TOTAL AMOUNT DUE:    ${final_due:9.2f}")
    print("****************************************")

if __name__ == "__main__":
    main()
