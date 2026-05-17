def main():
    print("--- TELECOM MONTHLY STATEMENT ---")
    try:
        phone_num = int(input("Phone Number: "))
    except ValueError:
        phone_num = 0
    plan_type = input("Plan (B=Basic 5GB $30, U=Unlimited $70): ").strip().upper()
    try:
        data_used_gb = float(input("Total Data Used (GB): "))
    except ValueError:
        data_used_gb = 0.0
    try:
        intl_minutes = int(input("International Calling Minutes: "))
    except ValueError:
        intl_minutes = 0

    overage_charge = 0.0
    
    if plan_type == 'B':
        base_charge = 30.00
        if data_used_gb > 5.00:
            overage_charge = (data_used_gb - 5.00) * 10.00
    elif plan_type == 'U':
        base_charge = 70.00
        overage_charge = 0.0
    else:
        base_charge = 30.00

    intl_charge = intl_minutes * 0.25

    total_bill = base_charge + overage_charge + intl_charge
    taxes = total_bill * 0.12
    total_bill += taxes

    print("\n=======================================")
    print("          MONTHLY INVOICE              ")
    print("=======================================")
    print(f"Mobile Number: {phone_num:010d}")
    print("---------------------------------------")
    print(f"Plan Base Charge:    ${base_charge:6.2f}")
    
    if overage_charge > 0:
        print(f"Data Overage Fees:   ${overage_charge:6.2f}")
        
    if intl_charge > 0:
        print(f"Int'l Call Charges:  ${intl_charge:6.2f}")
        
    print("---------------------------------------")
    print(f"Taxes & Surcharges:  ${taxes:6.2f}")
    print(f"TOTAL AMOUNT DUE:    ${total_bill:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
