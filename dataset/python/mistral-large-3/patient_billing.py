def patient_billing():
    print("+++ GENERAL HOSPITAL BILLING +++")

    # Input Phase
    patient_id = input("Patient ID: ").strip()
    patient_name = input("Patient Name: ").strip()
    admit_days = int(input("Days Admitted: ").strip())
    room_type = int(input("Room Type (1=Ward, 2=Semi, 3=Private): ").strip())
    surgery_chg = float(input("Surgery Charges ($): ").strip())
    medication_chg = float(input("Medication Charges ($): ").strip())

    # Process Phase
    if room_type == 1:
        room_chg = admit_days * 150.00
    elif room_type == 2:
        room_chg = admit_days * 250.00
    elif room_type == 3:
        room_chg = admit_days * 400.00
    else:
        room_chg = admit_days * 150.00
        print("(Defaulted room to Ward)")

    total_chg = room_chg + surgery_chg + medication_chg
    insur_cover = total_chg * 0.80
    patient_owes = total_chg - insur_cover

    # Output Phase
    def format_currency(value):
        return "${:,.2f}".format(value)

    print("\n-----------------------------------------")
    print(" HOSPITAL DISCHARGE BILL")
    print("-----------------------------------------")
    print(f"Patient: {patient_name}  [ID: {patient_id}]")
    print(f"Days in Hospital: {admit_days}")
    print(f"Room Charges:    {format_currency(room_chg)}")
    print(f"Surgery:         {format_currency(surgery_chg)}")
    print(f"Medication:      {format_currency(medication_chg)}")
    print("-----------------------------------------")
    print(f"GROSS TOTAL:     {format_currency(total_chg)}")
    print(f"Insurance Pays: -{format_currency(insur_cover)}")
    print("=========================================")
    print(f"PATIENT TO PAY:  {format_currency(patient_owes)}")
    print("=========================================")

    print("Billing cycle complete.")

if __name__ == "__main__":
    patient_billing()
