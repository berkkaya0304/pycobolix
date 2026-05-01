# POTTERY-CLASS - Clay Creations Studio
# Converted from COBOL to Python

def main():
    print("--- CLAY CREATIONS STUDIO ---")
    student_name = input("Student Name: ")
    ticket_type = int(input("Session (1=Drop-In $35, 2=Member $0): "))
    clay_lbs = float(input("Clay Required (Lbs, $2.50/lb): "))
    kiln_firing = int(input("Items to Kiln Fire/Glaze ($5.00 ea): "))

    studio_fee = 35.00 if ticket_type == 1 else 0.0
    clay_fee = clay_lbs * 2.50
    kiln_fee = kiln_firing * 5.00
    grand_tot = studio_fee + clay_fee + kiln_fee

    print("")
    print("========================================")
    print("            STUDIO WORKSHOP             ")
    print("========================================")
    print(f"Maker: {student_name}")
    print("----------------------------------------")
    print(f"Studio Access Fee:  ${studio_fee:,.2f}")
    if clay_lbs > 0:
        print(f"Clay ({clay_lbs} lbs):      ${clay_fee:,.2f}")
    if kiln_firing > 0:
        print(f"Kiln Firing ({kiln_firing}):   ${kiln_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL COST:         ${grand_tot:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
