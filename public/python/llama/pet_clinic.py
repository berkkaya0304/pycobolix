# PET-CLINIC - Paws & Claws Vet Clinic
# Converted from COBOL to Python

def main():
    CONSULT_FEE = 65.00

    print("=== PAWS & CLAWS VET CLINIC ===")
    pet_name = input("Pet Name: ")
    pet_type = input("Pet Type (Dog/Cat/Bird/etc): ")
    owner_name = input("Owner Name: ")
    vaccine_qty = int(input("Number of Vaccines given ($25 each): "))
    blood_test = input("Perform Blood Work? ($100) (Y/N): ").strip().upper()
    medication_amt = float(input("Cost of Dispensed Medications ($): "))

    vaccine_fee = vaccine_qty * 25.00
    test_fee = 100.00 if blood_test == 'Y' else 0.0
    sub_total = CONSULT_FEE + vaccine_fee + test_fee + medication_amt
    tax = sub_total * 0.05
    grand_total = sub_total + tax

    print("")
    print("=========================================")
    print("           CLINIC INVOICE                ")
    print("=========================================")
    print(f"Patient: {pet_name} ({pet_type})")
    print(f"Owner:   {owner_name}")
    print("-----------------------------------------")
    print(f"General Consultation: ${CONSULT_FEE:,.2f}")
    if vaccine_fee > 0:
        print(f"Vaccinations ({vaccine_qty}):    ${vaccine_fee:,.2f}")
    if test_fee > 0:
        print(f"Laboratory/Blood:     ${test_fee:,.2f}")
    if medication_amt > 0:
        print(f"Prescription Meds:    ${medication_amt:,.2f}")
    print("-----------------------------------------")
    print(f"SubTotal:             ${sub_total:,.2f}")
    print(f"Tax (5%):             ${tax:,.2f}")
    print("=========================================")
    print(f"TOTAL BALANCE DUE:    ${grand_total:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
