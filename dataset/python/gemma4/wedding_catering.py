def calculate_wedding_catering():
    print("--- ELEGANCE EVENT CATERING ---")
    
    couple_name = input("Couple's Names: ")
    
    try:
        guest_count = int(input("Expected Guest Count: "))
        menu_tier = int(input("Menu (1=Buffet $35, 2=Standard $50, 3=Prem $85): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for guests and menu tier.")
        return

    open_bar_input = input("Add Full Open Bar ($30 per head)? (Y/N): ").strip().upper()
    wants_bar = open_bar_input == 'Y'

    # Determine cost per head based on menu tier
    if menu_tier == 1:
        cost_per_head = 35.00
    elif menu_tier == 2:
        cost_per_head = 50.00
    elif menu_tier == 3:
        cost_per_head = 85.00
    else:
        cost_per_head = 50.00

    food_tot = guest_count * cost_per_head
    bar_cost = (guest_count * 30.00) if wants_bar else 0.0
    gratuity = (food_tot + bar_cost) * 0.20
    grand_total = food_tot + bar_cost + gratuity

    print("\n========================================")
    print("            CATERING ESTIMATE           ")
    print("========================================")
    print(f"Event: The {couple_name} Wedding")
    print(f"Guests Expected: {guest_count}")
    print("----------------------------------------")
    print(f"Food & Dining Cost:  ${food_tot:,.2f}")
    
    if bar_cost > 0:
        print(f"Open Bar Setup:      ${bar_cost:,.2f}")
        
    print(f"Staffing/Gratuity(20%) ${gratuity:,.2f}")
    print("----------------------------------------")
    print(f"ESTIMATED TOTAL:     ${grand_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    calculate_wedding_catering()
