import sys

def main():
    print("--- CORNERSTONE PHARMACY RX ---")
    
    patient_name = input("Patient Name: ")
    
    print("Type of Medication: ")
    print("1=Generic ($25), 2=Brand ($150), 3=Specialty ($800)")
    try:
        med_type = int(input())
    except ValueError:
        med_type = 1

    insur_provider = input("Does patient have insurance? (Y/N): ").upper()
    has_insurance = (insur_provider == 'Y')
    
    try:
        refill_months = int(input("Number of months supply (1-12): "))
    except ValueError:
        refill_months = 1

    # Calculate Base Price
    if med_type == 1:
        base_unit_price = 25.00
    elif med_type == 2:
        base_unit_price = 150.00
    elif med_type == 3:
        base_unit_price = 800.00
    else:
        base_unit_price = 25.00

    total_charge = base_unit_price * refill_months

    if has_insurance:
        if med_type == 1:
            copay_amt = 10.00 * refill_months
        elif med_type == 2:
            copay_amt = 40.00 * refill_months
        elif med_type == 3:
            copay_amt = 100.00 * refill_months
        else:
            copay_amt = 0.00
            
        if copay_amt > total_charge:
            copay_amt = total_charge
            
        total_charge = copay_amt

    # Print Label
    retail_value = base_unit_price * refill_months
    
    print("\n=======================================")
    print("         PRESCRIPTION LABEL            ")
    print("=======================================")
    print(f"Patient: {patient_name}")
    print(f"Supply:  {refill_months} Month(s)")
    print("---------------------------------------")
    print(f"Retail Value:         ${retail_value:,.2f}")
    
    if has_insurance:
        print("Insurance Applied:    YES")
    else:
        print("Insurance Applied:    NO")
        
    print("---------------------------------------")
    print(f"PATIENT RESPONSIBILITY: ${total_charge:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
