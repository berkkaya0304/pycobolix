from decimal import Decimal, getcontext

def main():
    print("--- SEASIDE RESORT BOOKING ---")
    guest = input("Guest Name: ").strip()
    season = input("Season (P=Peak, O=Off-Peak): ").strip().upper()
    view_type = int(input("Room View (1=Std, 2=Ocean, 3=Suite): ").strip())
    nights = int(input("Number of Nights: ").strip())

    rates = calculate_stay(season, view_type, nights)
    print_confirmation(guest, nights, rates)

def calculate_stay(season, view_type, nights):
    getcontext().prec = 6

    # Determine base rate
    if view_type == 1:
        base_rate = Decimal('150.00')
    elif view_type == 2:
        base_rate = Decimal('250.00')
    elif view_type == 3:
        base_rate = Decimal('500.00')
    else:
        base_rate = Decimal('150.00')

    # Determine season multiplier
    season_mult = Decimal('1.50') if season == 'P' else Decimal('1.00')

    nightly_rate = base_rate * season_mult
    subtotal = nightly_rate * nights
    taxes = subtotal * Decimal('0.125')
    grand_total = subtotal + taxes

    return {
        'base_rate': base_rate,
        'season_mult': season_mult,
        'nightly_rate': nightly_rate,
        'subtotal': subtotal,
        'taxes': taxes,
        'grand_total': grand_total
    }

def print_confirmation(guest, nights, rates):
    def format_currency(value):
        return f"${value:,.2f}"

    print("\n====================================")
    print("       BOOKING CONFIRMATION         ")
    print("====================================")
    print(f"Guest:  {guest}")
    print(f"Nights: {nights}")
    print("------------------------------------")
    print(f"Est. Nightly Rate: {format_currency(rates['nightly_rate'])}")
    print(f"Room Subtotal:     {format_currency(rates['subtotal'])}")
    print(f"Taxes (12.5%):     {format_currency(rates['taxes'])}")
    print("------------------------------------")
    print(f"TOTAL STAY COST:   {format_currency(rates['grand_total'])}")
    print("====================================")

if __name__ == "__main__":
    main()
