# PARKING-GARAGE - City Center Parking Garage
# Converted from COBOL to Python

def main():
    HOURLY_RATE = 4.50
    DAILY_MAX = 25.00
    VALET_FLAT = 15.00
    LOST_PENALTY = 40.00

    print("--- CITY CENTER PARKING GARAGE ---")
    ticket_num = input("Ticket Number: ")
    hours_parked = float(input("Hours Parked (e.g. 3.5): "))
    valet_service = input("Valet Service used? (Y/N): ").strip().upper()
    lost_ticket = input("Is ticket lost? (Y/N): ").strip().upper()

    extra_fee = 0.0
    if lost_ticket == 'Y':
        time_charge = DAILY_MAX
        extra_fee += LOST_PENALTY
    else:
        time_charge = hours_parked * HOURLY_RATE
        if time_charge > DAILY_MAX:
            time_charge = DAILY_MAX

    if valet_service == 'Y':
        extra_fee += VALET_FLAT

    total_due = time_charge + extra_fee

    print("")
    print("===================================")
    print("        PARKING EXIT TICKET        ")
    print("===================================")
    print(f"Ticket #: {ticket_num}")
    print(f"Time In Garage: {hours_parked} hours")
    print("-----------------------------------")
    print(f"Parking Fee:     ${time_charge:,.2f}")
    if extra_fee > 0:
        print(f"Additional Fees: ${extra_fee:,.2f}")
    print("-----------------------------------")
    print(f"TOTAL TO PAY:    ${total_due:,.2f}")
    print("===================================")

if __name__ == "__main__":
    main()
