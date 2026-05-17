def main():
    print("--- CLAY CREATIONS STUDIO ---")
    student_name = input("Student Name: ")
    ticket_type = input("Session (1=Drop-In $35, 2=Member $0): ").strip()
    try:
        clay_lbs = float(input("Clay Required (Lbs, $2.50/lb): "))
    except ValueError:
        clay_lbs = 0.0
    try:
        kiln_firing = int(input("Items to Kiln Fire/Glaze ($5.00 ea): "))
    except ValueError:
        kiln_firing = 0

    if ticket_type == '1':
        studio_fee = 35.00
    elif ticket_type == '2':
        studio_fee = 0.0
    else:
        studio_fee = 35.00

    clay_fee = clay_lbs * 2.50
    kiln_fee = kiln_firing * 5.00

    grand_tot = studio_fee + clay_fee + kiln_fee

    print("\n========================================")
    print("            STUDIO WORKSHOP             ")
    print("========================================")
    print(f"Maker: {student_name}")
    print("----------------------------------------")
    print(f"Studio Access Fee:  ${studio_fee:6.2f}")
    
    if clay_lbs > 0:
        print(f"Clay ({clay_lbs:.2f} lbs):      ${clay_fee:6.2f}")
        
    if kiln_firing > 0:
        print(f"Kiln Firing ({kiln_firing:02d}):   ${kiln_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL COST:         ${grand_tot:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
