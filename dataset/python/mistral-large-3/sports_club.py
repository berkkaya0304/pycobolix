def sports_club():
    print("--- ELITE SPORTS CLUB REGISTRATION ---")
    member_name = input("Member Name: ").strip()
    sport_dept = input("Sport (T=Tennis, G=Golf, S=Swimming): ").strip().upper()
    months_mbr = int(input("Months to prepay (1-12): ").strip())
    equipment_rnt = input("Rent Club Equipment ($30/mo)? (Y/N): ").strip().upper() == 'Y'

    registry_fee = 150.00
    monthly_fee = 0.0
    equip_fee = 30.00 if equipment_rnt else 0.0

    if sport_dept == 'T':
        monthly_fee = 100.00
    elif sport_dept == 'G':
        monthly_fee = 250.00
    elif sport_dept == 'S':
        monthly_fee = 75.00
    else:
        monthly_fee = 100.00

    sub_total = (monthly_fee * months_mbr) + (equip_fee * months_mbr)
    total_bill = sub_total + registry_fee

    print("\n=======================================")
    print("           CLUB MEMBERSHIP             ")
    print("=======================================")
    print(f"Welcome, {member_name}")
    print(f"Prepaid Term: {months_mbr} months")
    print("---------------------------------------")
    print(f"One-Time Joining Fee: ${registry_fee:,.2f}")
    print(f"Membership Dues:      ${monthly_fee * months_mbr:,.2f}")

    if equipment_rnt:
        print(f"Equipment Rental:     ${equip_fee * months_mbr:,.2f}")

    print("---------------------------------------")
    print(f"TOTAL REGISTRATION:   ${total_bill:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    sports_club()
