# ESCAPE-ROOM - Enigma Escape Rooms
# Converted from COBOL to Python

def main():
    BASE_TICKET = 25.00

    print("--- ENIGMA ESCAPE ROOMS ---")
    group_name = input("Group/Team Name: ")
    num_players = int(input("Number of Players: "))
    difficulty = int(input("Room Difficulty (1=Easy, 2=Med, 3=Hard +$5): "))
    is_weekend = input("Is booking on Weekend (Fri-Sun)? (Y/N): ").strip().upper()

    diff_surcharge = 5.00 if difficulty == 3 else 0.0
    ticket_price = BASE_TICKET + diff_surcharge
    room_tot = num_players * ticket_price

    weekend_fee = 20.00 if is_weekend == 'Y' else 0.0
    final_bill = room_tot + weekend_fee

    print("")
    print("========================================")
    print("          BOOKING CONFIRMATION          ")
    print("========================================")
    print(f"Team: {group_name} ({num_players} players)")
    print("----------------------------------------")
    print(f"Price Per Ticket:    ${ticket_price:,.2f}")
    print(f"Base Room Charge:    ${room_tot:,.2f}")
    if weekend_fee > 0:
        print(f"Weekend Premium:     ${weekend_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${final_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
