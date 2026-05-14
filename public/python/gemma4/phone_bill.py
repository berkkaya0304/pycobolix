def calculate_bill(plan_type, data_used_gb, intl_minutes):
    base_charge = 0.0
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
    subtotal = base_charge + overage_charge + intl_charge
    taxes = subtotal * 0.12
    total_bill = subtotal + taxes
    
    return {
        "base_charge": base_charge,
        "overage_charge": overage_charge,
        "intl_charge": intl_charge,
        "taxes": taxes,
        "total_bill": total_bill
    }

def print_bill(phone_num, bill_details):
    print("\n=======================================")
    print("          MONTHLY INVOICE              ")
    print("=======================================")
    print(f"Mobile Number: {phone_num}")
    print("---------------------------------------")
    print(f"Plan Base Charge:    ${bill_details['base_charge']:,.2f}")
    
    if bill_details['overage_charge'] > 0:
        print(f"Data Overage Fees:   ${bill_details['overage_charge']:,.2f}")
        
    if bill_details['intl_charge'] > 0:
        print(f"Int'l Call Charges:  ${bill_details['intl_charge']:,.2f}")
        
    print("---------------------------------------")
    print(f"Taxes & Surcharges:  ${bill_details['taxes']:,.2f}")
    print(f"TOTAL AMOUNT DUE:    ${bill_details['total_bill']:,.2f}")
    print("=======================================")

def main():
    print("--- TELECOM MONTHLY STATEMENT ---")
    phone_num = input("Phone Number: ")
    plan_type = input("Plan (B=Basic 5GB $30, U=Unlimited $70): ").upper()
    
    try:
        data_used_gb = float(input("Total Data Used (GB): "))
        intl_minutes = int(input("International Calling Minutes: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for data and minutes.")
        return

    bill_details = calculate_bill(plan_type, data_used_gb, intl_minutes)
    print_bill(phone_num, bill_details)

if __name__ == "__main__":
    main()
