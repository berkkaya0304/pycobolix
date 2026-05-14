from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- FAST FILL GAS STATION ---")
    print("Select Fuel Grade: ")
    print("1=Regular 87 ($3.50)")
    print("2=Plus 89 ($3.80)")
    print("3=Premium 93 ($4.20)")
    print("4=Diesel ($4.50)")
    
    try:
        fuel_type = input().strip()
    except EOFError:
        return

    try:
        gallons_pumped = Decimal(input("Gallons Pumped: ").strip())
    except (EOFError, ValueError):
        gallons_pumped = Decimal('0.00')

    car_wash_choice = input("Add Basic Car Wash for $8.00? (Y/N): ").strip().upper()

    # Calculate Sale
    pricing_map = {
        '1': Decimal('3.50'),
        '2': Decimal('3.80'),
        '3': Decimal('4.20'),
        '4': Decimal('4.50')
    }

    price_per_gal = pricing_map.get(fuel_type)
    if price_per_gal is None:
        print("Invalid Selection. Defaulting to Regular.")
        price_per_gal = Decimal('3.50')

    fuel_total = (gallons_pumped * price_per_gal).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    wash_fee = Decimal('0.00')
    if car_wash_choice == 'Y':
        wash_fee = Decimal('8.00')

    grand_total = fuel_total + wash_fee

    # Print Receipt
    print("\n")
    print("=======================================")
    print("          FUEL PUMP RECEIPT            ")
    print("=======================================")
    print(f"Gallons Dispensed: {gallons_pumped:g}")
    print(f"Price per Gallon:  ${price_per_gal:.2f}")
    print("---------------------------------------")
    print(f"Fuel Charge:       {format_currency(fuel_total)}")
    
    if car_wash_choice == 'Y':
        print(f"Car Wash Add-on:   {format_currency(wash_fee)}")
        print("   -> Wash Code: 49813 <-")
        
    print("---------------------------------------")
    print(f"TOTAL SALE:        {format_currency(grand_total)}")
    print("=======================================")

if __name__ == "__main__":
    main()
