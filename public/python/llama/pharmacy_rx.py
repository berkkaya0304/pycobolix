# PHARMACY-RX - Cornerstone Pharmacy RX
# Converted from COBOL to Python

def main():
    print("--- CORNERSTONE PHARMACY RX ---")
    patient_name = input("Patient Name: ")
    print("Type of Medication:")
    print("1=Generic ($25), 2=Brand ($150), 3=Specialty ($800)")
    med_type = int(input())
    insur_provider = input("Does patient have insurance? (Y/N): ").strip().upper()
    refill_months = int(input("Number of months supply (1-12): "))

    if med_type == 1:
        base_price = 25.00
        copay_per_month = 10.00
    elif med_type == 2:
        base_price = 150.00
        copay_per_month = 40.00
    elif med_type == 3:
        base_price = 800.00
        copay_per_month = 100.00
    else:
        base_price = 25.00
        copay_per_month = 10.00

    retail_value = base_price * refill_months
    total_charge = retail_value

    if insur_provider == 'Y':
        copay_amt = copay_per_month * refill_months
        if copay_amt > total_charge:
            copay_amt = total_charge
        total_charge = copay_amt

    print("")
    print("=======================================")
    print("         PRESCRIPTION LABEL            ")
    print("=======================================")
    print(f"Patient: {patient_name}")
    print(f"Supply:  {refill_months} Month(s)")
    print("---------------------------------------")
    print(f"Retail Value:         ${retail_value:,.2f}")
    if insur_provider == 'Y':
        print("Insurance Applied:    YES")
    else:
        print("Insurance Applied:    NO")
    print("---------------------------------------")
    print(f"PATIENT RESPONSIBILITY: ${total_charge:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
