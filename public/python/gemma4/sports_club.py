def main():
    print("--- ELITE SPORTS CLUB REGISTRATION ---")
    
    member_name = input("Member Name: ")
    sport_dept = input("Sport (T=Tennis, G=Golf, S=Swimming): ").upper()
    
    try:
        months_mbr = int(input("Months to prepay (1-12): "))
    except ValueError:
        months_mbr = 1
        
    equipment_rnt = input("Rent Club Equipment ($30/mo)? (Y/N): ").upper()

    # Constants and Fees
    registry_fee = 150.00
    equip_fee_rate = 0.00
    
    # Determine Monthly Fee based on Sport
    if sport_dept == 'T':
        monthly_fee_rate = 100.00
    elif sport_dept == 'G':
        monthly_fee_rate = 250.00
    elif sport_dept == 'S':
        monthly_fee_rate = 75.00
    else:
        monthly_fee_rate = 100.00

    # Equipment Rental Fee
    if equipment_rnt == 'Y':
        equip_fee_rate = 30.00

    # Calculations
    sub_total = (monthly_fee_rate * months_mbr) + (equip_fee_rate * months_mbr)
    total_bill = sub_total + registry_fee

    # Output Invoice
    print("\n=======================================")
    print("           CLUB MEMBERSHIP             ")
    print("=======================================")
    print(f"Welcome, {member_name}")
    print(f"Prepaid Term: {months_mbr} months")
    print("---------------------------------------")
    print(f"One-Time Joining Fee: ${registry_fee:,.2f}")
    
    membership_dues = monthly_fee_rate * months_mbr
    print(f"Membership Dues:      ${membership_dues:,.2f}")
    
    if equipment_rnt == 'Y':
        rental_total = equip_fee_rate * months_mbr
        print(f"Equipment Rental:     ${rental_total:,.2f}")
        
    print("---------------------------------------")
    print(f"TOTAL REGISTRATION:   ${total_bill:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
