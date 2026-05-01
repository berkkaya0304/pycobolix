def main():
    print("--- ADVENTURE WORLD TICKETS ---")
    guest_name = input("Lead Guest Name: ")
    try:
        adult_tkts = int(input("Adult Tickets ($85 each): "))
    except ValueError:
        adult_tkts = 0
    try:
        child_tkts = int(input("Child Tickets ($60 each): "))
    except ValueError:
        child_tkts = 0
    fast_pass = input("Add Fast-Pass ($45/person)? (Y/N): ").strip().upper() == 'Y'
    meal_plan = input("Add All-Day Dining ($30/person)? (Y/N): ").strip().upper() == 'Y'

    adult_fare = 85.00
    child_fare = 60.00
    fp_cost = 45.00
    mp_cost = 30.00

    tkt_total = (adult_tkts * adult_fare) + (child_tkts * child_fare)
    head_count = adult_tkts + child_tkts
    
    upgrade_total = 0.0
    if fast_pass:
        upgrade_total += (head_count * fp_cost)
        
    if meal_plan:
        upgrade_total += (head_count * mp_cost)

    grand_total = tkt_total + upgrade_total

    print("\n========================================")
    print("       ADVENTURE WORLD RECEIPT          ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print(f"Headcount: {head_count:03d} people")
    print("----------------------------------------")
    
    if adult_tkts > 0:
        print(f"Adult Tickets ({adult_tkts:02d}):    ${adult_tkts * adult_fare:6.2f}")
    if child_tkts > 0:
        print(f"Child Tickets ({child_tkts:02d}):    ${child_tkts * child_fare:6.2f}")
        
    print(f"Base Ticket Total:    ${tkt_total:6.2f}")
    print("----------------------------------------")
    
    if upgrade_total > 0:
        print(f"Add-ons (FP/Dining):  ${upgrade_total:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL PAYABLE:        ${grand_total:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
