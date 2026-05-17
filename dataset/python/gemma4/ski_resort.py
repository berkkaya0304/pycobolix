def main():
    print("--- SNOW PEAK RESORT ---")
    
    skier_name = input("Skier Name: ")
    pass_type_input = input("Pass (1=Half Day $60, 2=Full $95, 3=3-Day $250): ")
    rent_gear_input = input("Rent Skis/Snowboard ($45)? (Y/N): ").upper()
    rent_helmet_input = input("Rent Safety Helmet ($15)? (Y/N): ").upper()

    # Determine Lift Ticket Price
    if pass_type_input == '1':
        lift_ticket = 60.00
    elif pass_type_input == '2':
        lift_ticket = 95.00
    elif pass_type_input == '3':
        lift_ticket = 250.00
    else:
        lift_ticket = 95.00

    # Determine Rental Fees
    gear_fee = 45.00 if rent_gear_input == 'Y' else 0.00
    helmet_fee = 15.00 if rent_helmet_input == 'Y' else 0.00

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
