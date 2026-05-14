def escape_room():
    print("--- ENIGMA ESCAPE ROOMS ---")

    group_name = input("Group/Team Name: ").strip()
    num_players = int(input("Number of Players: ").strip())
    difficulty = int(input("Room Difficulty (1=Easy, 2=Med, 3=Hard +$5): ").strip())
    is_weekend = input("Is booking on Weekend (Fri-Sun)? (Y/N): ").strip().upper() == 'Y'

    base_ticket = 25.00
    diff_surcharge = 5.00 if difficulty == 3 else 0.00
    ticket_price = base_ticket + diff_surcharge
    room_total = num_players * ticket_price
    weekend_fee = 20.00 if is_weekend else 0.00
    final_bill = room_total + weekend_fee

    print("")
    print("=" * 40)
    print("          BOOKING CONFIRMATION          ")
    print("=" * 40)
    print(f"Team: {group_name} ({num_players} players)")
    print("-" * 40)
    print(f"Price Per Ticket:    ${ticket_price:,.2f}")
    print(f"Base Room Charge:    ${room_total:,.2f}")

    if weekend_fee > 0:
        print(f"Weekend Premium:     ${weekend_fee:,.2f}")

    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:    ${final_bill:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    escape_room()
