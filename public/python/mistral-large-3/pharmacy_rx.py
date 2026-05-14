def pharmacy_rx():
    print("--- CORNERSTONE PHARMACY RX ---")

    patient_name = input("Patient Name: ").strip()
    print("Type of Medication: ")
    print("1=Generic ($25), 2=Brand ($150), 3=Specialty ($800)")
    med_type = int(input().strip())
    has_insurance = input("Does patient have insurance? (Y/N): ").strip().upper() == 'Y'
    refill_months = int(input("Number of months supply (1-12): ").strip())

    base_price, copay_amt, total_charge = calc_rx(med_type, has_insurance, refill_months)
    print_label(patient_name, med_type, refill_months, base_price, has_insurance, total_charge)

def calc_rx(med_type, has_insurance, refill_months):
    if med_type == 1:
        base_price = 25.00
    elif med_type == 2:
        base_price = 150.00
    elif med_type == 3:
        base_price = 800.00
    else:
        base_price = 25.00

    total_charge = base_price * refill_months

    if has_insurance:
        if med_type == 1:
            copay_amt = 10.00 * refill_months
        elif med_type == 2:
            copay_amt = 40.00 * refill_months
        elif med_type == 3:
            copay_amt = 100.00 * refill_months
        else:
            copay_amt = 10.00 * refill_months

        if copay_amt > total_charge:
            copay_amt = total_charge

        total_charge = copay_amt

    return base_price, copay_amt, total_charge

def print_label(patient_name, med_type, refill_months, base_price, has_insurance, total_charge):
    print()
    print("=======================================")
    print("         PRESCRIPTION LABEL            ")
    print("=======================================")
    print(f"Patient: {patient_name}")
    print(f"Supply:  {refill_months} Month(s)")
    print("---------------------------------------")

    retail_value = base_price * refill_months
    print(f"Retail Value:         ${retail_value:,.2f}")

    if has_insurance:
        print("Insurance Applied:    YES")
    else:
        print("Insurance Applied:    NO")

    print("---------------------------------------")
    print(f"PATIENT RESPONSIBILITY: ${total_charge:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    pharmacy_rx()
