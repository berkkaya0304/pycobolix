def main():
    print("--- ELEGANCE EVENT CATERING ---")
    couple_name = input("Couple's Names: ")
    guest_count = int(input("Expected Guest Count: "))
    print("Menu (1=Buffet $35, 2=Standard $50, 3=Prem $85): ")
    menu_tier = int(input())
    open_bar = input("Add Full Open Bar ($30 per head)? (Y/N): ").upper()

    if menu_tier == 1:
        cost_per_head = 35.00
    elif menu_tier == 2:
        cost_per_head = 50.00
    elif menu_tier == 3:
        cost_per_head = 85.00
    else:
        cost_per_head = 50.00

    food_total = guest_count * cost_per_head
    bar_cost = guest_count * 30.00 if open_bar == 'Y' else 0.0
    gratuity = (food_total + bar_cost) * 0.20
    grand_total = food_total + bar_cost + gratuity

    print("\n" + "="*40)
    print("            CATERING ESTIMATE           ")
    print("="*40)
    print(f"Event: The {couple_name} Wedding")
    print(f"Guests Expected: {guest_count}")
    print("-"*40)
    print(f"Food & Dining Cost:  ${food_total:,.2f}")
    if bar_cost > 0:
        print(f"Open Bar Setup:      ${bar_cost:,.2f}")
    print(f"Staffing/Gratuity(20%) ${gratuity:,.2f}")
    print("-"*40)
    print(f"ESTIMATED TOTAL:     ${grand_total:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
