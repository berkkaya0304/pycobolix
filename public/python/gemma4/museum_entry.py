def main():
    # Rates
    GEN_RATE = 25.00
    STU_RATE = 15.00
    SEN_RATE = 12.00
    AUDIO_RATE = 8.00
    SPEC_RATE = 10.00

    print("--- NATIONAL HISTORY MUSEUM ---")
    
    try:
        general_qty = int(input("General Admission QTY ($25): ") or 0)
        student_qty = int(input("Student Admission QTY ($15): ") or 0)
        senior_qty = int(input("Senior Admission QTY ($12): ") or 0)
        audio_guides = int(input("Audio Guides ($8 each): ") or 0)
        spec_exhibit = int(input("Special Exhibit Passes ($10 each): ") or 0)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    total_cost = (
        (general_qty * GEN_RATE) +
        (student_qty * STU_RATE) +
        (senior_qty * SEN_RATE) +
        (audio_guides * AUDIO_RATE) +
        (spec_exhibit * SPEC_RATE)
    )

    print("\n========================================")
    print("          MUSEUM TICKET RECIEPT         ")
    print("========================================")

    if general_qty > 0:
        print(f"{general_qty}x General Adm:    ${general_qty * GEN_RATE:,.2f}")
    
    if student_qty > 0:
        print(f"{student_qty}x Student Adm:    ${student_qty * STU_RATE:,.2f}")
        
    if senior_qty > 0:
        print(f"{senior_qty}x Senior Adm:     ${senior_qty * SEN_RATE:,.2f}")
        
    if audio_guides > 0:
        print(f"{audio_guides}x Audio Guides:   ${audio_guides * AUDIO_RATE:,.2f}")
        
    if spec_exhibit > 0:
        print(f"{spec_exhibit}x Spec. Exhibit:  ${spec_exhibit * SPEC_RATE:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL ADMISSION:    ${total_cost:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
