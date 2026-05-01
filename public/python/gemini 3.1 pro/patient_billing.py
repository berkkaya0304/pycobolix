def main():
    print("+++ GENERAL HOSPITAL BILLING +++")
    pat_id = input("Patient ID: ")
    pat_name = input("Patient Name: ")
    try:
        admit_days = int(input("Days Admitted: "))
    except ValueError:
        admit_days = 0
    room_type = input("Room Type (1=Ward, 2=Semi, 3=Private): ").strip()
    try:
        surgery_chg = float(input("Surgery Charges ($): "))
    except ValueError:
        surgery_chg = 0.0
    try:
        medication_chg = float(input("Medication Charges ($): "))
    except ValueError:
        medication_chg = 0.0

    if room_type == '1':
        room_chg = admit_days * 150.00
    elif room_type == '2':
        room_chg = admit_days * 250.00
    elif room_type == '3':
        room_chg = admit_days * 400.00
    else:
        room_chg = admit_days * 150.00
        print("(Defaulted room to Ward)")

    total_chg = room_chg + surgery_chg + medication_chg
    
    insur_cover = total_chg * 0.80
    patient_owes = total_chg - insur_cover

    print("\n-----------------------------------------")
    print(" HOSPITAL DISCHARGE BILL")
    print("-----------------------------------------")
    print(f"Patient: {pat_name}  [ID: {pat_id}]")
    print(f"Days in Hospital: {admit_days:03d}")
    print(f"Room Charges:    ${room_chg:10.2f}")
    print(f"Surgery:         ${surgery_chg:10.2f}")
    print(f"Medication:      ${medication_chg:10.2f}")
    print("-----------------------------------------")
    print(f"GROSS TOTAL:     ${total_chg:10.2f}")
    print(f"Insurance Pays: -${insur_cover:10.2f}")
    print("=========================================")
    print(f"PATIENT TO PAY:  ${patient_owes:10.2f}")
    print("=========================================")
    
    print("Billing cycle complete.")

if __name__ == "__main__":
    main()
