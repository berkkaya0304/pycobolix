import sys

def main():
    print("--- FIT-LIFE CLASS BOOKING ---")
    
    member_name = input("Member Name: ").strip()
    
    try:
        class_selection = int(input("Class (1=Yoga $15, 2=Spin $20, 3=Pilates $25): "))
    except ValueError:
        class_selection = 0

    try:
        guest_passes = int(input("Number of Non-Member Guests ($10 ea): "))
    except ValueError:
        guest_passes = 0

    towel_rental = input("Rent Premium Towel Service ($3)? (Y/N): ").strip().upper()

    # Determine Class Fee
    if class_selection == 1:
        class_fee = 15.00
    elif class_selection == 2:
        class_fee = 20.00
    elif class_selection == 3:
        class_fee = 25.00
    else:
        class_fee = 15.00

    # Calculate Guest Fee
    guest_fee = guest_passes * 10.00

    # Determine Towel Fee
    towel_fee = 3.00 if towel_rental == 'Y' else 0.00

    # Calculate Total
    total_chg = class_fee + guest_fee + towel_fee

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("           CLASS RESERVATION            ")
    print("========================================")
    print(f"Member: {member_name}")
    print("----------------------------------------")
    print(f"Class Base Fee:       {format_currency(class_fee)}")
    
    if guest_passes > 0:
        print(f"Guest Passes ({guest_passes}):      {format_currency(guest_fee)}")
    
    if towel_rental == 'Y':
        print(f"Towel Service Option: {format_currency(towel_fee)}")
        
    print("----------------------------------------")
    print(f"TOTAL CHARGED:        {format_currency(total_chg)}")
    print("========================================")

if __name__ == "__main__":
    main()
