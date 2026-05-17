from decimal import Decimal, ROUND_HALF_UP

def calculate_stay(guest_data):
    # Base Rate Mapping
    view_rates = {
        1: Decimal('150.00'), # Standard
        2: Decimal('250.00'), # Ocean
        3: Decimal('500.00')  # Suite
    }
    
    base_rate = view_rates.get(guest_data['view_type'], Decimal('150.00'))
    
    # Season Multiplier
    season_mult = Decimal('1.50') if guest_data['season'] == 'P' else Decimal('1.00')
    
    # Calculations
    nightly_rate = base_rate * season_mult
    subtotal = nightly_rate * guest_data['nights']
    taxes = subtotal * Decimal('0.125')
    grand_total = subtotal + taxes
    
    return {
        'nightly_rate': nightly_rate,
        'subtotal': subtotal,
        'taxes': taxes,
        'grand_total': grand_total
    }

def print_confirmation(guest_data, totals):
    def format_currency(value):
        return f"${value:,.2f}"

    print("\n====================================")
    print("       BOOKING CONFIRMATION         ")
    print("====================================")
    print(f"Guest:  {guest_data['guest']}")
    print(f"Nights: {guest_data['nights']}")
    print("------------------------------------")
    print(f"Est. Nightly Rate: {format_currency(totals['nightly_rate'])}")
    print(f"Room Subtotal:     {format_currency(totals['subtotal'])}")
    print(f"Taxes (12.5%):     {format_currency(totals['taxes'])}")
    print("------------------------------------")
    print(f"TOTAL STAY COST:   {format_currency(totals['grand_total'])}")
    print("====================================")

def main():
    print("--- SEASIDE RESORT BOOKING ---")
    
    try:
        guest = input("Guest Name: ")
        season = input("Season (P=Peak, O=Off-Peak): ").upper()
        view_type = int(input("Room View (1=Std, 2=Ocean, 3=Suite): "))
        nights = int(input("Number of Nights: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for View and Nights.")
        return

    guest_data = {
        'guest': guest,
        'season': season,
        'view_type': view_type,
        'nights': Decimal(nights)
    }

    totals = calculate_stay(guest_data)
    print_confirmation(guest_data, totals)

if __name__ == "__main__":
    main()
