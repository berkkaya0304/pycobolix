def main():
    print("--- SNOW PEAK RESORT ---")
    skier_name = input("Skier Name: ").strip()
    pass_type = int(input("Pass (1=Half Day $60, 2=Full $95, 3=3-Day $250): "))
    rent_gear = input("Rent Skis/Snowboard ($45)? (Y/N): ").strip().upper() == 'Y'
    rent_helmet = input("Rent Safety Helmet ($15)? (Y/N): ").strip().upper() == 'Y'

    lift_ticket = 0.0
    if pass_type == 1:
        lift_ticket = 60.00
    elif pass_type == 2:
        lift_ticket = 95.00
    elif pass_type == 3:
        lift_ticket = 250.00
    else:
        lift_ticket = 95.00

    gear_fee = 45.00 if rent_gear else 0.0
    helmet_fee = 15.00 if rent_helmet else 0.0
    total_cost = lift_ticket + gear_fee + helmet_fee

    print("\n========================================")
    print("           LIFT PASS ISSUED             ")
    print("========================================")
    print(f"Skier: {skier_name}")
    print("----------------------------------------")
    print(f"Lift Ticket Access:  ${lift_ticket:,.2f}")
    if gear_fee > 0:
        print(f"Equipment Rental:    ${gear_fee:,.2f}")
    if helmet_fee > 0:
        print(f"Helmet Rental:       ${helmet_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL PAID:          ${total_cost:,.2f}")
    print("  >>> SEE YOU ON THE SLOPES! <<<        ")
    print("========================================")

if __name__ == "__main__":
    main()
