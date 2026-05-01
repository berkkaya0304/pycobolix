def main():
    print("--- CORNERSTONE PHARMACY RX ---")
    patient_name = input("Patient Name: ")
    print("Type of Medication: ")
    med_type = input("1=Generic ($25), 2=Brand ($150), 3=Specialty ($800): ").strip()
    insur_provider = input("Does patient have insurance? (Y/N): ").strip().upper() == 'Y'
    try:
        refill_months = int(input("Number of months supply (1-12): "))
    except ValueError:
        refill_months = 1

    if med_type == '1':
        base_price = 25.00
    elif med_type == '2':
        base_price = 150.00
    elif med_type == '3':
        base_price = 800.00
    else:
        base_price = 25.00

    total_charge = base_price * refill_months
    copay_amt = 0.0

    if insur_provider:
        if med_type == '1':
            copay_amt = 10.00 * refill_months
        elif med_type == '2':
            copay_amt = 40.00 * refill_months
        elif med_type == '3':
            copay_amt = 100.00 * refill_months
        else:
            copay_amt = 10.00 * refill_months

        if copay_amt > total_charge:
            copay_amt = total_charge
            
        total_charge = copay_amt

    print("\n=======================================")
    print("         PRESCRIPTION LABEL            ")
    print("=======================================")
    print(f"Patient: {patient_name}")
    print(f"Supply:  {refill_months:02d} Month(s)")
    print("---------------------------------------")
    
    retail_value = base_price * refill_months
    print(f"Retail Value:         ${retail_value:6.2f}")
    
    if insur_provider:
        print("Insurance Applied:    YES")
    else:
        print("Insurance Applied:    NO")
        
    print("---------------------------------------")
    print(f"PATIENT RESPONSIBILITY: ${total_charge:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
