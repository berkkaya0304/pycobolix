def main():
    print("--- CITY CENTER PARKING GARAGE ---")
    ticket_num = input("Ticket Number: ")
    hours_parked = float(input("Hours Parked (e.g. 3.5): "))
    valet_service = input("Valet Service used? (Y/N): ").upper()
    lost_ticket = input("Is ticket lost? (Y/N): ").upper()

    time_charge = 0.0
    extra_fee = 0.0
    total_due = 0.0

    hourly_rate = 4.50
    daily_max = 25.00
    valet_flat = 15.00
    lost_penalty = 40.00

    if lost_ticket == 'Y':
        time_charge = daily_max
        extra_fee = lost_penalty
    else:
        time_charge = hours_parked * hourly_rate
        if time_charge > daily_max:
            time_charge = daily_max

    if valet_service == 'Y':
        extra_fee += valet_flat

    total_due = time_charge + extra_fee

    print("\n===================================")
    print("        PARKING EXIT TICKET        ")
    print("===================================")
    print(f"Ticket #: {ticket_num}")
    print(f"Time In Garage: {hours_parked} hours")
    print("-----------------------------------")
    print(f"Parking Fee:     ${time_charge:.2f}")
    
    if extra_fee > 0:
        print(f"Additional Fees: ${extra_fee:.2f}")
    
    print("-----------------------------------")
    print(f"TOTAL TO PAY:    ${total_due:.2f}")
    print("===================================")

if __name__ == "__main__":
    main()
