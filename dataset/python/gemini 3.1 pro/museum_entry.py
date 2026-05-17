def main():
    print("--- NATIONAL HISTORY MUSEUM ---")
    try:
        general_qty = int(input("General Admission QTY ($25): "))
    except ValueError:
        general_qty = 0
    try:
        student_qty = int(input("Student Admission QTY ($15): "))
    except ValueError:
        student_qty = 0
    try:
        senior_qty = int(input("Senior Admission QTY ($12): "))
    except ValueError:
        senior_qty = 0
        
    try:
        audio_guides = int(input("Audio Guides ($8 each): "))
    except ValueError:
        audio_guides = 0
    try:
        spec_exhibit = int(input("Special Exhibit Passes ($10 each): "))
    except ValueError:
        spec_exhibit = 0

    gen_rate = 25.00
    stu_rate = 15.00
    sen_rate = 12.00
    audio_rate = 8.00
    spec_rate = 10.00
    
    total_cost = (general_qty * gen_rate) + \
                 (student_qty * stu_rate) + \
                 (senior_qty * sen_rate) + \
                 (audio_guides * audio_rate) + \
                 (spec_exhibit * spec_rate)

    print("\n========================================")
    print("          MUSEUM TICKET RECIEPT         ")
    print("========================================")
    
    if general_qty > 0:
        disp = general_qty * gen_rate
        print(f"{general_qty:02d}x General Adm:    ${disp:6.2f}")
    if student_qty > 0:
        disp = student_qty * stu_rate
        print(f"{student_qty:02d}x Student Adm:    ${disp:6.2f}")
    if senior_qty > 0:
        disp = senior_qty * sen_rate
        print(f"{senior_qty:02d}x Senior Adm:     ${disp:6.2f}")
    if audio_guides > 0:
        disp = audio_guides * audio_rate
        print(f"{audio_guides:02d}x Audio Guides:   ${disp:6.2f}")
    if spec_exhibit > 0:
        disp = spec_exhibit * spec_rate
        print(f"{spec_exhibit:02d}x Spec. Exhibit:  ${disp:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL ADMISSION:    ${total_cost:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
