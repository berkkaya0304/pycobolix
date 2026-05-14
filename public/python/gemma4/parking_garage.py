from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    # Constants (Fees)
    HOURLY_RATE = Decimal("4.50")
    DAILY_MAX = Decimal("25.00")
    VALET_FLAT = Decimal("15.00")
    LOST_PENALTY = Decimal("40.00")

    print("--- CITY CENTER PARKING GARAGE ---")
    
    try:
        ticket_num = input("Ticket Number: ")
        hours_parked = Decimal(input("Hours Parked (e.g. 3.5): "))
        valet_service = input("Valet Service used? (Y/N): ").strip().upper()
        lost_ticket = input("Is ticket lost? (Y/N): ").strip().upper()
    except Exception as e:
        print(f"Invalid input: {e}")
        return

    # Compute Fare
    extra_fee = Decimal("0.00")
    
    if lost_ticket == 'Y':
        time_charge = DAILY_MAX
        extra_fee = LOST_PENALTY
    else:
        time_charge = hours_parked * HOURLY_RATE
        if time_charge > DAILY_MAX:
            time_charge = DAILY_MAX

    if valet_service == 'Y':
        extra_fee += VALET_FLAT

    total_due = time_charge + extra_fee

    # Issue Exit Pass
    print("\n===================================")
    print("        PARKING EXIT TICKET        ")
    print("===================================")
    print(f"Ticket #: {ticket_num}")
    print(f"Time In Garage: {hours_parked} hours")
    print("-----------------------------------")
    print(f"Parking Fee:     {format_currency(time_charge)}")
    
    if extra_fee > 0:
        print(f"Additional Fees: {format_currency(extra_fee)}")
        
    print("-----------------------------------")
    print(f"TOTAL TO PAY:    {format_currency(total_due)}")
    print("===================================")

if __name__ == "__main__":
    main()
