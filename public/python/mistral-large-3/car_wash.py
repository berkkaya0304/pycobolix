def main():
    print("--- SPARKLE CAR WASH ---")
    license_plate = input("License Plate: ").strip()
    wash_package = int(input("Package (1=Basic $10, 2=Prem $18, 3=Ult $25): "))
    wax_option = input("Add Hand Wax ($15)? (Y/N): ").strip().upper()
    tip_amount = float(input("Add Tip Amount for the crew ($): "))

    base_fee, wax_fee, sub_total, total_charge = calc_fees(wash_package, wax_option, tip_amount)
    issue_ticket(license_plate, base_fee, wax_fee, sub_total, tip_amount, total_charge)

def calc_fees(wash_package, wax_option, tip_amount):
    if wash_package == 1:
        base_fee = 10.00
    elif wash_package == 2:
        base_fee = 18.00
    elif wash_package == 3:
        base_fee = 25.00
    else:
        base_fee = 10.00
        print("Invalid pkg, defaulted to Basic.")

    wax_fee = 15.00 if wax_option == 'Y' else 0.00
    sub_total = base_fee + wax_fee
    total_charge = sub_total + tip_amount
    return base_fee, wax_fee, sub_total, total_charge

def issue_ticket(license_plate, base_fee, wax_fee, sub_total, tip_amount, total_charge):
    print("\n=============================================")
    print("           WASH TICKET & RECEIPT             ")
    print("=============================================")
    print(f"Vehicle: {license_plate}")
    print("---------------------------------------------")
    print(f"Wash Package Fee:    ${base_fee:,.2f}")
    if wax_fee > 0:
        print(f"Hand Wax Add-on:     ${wax_fee:,.2f}")
    print("---------------------------------------------")
    print(f"Subtotal:            ${sub_total:,.2f}")
    print(f"Crew Tip:            ${tip_amount:,.2f}")
    print("=============================================")
    print(f"TOTAL CHARGED:       ${total_charge:,.2f}")
    print("   Thank you for choosing Sparkle!           ")
    print("=============================================")

if __name__ == "__main__":
    main()
