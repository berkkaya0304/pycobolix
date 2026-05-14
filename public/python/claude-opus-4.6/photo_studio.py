"""
Lens Aperture Studio - Photo Studio
Converted from COBOL (photo_studio.cbl) to Python
"""


def main():
    print("--- LENS APERTURE STUDIO ---")
    client_name = input("Client: ")
    session_type = int(input("Session (1=Headshot $99, 2=Family $150, 3=Event): "))
    phy_prints = int(input("Physical Prints Wanted ($15 per sheet): "))
    digital_copy = input("USB Drive with Digital Masters ($50)? (Y/N): ").strip().upper()

    if session_type == 1:
        sitting_fee = 99.00
    elif session_type == 2:
        sitting_fee = 150.00
    elif session_type == 3:
        sitting_fee = 300.00
    else:
        sitting_fee = 99.00

    print_fee = phy_prints * 15.00
    digital_fee = 50.00 if digital_copy == "Y" else 0.0
    grand_total = sitting_fee + print_fee + digital_fee

    print()
    print("========================================")
    print("          STUDIO INVOICE                ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    print(f"Session/Sitting Fee: ${sitting_fee:>9,.2f}")
    if print_fee > 0:
        print(f"Physical Prints ({phy_prints}):  ${print_fee:>9,.2f}")
    if digital_fee > 0:
        print(f"Digital Masters USB: ${digital_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL CHARGED:       ${grand_total:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
