def ski_resort():
    print("--- SNOW PEAK RESORT ---")
    skier_name = input("Skier Name: ")
    
    print("Pass (1=Half Day $60, 2=Full $95, 3=3-Day $250): ")
    pass_type = int(input().strip())
    
    rent_gear = input("Rent Skis/Snowboard ($45)? (Y/N): ").strip().upper()
    rent_helmet = input("Rent Safety Helmet ($15)? (Y/N): ").strip().upper()
    
    if pass_type == 1:
        lift_ticket = 60.00
    elif pass_type == 2:
        lift_ticket = 95.00
    elif pass_type == 3:
        lift_ticket = 250.00
    else:
        lift_ticket = 95.00
    
    gear_fee = 45.00 if rent_gear == 'Y' else 0.00
    helmet_fee = 15.00 if rent_helmet == 'Y' else 0.00
    
    total_cost = lift_ticket + gear_fee + helmet_fee
    
    print("\n" + "="*40)
    print("           LIFT PASS ISSUED             ")
    print("="*40)
    print(f"Skier: {skier_name}")
    print("-"*40)
    print(f"Lift Ticket Access:  ${lift_ticket:,.2f}")
    
    if gear_fee > 0:
        print(f"Equipment Rental:    ${gear_fee:,.2f}")
    if helmet_fee > 0:
        print(f"Helmet Rental:       ${helmet_fee:,.2f}")
    
    print("-"*40)
    print(f"TOTAL PAID:          ${total_cost:,.2f}")
    print("  >>> SEE YOU ON THE SLOPES! <<<        ")
    print("="*40)

if __name__ == "__main__":
    ski_resort()
