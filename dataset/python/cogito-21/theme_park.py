def main():
    print("--- ADVENTURE WORLD TICKETS ---")
    guest_name = input("Lead Guest Name: ")
    
    try:
        adult_tickets = int(input("Adult Tickets ($85 each): "))
        child_tickets = int(input("Child Tickets ($60 each): "))
    except ValueError:
        print("Please enter valid numbers for tickets.")
        return

    fast_pass = input("Add Fast-Pass ($45/person)? (Y/N): ").upper() == 'Y'
    meal_plan = input("Add All-Day Dining ($30/person)? (Y/N): ").upper() == 'Y'

    ticket_total, upgrade_total, grand_total, head_count = calculate_fees(
        adult_tickets, child_tickets, fast_pass, meal_plan
    )

    print_pass(guest_name, adult_tickets, child_tickets, 
               ticket_total, upgrade_total, grand_total, head_count)

def calculate_fees(adult_tickets, child_tickets, fast_pass, meal_plan):
    ADULT_FARE = 85.00
    CHILD_FARE = 60.00
    FP_COST = 45.00
    MP_COST = 30.00

    ticket_total = (adult_tickets * ADULT_FARE) + (child_tickets * CHILD_FARE)
    head_count = adult_tickets + child_tickets

    upgrade_total = 0.0
    if fast_pass:
        upgrade_total += head_count * FP_COST
    if meal_plan:
        upgrade_total += head_count * MP_COST

    grand_total = ticket_total + upgrade_total

    return ticket_total, upgrade_total, grand_total, head_count

def print_pass(guest_name, adult_tickets, child_tickets, 
               ticket_total, upgrade_total, grand_total, head_count):
    print("\n" + "=" * 40)
    print("       ADVENTURE WORLD RECEIPT          ")
    print("=" * 40)
    print(f"Guest: {guest_name}")
    print(f"Headcount: {head_count} people")
    print("-" * 40)
    
    if adult_tickets > 0:
        print(f"Adult Tickets ({adult_tickets}):    ${adult_tickets * 85.00:,.2f}")
    if child_tickets > 0:
        print(f"Child Tickets ({child_tickets}):    ${child_tickets * 60.00:,.2f}")
    
    print(f"Base Ticket Total:    ${ticket_total:,.2f}")
    print("-" * 40)
    
    if upgrade_total > 0:
        print(f"Add-ons (FP/Dining):  ${upgrade_total:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL PAYABLE:        ${grand_total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
