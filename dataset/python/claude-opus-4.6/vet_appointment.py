"""
Vet Clinic Scheduling - Vet Appointment
Converted from COBOL (vet_appointment.cbl) to Python
"""


def main():
    print("--- VET CLINIC SCHEDULING ---")
    pet_name = input("Pet Name: ")
    print("Reason for Visit:")
    print("1=Wellness Exam ($50)")
    print("2=Sick Visit ($85)")
    print("3=Emergency ($150)")
    visit_reason = int(input("Select: "))

    print("Requested Doctor:")
    print("1=Dr. Smith (General)")
    print("2=Dr. Jones (Specialist +$40)")
    doctor_req = int(input("Select: "))

    if visit_reason == 1:
        exam_fee, reason_txt = 50.00, "Wellness Exam"
    elif visit_reason == 2:
        exam_fee, reason_txt = 85.00, "Sick Visit"
    elif visit_reason == 3:
        exam_fee, reason_txt = 150.00, "Emergency"
    else:
        exam_fee, reason_txt = 50.00, "Wellness (Default)"

    if doctor_req == 1:
        dr_surcharge, dr_txt = 0.0, "Dr. Smith"
    elif doctor_req == 2:
        dr_surcharge, dr_txt = 40.00, "Dr. Jones"
    else:
        dr_surcharge, dr_txt = 0.0, "Any Available"

    total_estimate = exam_fee + dr_surcharge

    print()
    print("========================================")
    print("       APPOINTMENT CONFIRMATION         ")
    print("========================================")
    print(f"Patient: {pet_name}")
    print(f"Doctor:  {dr_txt}")
    print(f"Visit:   {reason_txt}")
    print("----------------------------------------")
    print(f"Base Exam Fee:      ${exam_fee:>9,.2f}")
    if dr_surcharge > 0:
        print(f"Specialist Fee:     ${dr_surcharge:>9,.2f}")
    print("----------------------------------------")
    print(f"ESTIMATED TOTAL:    ${total_estimate:>9,.2f}")
    print("=======================================")


if __name__ == "__main__":
    main()
