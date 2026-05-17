def main():
    print("--- FAST FILL GAS STATION ---")
    print("Select Fuel Grade: ")
    print("1=Regular 87 ($3.50)")
    print("2=Plus 89 ($3.80)")
    print("3=Premium 93 ($4.20)")
    print("4=Diesel ($4.50)")
    
    try:
        fuel_type = int(input().strip())
    except ValueError:
        fuel_type = 1
        print("Invalid input. Defaulting to Regular.")
    
    try:
        gallons = float(input("Gallons Pumped: ").strip())
    except ValueError:
        gallons = 0.0
        print("Invalid input. Defaulting to 0 gallons.")
    
    car_wash = input("Add Basic Car Wash for $8.00? (Y/N): ").strip().upper()
    wants_wash = car_wash == 'Y'
    
    fuel_total, price_per_gal, wash_fee = calculate_sale(fuel_type, gallons, wants_wash)
    grand_total = fuel_total + wash_fee
    
    print_receipt(gallons, price_per_gal, fuel_total, wants_wash, wash_fee, grand_total)

def calculate_sale(fuel_type, gallons, wants_wash):
    fuel_prices = {
        1: 3.50,
        2: 3.80,
        3: 4.20,
        4: 4.50
    }
    
    price_per_gal = fuel_prices.get(fuel_type, 3.50)
    if fuel_type not in fuel_prices:
        print("Invalid Selection. Defaulting to Regular.")
    
    fuel_total = gallons * price_per_gal
    wash_fee = 8.00 if wants_wash else 0.0
    
    return fuel_total, price_per_gal, wash_fee

def print_receipt(gallons, price_per_gal, fuel_total, wants_wash, wash_fee, grand_total):
    print("\n=======================================")
    print("          FUEL PUMP RECEIPT            ")
    print("=======================================")
    print(f"Gallons Dispensed: {gallons:.2f}")
    print(f"Price per Gallon:  ${price_per_gal:.2f}")
    print("---------------------------------------")
    print(f"Fuel Charge:       ${fuel_total:,.2f}")
    
    if wants_wash:
        print(f"Car Wash Add-on:   ${wash_fee:,.2f}")
        print("   -> Wash Code: 49813 <-")
    
    print("---------------------------------------")
    print(f"TOTAL SALE:        ${grand_total:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
