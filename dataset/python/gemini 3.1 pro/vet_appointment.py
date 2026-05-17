def main():
    print("--- VET CLINIC SCHEDULING ---")
    pet_name = input("Pet Name: ")
    print("Reason for Visit: ")
    print("1=Wellness Exam ($50)")
    print("2=Sick Visit ($85)")
    print("3=Emergency ($150)")
    visit_reason = input().strip()
    
    print("Requested Doctor: ")
    print("1=Dr. Smith (General)")
    print("2=Dr. Jones (Specialist +$40)")
    doctor_req = input().strip()

    if visit_reason == '1':
        exam_fee = 50.00
        reason_txt = "Wellness Exam"
    elif visit_reason == '2':
        exam_fee = 85.00
        reason_txt = "Sick Visit"
    elif visit_reason == '3':
        exam_fee = 150.00
        reason_txt = "Emergency"
    else:
        exam_fee = 50.00
        reason_txt = "Wellness (Default)"

    if doctor_req == '1':
        dr_surcharge = 0.0
        dr_txt = "Dr. Smith"
    elif doctor_req == '2':
        dr_surcharge = 40.00
        dr_txt = "Dr. Jones"
    else:
        dr_surcharge = 0.0
        dr_txt = "Any Available"

    total_estimate = exam_fee + dr_surcharge

    print("\n========================================")
    print("       APPOINTMENT CONFIRMATION         ")
    print("========================================")
    print(f"Patient: {pet_name}")
    print(f"Doctor:  {dr_txt}")
    print(f"Visit:   {reason_txt}")
    print("----------------------------------------")
    print(f"Base Exam Fee:      ${exam_fee:6.2f}")
    
    if dr_surcharge > 0:
        print(f"Specialist Fee:     ${dr_surcharge:6.2f}")
        
    print("----------------------------------------")
    print(f"ESTIMATED TOTAL:    ${total_estimate:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
