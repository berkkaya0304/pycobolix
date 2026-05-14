"""
Adventure World Theme Park Tickets
Converted from COBOL (theme_park.cbl) to Python
"""


def main():
    adult_fare, child_fare = 85.00, 60.00
    fp_cost, mp_cost = 45.00, 30.00

    print("--- ADVENTURE WORLD TICKETS ---")
    guest_name = input("Lead Guest Name: ")
    adult_tkts = int(input("Adult Tickets ($85 each): "))
    child_tkts = int(input("Child Tickets ($60 each): "))
    fast_pass = input("Add Fast-Pass ($45/person)? (Y/N): ").strip().upper()
    meal_plan = input("Add All-Day Dining ($30/person)? (Y/N): ").strip().upper()

    tkt_total = (adult_tkts * adult_fare) + (child_tkts * child_fare)
    head_count = adult_tkts + child_tkts

    upgrade_total = 0.0
    if fast_pass == "Y":
        upgrade_total += head_count * fp_cost
    if meal_plan == "Y":
        upgrade_total += head_count * mp_cost

    grand_total = tkt_total + upgrade_total

    print()
    print("========================================")
    print("       ADVENTURE WORLD RECEIPT          ")
    print("========================================")
    print(f"Guest: {guest_name}")
    print(f"Headcount: {head_count} people")
    print("----------------------------------------")
    print(f"Base Ticket Total:    ${tkt_total:>9,.2f}")
    print("----------------------------------------")
    if upgrade_total > 0:
        print(f"Add-ons (FP/Dining):  ${upgrade_total:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL PAYABLE:        ${grand_total:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
