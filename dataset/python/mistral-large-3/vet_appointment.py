def vet_appointment():
    print("--- VET CLINIC SCHEDULING ---")
    pet_name = input("Pet Name: ").strip()

    print("Reason for Visit: ")
    print("1=Wellness Exam ($50)")
    print("2=Sick Visit ($85)")
    print("3=Emergency ($150)")
    visit_reason = input().strip()

    print("Requested Doctor: ")
    print("1=Dr. Smith (General)")
    print("2=Dr. Jones (Specialist +$40)")
    doctor_req = input().strip()

    exam_fee, reason_txt = calculate_exam_fee(visit_reason)
    dr_surcharge, dr_txt = calculate_doctor_fee(doctor_req)
    total_estimate = exam_fee + dr_surcharge

    print_confirmation(pet_name, dr_txt, reason_txt, exam_fee, dr_surcharge, total_estimate)

def calculate_exam_fee(visit_reason):
    if visit_reason == "1":
        return 50.00, "Wellness Exam"
    elif visit_reason == "2":
        return 85.00, "Sick Visit"
    elif visit_reason == "3":
        return 150.00, "Emergency"
    else:
        return 50.00, "Wellness (Default)"

def calculate_doctor_fee(doctor_req):
    if doctor_req == "1":
        return 0.00, "Dr. Smith"
    elif doctor_req == "2":
        return 40.00, "Dr. Jones"
    else:
        return 0.00, "Any Available"

def print_confirmation(pet_name, dr_txt, reason_txt, exam_fee, dr_surcharge, total_estimate):
    print()
    print("=" * 40)
    print("       APPOINTMENT CONFIRMATION         ")
    print("=" * 40)
    print(f"Patient: {pet_name}")
    print(f"Doctor:  {dr_txt}")
    print(f"Visit:   {reason_txt}")
    print("-" * 40)
    print(f"Base Exam Fee:      ${exam_fee:,.2f}")
    if dr_surcharge > 0:
        print(f"Specialist Fee:     ${dr_surcharge:,.2f}")
    print("-" * 40)
    print(f"ESTIMATED TOTAL:    ${total_estimate:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    vet_appointment()
