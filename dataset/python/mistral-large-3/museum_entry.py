def museum_entry():
    print("--- NATIONAL HISTORY MUSEUM ---")

    # Get ticket quantities
    general_qty = int(input("General Admission QTY ($25): "))
    student_qty = int(input("Student Admission QTY ($15): "))
    senior_qty = int(input("Senior Admission QTY ($12): "))

    # Get add-ons
    audio_guides = int(input("Audio Guides ($8 each): "))
    spec_exhibit = int(input("Special Exhibit Passes ($10 each): "))

    # Calculate costs
    gen_rate = 25.00
    stu_rate = 15.00
    sen_rate = 12.00
    audio_rate = 8.00
    spec_rate = 10.00

    total_cost = (general_qty * gen_rate +
                  student_qty * stu_rate +
                  senior_qty * sen_rate +
                  audio_guides * audio_rate +
                  spec_exhibit * spec_rate)

    # Display receipt
    print("")
    print("=" * 40)
    print("          MUSEUM TICKET RECEIPT         ")
    print("=" * 40)

    if general_qty > 0:
        print(f"{general_qty}x General Adm:    ${general_qty * gen_rate:.2f}")
    if student_qty > 0:
        print(f"{student_qty}x Student Adm:    ${student_qty * stu_rate:.2f}")
    if senior_qty > 0:
        print(f"{senior_qty}x Senior Adm:     ${senior_qty * sen_rate:.2f}")
    if audio_guides > 0:
        print(f"{audio_guides}x Audio Guides:   ${audio_guides * audio_rate:.2f}")
    if spec_exhibit > 0:
        print(f"{spec_exhibit}x Spec. Exhibit:  ${spec_exhibit * spec_rate:.2f}")

    print("-" * 40)
    print(f"TOTAL ADMISSION:    ${total_cost:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    museum_entry()
