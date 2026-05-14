import sys

def main():
    # Constants
    CONSULT_FEE = 65.00
    VACCINE_UNIT_PRICE = 25.00
    BLOOD_TEST_FEE = 100.00
    TAX_RATE = 0.05

    print("=== PAWS & CLAWS VET CLINIC ===")
    
    # Input Section
    pet_name = input("Pet Name: ")
    pet_type = input("Pet Type (Dog/Cat/Bird/etc): ")
    owner_name = input("Owner Name: ")
    
    try:
        vaccine_qty = int(input("Number of Vaccines given ($25 each): "))
    except ValueError:
        vaccine_qty = 0
        
    blood_test_choice = input("Perform Blood Work? ($100) (Y/N): ")
    
    try:
        medication_amt = float(input("Cost of Dispensed Medications ($): "))
    except ValueError:
        medication_amt = 0.0

    # Calculation Section
    vaccine_fee = vaccine_qty * VACCINE_UNIT_PRICE
    test_fee = BLOOD_TEST_FEE if blood_test_choice.upper() == 'Y' else 0.0
    
    sub_total = CONSULT_FEE + vaccine_fee + test_fee + medication_amt
    tax = sub_total * TAX_RATE
    grand_total = sub_total + tax

    # Formatting helper to mimic PIC $ZZ,ZZ9.99
    def fmt_c(amount):
        return f"${amount:,.2f}"

    # Print Bill Section
    print("\n=========================================")
    print("           CLINIC INVOICE                ")
    print("=========================================")
    print(f"Patient: {pet_name} ({pet_type})")
    print(f"Owner:   {owner_name}")
    print("-----------------------------------------")
    print(f"General Consultation: {fmt_c(CONSULT_FEE)}")
    
    if vaccine_fee > 0:
        print(f"Vaccinations ({vaccine_qty}):    {fmt_c(vaccine_fee)}")
        
    if test_fee > 0:
        print(f"Laboratory/Blood:     {fmt_c(test_fee)}")
        
    if medication_amt > 0:
        print(f"Prescription Meds:    {fmt_c(medication_amt)}")
        
    print("-----------------------------------------")
    print(f"SubTotal:             {fmt_c(sub_total)}")
    print(f"Tax (5%):             {fmt_c(tax)}")
    print("=========================================")
    print(f"TOTAL BALANCE DUE:    {fmt_c(grand_total)}")
    print("=========================================")

if __name__ == "__main__":
    main()
