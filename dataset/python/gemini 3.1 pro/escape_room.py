def main():
    print("--- ENIGMA ESCAPE ROOMS ---")
    group_name = input("Group/Team Name: ")
    try:
        num_players = int(input("Number of Players: "))
    except ValueError:
        num_players = 0
    difficulty = input("Room Difficulty (1=Easy, 2=Med, 3=Hard +$5): ").strip()
    is_weekend = input("Is booking on Weekend (Fri-Sun)? (Y/N): ").strip().upper() == 'Y'

    base_ticket = 25.00
    if difficulty == '3':
        diff_surcharge = 5.00
    else:
        diff_surcharge = 0.0

    ticket_price = base_ticket + diff_surcharge
    room_tot = num_players * ticket_price

    weekend_fee = 20.00 if is_weekend else 0.0
    final_bill = room_tot + weekend_fee

    print("\n========================================")
    print("          BOOKING CONFIRMATION          ")
    print("========================================")
    print(f"Team: {group_name} ({num_players} players)")
    print("----------------------------------------")
    print(f"Price Per Ticket:    ${ticket_price:6.2f}")
    print(f"Base Room Charge:    ${room_tot:6.2f}")
    
    if weekend_fee > 0:
        print(f"Weekend Premium:     ${weekend_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${final_bill:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
