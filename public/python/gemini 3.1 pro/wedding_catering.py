def main():
    print("--- ELEGANCE EVENT CATERING ---")
    couple_name = input("Couple's Names: ")
    try:
        guest_count = int(input("Expected Guest Count: "))
    except ValueError:
        guest_count = 0
    menu_tier = input("Menu (1=Buffet $35, 2=Standard $50, 3=Prem $85): ").strip()
    wants_bar = input("Add Full Open Bar ($30 per head)? (Y/N): ").strip().upper() == 'Y'

    if menu_tier == '1':
        cost_per_head = 35.00
    elif menu_tier == '2':
        cost_per_head = 50.00
    elif menu_tier == '3':
        cost_per_head = 85.00
    else:
        cost_per_head = 50.00

    food_tot = guest_count * cost_per_head

    bar_cost = 0.0
    if wants_bar:
        bar_cost = guest_count * 30.00

    gratuity = (food_tot + bar_cost) * 0.20
    grand_total = food_tot + bar_cost + gratuity

    print("\n========================================")
    print("            CATERING ESTIMATE           ")
    print("========================================")
    print(f"Event: The {couple_name} Wedding")
    print(f"Guests Expected: {guest_count:03d}")
    print("----------------------------------------")
    print(f"Food & Dining Cost:  ${food_tot:9.2f}")
    
    if bar_cost > 0:
        print(f"Open Bar Setup:      ${bar_cost:9.2f}")
        
    print(f"Staffing/Gratuity(20%) ${gratuity:8.2f}")
    print("----------------------------------------")
    print(f"ESTIMATED TOTAL:     ${grand_total:9.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
