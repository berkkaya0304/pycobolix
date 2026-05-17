def main():
    # Ticket information
    guest_name = ""
    adult_tkts = 0
    child_tkts = 0

    # Upgrades
    fast_pass = 'N'
    meal_plan = 'N'

    # Pricing
    ADULT_FARE = 85.00
    CHILD_FARE = 60.00
    FP_COST = 45.00
    MP_COST = 30.00

    # Totals
    tkt_total = 0.0
    upgrade_total = 0.0
    grand_total = 0.0
    head_count = 0

    # Display header
    print("--- ADVENTURE WORLD TICKETS ---")
    guest_name = input("Lead Guest Name: ")
    adult_tkts = int(input("Adult Tickets ($85 each): "))
    child_tkts = int(input("Child Tickets ($60 each): "))
    fast_pass = input("Add Fast-Pass ($45/person)? (Y/N): ").upper()
    meal_plan = input("Add All-Day Dining ($30/person)? (Y/N): ").upper()

    # Calculate fees
    tkt_total = (adult_tkts * ADULT_FARE) + (child_tkts * CHILD_FARE)
    head_count = adult_tkts + child_tkts

    upgrade_total = 0.0
    if fast_pass == 'Y':
        upgrade_total += head_count * FP_COST
    if meal_plan == 'Y':
        upgrade_total += head_count * MP_COST

    grand_total = tkt_total + upgrade_total

    # Print receipt
    print("\n========================================")
    print("       ADVENTURE WORLD RECEIPT          ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print(f"Headcount: {head_count} people")
    print("----------------------------------------")
    if adult_tkts > 0:
        print(f"Adult Tickets ({adult_tkts}):    ${adult_tkts * ADULT_FARE:,.2f}")
    if child_tkts > 0:
        print(f"Child Tickets ({child_tkts}):    ${child_tkts * CHILD_FARE:,.2f}")
    print(f"Base Ticket Total:    ${tkt_total:,.2f}")
    print("----------------------------------------")
    if upgrade_total > 0:
        print(f"Add-ons (FP/Dining):  ${upgrade_total:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL PAYABLE:        ${grand_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
