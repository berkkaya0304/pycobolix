def main():
    print("--- SPARKLE CAR WASH ---")
    license_plate = input("License Plate: ")
    wash_package = input("Package (1=Basic $10, 2=Prem $18, 3=Ult $25): ").strip()
    wants_wax = input("Add Hand Wax ($15)? (Y/N): ").strip().upper() == 'Y'
    try:
        tip_amount = float(input("Add Tip Amount for the crew ($): "))
    except ValueError:
        tip_amount = 0.0

    if wash_package == '1':
        base_fee = 10.00
    elif wash_package == '2':
        base_fee = 18.00
    elif wash_package == '3':
        base_fee = 25.00
    else:
        print("Invalid pkg, defaulted to Basic.")
        base_fee = 10.00

    wax_fee = 15.00 if wants_wax else 0.0
    sub_total = base_fee + wax_fee
    total_charge = sub_total + tip_amount

    print("\n=============================================")
    print("           WASH TICKET & RECEIPT             ")
    print("=============================================")
    print(f"Vehicle: {license_plate}")
    print("---------------------------------------------")
    print(f"Wash Package Fee:    ${base_fee:6.2f}")
    
    if wax_fee > 0:
        print(f"Hand Wax Add-on:     ${wax_fee:6.2f}")
        
    print("---------------------------------------------")
    print(f"Subtotal:            ${sub_total:6.2f}")
    print(f"Crew Tip:            ${tip_amount:6.2f}")
    print("=============================================")
    print(f"TOTAL CHARGED:       ${total_charge:6.2f}")
    print("   Thank you for choosing Sparkle!           ")
    print("=============================================")

if __name__ == "__main__":
    main()
