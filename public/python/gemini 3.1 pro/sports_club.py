def main():
    print("--- ELITE SPORTS CLUB REGISTRATION ---")
    member_name = input("Member Name: ")
    sport_dept = input("Sport (T=Tennis, G=Golf, S=Swimming): ").strip().upper()
    try:
        months_mbr = int(input("Months to prepay (1-12): "))
    except ValueError:
        months_mbr = 1
    equipment_rnt = input("Rent Club Equipment ($30/mo)? (Y/N): ").strip().upper() == 'Y'

    registry_fee = 150.00

    if sport_dept == 'T':
        monthly_fee = 100.00
    elif sport_dept == 'G':
        monthly_fee = 250.00
    elif sport_dept == 'S':
        monthly_fee = 75.00
    else:
        monthly_fee = 100.00

    equip_fee = 30.00 if equipment_rnt else 0.0

    sub_total = (monthly_fee * months_mbr) + (equip_fee * months_mbr)
    total_bill = sub_total + registry_fee

    print("\n=======================================")
    print("           CLUB MEMBERSHIP             ")
    print("=======================================")
    print(f"Welcome, {member_name}")
    print(f"Prepaid Term: {months_mbr:02d} months")
    print("---------------------------------------")
    print(f"One-Time Joining Fee: ${registry_fee:6.2f}")
    
    monthly_fee_total = monthly_fee * months_mbr
    print(f"Membership Dues:      ${monthly_fee_total:6.2f}")
    
    if equipment_rnt:
        equip_fee_total = equip_fee * months_mbr
        print(f"Equipment Rental:     ${equip_fee_total:6.2f}")
        
    print("---------------------------------------")
    print(f"TOTAL REGISTRATION:   ${total_bill:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
