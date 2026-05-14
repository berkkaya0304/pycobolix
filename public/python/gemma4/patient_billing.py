def main():
    print("+++ GENERAL HOSPITAL BILLING +++")
    
    # Input Phase
    pat_id = input("Patient ID: ")
    pat_name = input("Patient Name: ")
    
    try:
        admit_days = int(input("Days Admitted: "))
        room_type = int(input("Room Type (1=Ward, 2=Semi, 3=Private): "))
        surgery_chg = float(input("Surgery Charges ($): "))
        medication_chg = float(input("Medication Charges ($): "))
    except ValueError:
        print("Invalid numeric input. Please restart.")
        return

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
    print("\n-----------------------------------------")
    print(" HOSPITAL DISCHARGE BILL")
    print("-----------------------------------------")
    print(f"Patient: {pat_name:<25}  [ID: {pat_id}]")
    print(f"Days in Hospital: {admit_days}")
    
    # Formatting as $$,$$$,$$9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

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
    main()
