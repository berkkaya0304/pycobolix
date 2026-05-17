def photo_studio():
    print("--- LENS APERTURE STUDIO ---")
    client_name = input("Client: ").strip()
    session_type = int(input("Session (1=Headshot $99, 2=Family $150, 3=Event): ").strip())
    phy_prints = int(input("Physical Prints Wanted ($15 per sheet): ").strip())
    digital_copy = input("USB Drive with Digital Masters ($50)? (Y/N): ").strip().upper()

    sitting_fee = 0.0
    if session_type == 1:
        sitting_fee = 99.00
    elif session_type == 2:
        sitting_fee = 150.00
    elif session_type == 3:
        sitting_fee = 300.00
    else:
        sitting_fee = 99.00

    print_fee = phy_prints * 15.00
    digital_fee = 50.00 if digital_copy == 'Y' else 0.0
    grand_total = sitting_fee + print_fee + digital_fee

    print("\n========================================")
    print("          STUDIO INVOICE                ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    print(f"Session/Sitting Fee: ${sitting_fee:,.2f}")

    if print_fee > 0:
        print(f"Physical Prints ({phy_prints}):  ${print_fee:,.2f}")

    if digital_fee > 0:
        print(f"Digital Masters USB: ${digital_fee:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL CHARGED:       ${grand_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    photo_studio()
