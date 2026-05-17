"""
National History Museum Entry
Converted from COBOL (museum_entry.cbl) to Python
"""


def main():
    gen_rate = 25.00
    stu_rate = 15.00
    sen_rate = 12.00
    audio_rate = 8.00
    spec_rate = 10.00

    print("--- NATIONAL HISTORY MUSEUM ---")
    general_qty = int(input("General Admission QTY ($25): "))
    student_qty = int(input("Student Admission QTY ($15): "))
    senior_qty = int(input("Senior Admission QTY ($12): "))
    audio_guides = int(input("Audio Guides ($8 each): "))
    spec_exhibit = int(input("Special Exhibit Passes ($10 each): "))

    total_cost = (general_qty * gen_rate + student_qty * stu_rate
                  + senior_qty * sen_rate + audio_guides * audio_rate
                  + spec_exhibit * spec_rate)

    print()
    print("========================================")
    print("          MUSEUM TICKET RECIEPT         ")
    print("========================================")
    if general_qty > 0:
        print(f"{general_qty}x General Adm:    ${general_qty * gen_rate:>9,.2f}")
    if student_qty > 0:
        print(f"{student_qty}x Student Adm:    ${student_qty * stu_rate:>9,.2f}")
    if senior_qty > 0:
        print(f"{senior_qty}x Senior Adm:     ${senior_qty * sen_rate:>9,.2f}")
    if audio_guides > 0:
        print(f"{audio_guides}x Audio Guides:   ${audio_guides * audio_rate:>9,.2f}")
    if spec_exhibit > 0:
        print(f"{spec_exhibit}x Spec. Exhibit:  ${spec_exhibit * spec_rate:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL ADMISSION:    ${total_cost:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
