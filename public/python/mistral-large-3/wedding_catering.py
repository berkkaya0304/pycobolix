def wedding_catering_quote():
    print("--- ELEGANCE EVENT CATERING ---")
    couple_name = input("Couple's Names: ").strip()
    guest_count = int(input("Expected Guest Count: ").strip())
    menu_tier = int(input("Menu (1=Buffet $35, 2=Standard $50, 3=Prem $85): ").strip())
    open_bar = input("Add Full Open Bar ($30 per head)? (Y/N): ").strip().upper() == 'Y'

    cost_per_head = {
        1: 35.00,
        2: 50.00,
        3: 85.00
    }.get(menu_tier, 50.00)

    food_total = guest_count * cost_per_head
    bar_cost = guest_count * 30.00 if open_bar else 0.0
    gratuity = (food_total + bar_cost) * 0.20
    grand_total = food_total + bar_cost + gratuity

    def format_currency(value):
        return f"${value:,.2f}"

    print("\n========================================")
    print("            CATERING ESTIMATE           ")
    print("========================================")
    print(f"Event: The {couple_name} Wedding")
    print(f"Guests Expected: {guest_count}")
    print("----------------------------------------")
    print(f"Food & Dining Cost:  {format_currency(food_total)}")
    if bar_cost > 0:
        print(f"Open Bar Setup:      {format_currency(bar_cost)}")
    print(f"Staffing/Gratuity(20%) {format_currency(gratuity)}")
    print("----------------------------------------")
    print(f"ESTIMATED TOTAL:     {format_currency(grand_total)}")
    print("========================================")

if __name__ == "__main__":
    wedding_catering_quote()
