def main():
    print("--- CITY CENTER PARKING GARAGE ---")
    try:
        ticket_num = int(input("Ticket Number: "))
    except ValueError:
        ticket_num = 0
    try:
        hours_parked = float(input("Hours Parked (e.g. 3.5): "))
    except ValueError:
        hours_parked = 0.0
    valet_service = input("Valet Service used? (Y/N): ").strip().upper() == 'Y'
    lost_ticket = input("Is ticket lost? (Y/N): ").strip().upper() == 'Y'

    hourly_rate = 4.50
    daily_max = 25.00
    valet_flat = 15.00
    lost_penalty = 40.00

    extra_fee = 0.0

    if lost_ticket:
        time_charge = daily_max
        extra_fee = lost_penalty
    else:
        time_charge = hours_parked * hourly_rate
        if time_charge > daily_max:
            time_charge = daily_max

    if valet_service:
        extra_fee += valet_flat

    total_due = time_charge + extra_fee

    print("\n===================================")
    print("        PARKING EXIT TICKET        ")
    print("===================================")
    print(f"Ticket #: {ticket_num:06d}")
    print(f"Time In Garage: {hours_parked:.2f} hours")
    print("-----------------------------------")
    print(f"Parking Fee:     ${time_charge:6.2f}")
    
    if extra_fee > 0:
        print(f"Additional Fees: ${extra_fee:6.2f}")
        
    print("-----------------------------------")
    print(f"TOTAL TO PAY:    ${total_due:6.2f}")
    print("===================================")

if __name__ == "__main__":
    main()
