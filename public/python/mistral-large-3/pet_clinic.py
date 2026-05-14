def main():
    print("=== PAWS & CLAWS VET CLINIC ===")

    patient_info = {
        "pet_name": input("Pet Name: ").strip(),
        "pet_type": input("Pet Type (Dog/Cat/Bird/etc): ").strip(),
        "owner_name": input("Owner Name: ").strip()
    }

    vet_services = {
        "consult_fee": 65.00,
        "vaccine_qty": int(input("Number of Vaccines given ($25 each): ")),
        "vaccine_fee": 0.00,
        "blood_test": input("Perform Blood Work? ($100) (Y/N): ").strip().upper(),
        "test_fee": 0.00,
        "medication_amt": float(input("Cost of Dispensed Medications ($): "))
    }

    billing = {
        "sub_total": 0.00,
        "tax": 0.00,
        "grand_total": 0.00
    }

    def calc_bill():
        vet_services["vaccine_fee"] = vet_services["vaccine_qty"] * 25.00

        if vet_services["blood_test"] == 'Y':
            vet_services["test_fee"] = 100.00

        billing["sub_total"] = (
            vet_services["consult_fee"] +
            vet_services["vaccine_fee"] +
            vet_services["test_fee"] +
            vet_services["medication_amt"]
        )
        billing["tax"] = billing["sub_total"] * 0.05
        billing["grand_total"] = billing["sub_total"] + billing["tax"]

    def print_bill():
        def format_currency(value):
            return f"${value:,.2f}"

        print("\n=========================================")
        print("           CLINIC INVOICE                ")
        print("=========================================")
        print(f"Patient: {patient_info['pet_name']} ({patient_info['pet_type']})")
        print(f"Owner:   {patient_info['owner_name']}")
        print("-----------------------------------------")
        print(f"General Consultation: {format_currency(vet_services['consult_fee'])}")

        if vet_services["vaccine_fee"] > 0:
            print(f"Vaccinations ({vet_services['vaccine_qty']}):    {format_currency(vet_services['vaccine_fee'])}")

        if vet_services["test_fee"] > 0:
            print(f"Laboratory/Blood:     {format_currency(vet_services['test_fee'])}")

        if vet_services["medication_amt"] > 0:
            print(f"Prescription Meds:    {format_currency(vet_services['medication_amt'])}")

        print("-----------------------------------------")
        print(f"SubTotal:             {format_currency(billing['sub_total'])}")
        print(f"Tax (5%):             {format_currency(billing['tax'])}")
        print("=========================================")
        print(f"TOTAL BALANCE DUE:    {format_currency(billing['grand_total'])}")
        print("=========================================")

    calc_bill()
    print_bill()

if __name__ == "__main__":
    main()
