def gym_class_booking():
    print("--- FIT-LIFE CLASS BOOKING ---")

    member_name = input("Member Name: ").strip()
    class_selection = int(input("Class (1=Yoga $15, 2=Spin $20, 3=Pilates $25): "))
    guest_passes = int(input("Number of Non-Member Guests ($10 ea): "))
    towel_rental = input("Rent Premium Towel Service ($3)? (Y/N): ").strip().upper()

    class_fee = 0.0
    if class_selection == 1:
        class_fee = 15.00
    elif class_selection == 2:
        class_fee = 20.00
    elif class_selection == 3:
        class_fee = 25.00
    else:
        class_fee = 15.00

    guest_fee = guest_passes * 10.00
    towel_fee = 3.00 if towel_rental == 'Y' else 0.0
    total_charge = class_fee + guest_fee + towel_fee

    print("\n========================================")
    print("           CLASS RESERVATION            ")
    print("========================================")
    print(f"Member: {member_name}")
    print("----------------------------------------")
    print(f"Class Base Fee:       ${class_fee:.2f}")

    if guest_passes > 0:
        print(f"Guest Passes ({guest_passes}):      ${guest_fee:.2f}")

    if towel_rental == 'Y':
        print(f"Towel Service Option: ${towel_fee:.2f}")

    print("----------------------------------------")
    print(f"TOTAL CHARGED:        ${total_charge:.2f}")
    print("========================================")

if __name__ == "__main__":
    gym_class_booking()
