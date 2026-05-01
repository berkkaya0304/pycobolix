# SPORTS-CLUB - Elite Sports Club Registration
# Converted from COBOL to Python

def main():
    REGISTRY_FEE = 150.00

    print("--- ELITE SPORTS CLUB REGISTRATION ---")
    member_name = input("Member Name: ")
    sport_dept = input("Sport (T=Tennis, G=Golf, S=Swimming): ").strip().upper()
    months_mbr = int(input("Months to prepay (1-12): "))
    equipment_rnt = input("Rent Club Equipment ($30/mo)? (Y/N): ").strip().upper()

    if sport_dept == 'T':
        monthly_fee = 100.00
    elif sport_dept == 'G':
        monthly_fee = 250.00
    elif sport_dept == 'S':
        monthly_fee = 75.00
    else:
        monthly_fee = 100.00

    equip_fee = 30.00 if equipment_rnt == 'Y' else 0.0

    membership_total = monthly_fee * months_mbr
    equip_total = equip_fee * months_mbr
    sub_total = membership_total + equip_total
    total_bill = sub_total + REGISTRY_FEE

    print("")
    print("=======================================")
    print("           CLUB MEMBERSHIP             ")
    print("=======================================")
    print(f"Welcome, {member_name}")
    print(f"Prepaid Term: {months_mbr} months")
    print("---------------------------------------")
    print(f"One-Time Joining Fee: ${REGISTRY_FEE:,.2f}")
    print(f"Membership Dues:      ${membership_total:,.2f}")
    if equipment_rnt == 'Y':
        print(f"Equipment Rental:     ${equip_total:,.2f}")
    print("---------------------------------------")
    print(f"TOTAL REGISTRATION:   ${total_bill:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
