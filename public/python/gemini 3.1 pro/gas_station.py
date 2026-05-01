def main():
    print("--- FAST FILL GAS STATION ---")
    print("Select Fuel Grade: ")
    print("1=Regular 87 ($3.50)")
    print("2=Plus 89 ($3.80)")
    print("3=Premium 93 ($4.20)")
    print("4=Diesel ($4.50)")
    fuel_type = input("").strip()
    
    try:
        gallons_pumped = float(input("Gallons Pumped: "))
    except ValueError:
        gallons_pumped = 0.0
        
    car_wash = input("Add Basic Car Wash for $8.00? (Y/N): ").strip().upper() == 'Y'

    if fuel_type == '1':
        price_per_gal = 3.50
    elif fuel_type == '2':
        price_per_gal = 3.80
    elif fuel_type == '3':
        price_per_gal = 4.20
    elif fuel_type == '4':
        price_per_gal = 4.50
    else:
        print("Invalid Selection. Defaulting to Regular.")
        price_per_gal = 3.50

    fuel_total = gallons_pumped * price_per_gal
    wash_fee = 8.00 if car_wash else 0.0

    grand_total = fuel_total + wash_fee

    print("\n=======================================")
    print("          FUEL PUMP RECEIPT            ")
    print("=======================================")
    print(f"Gallons Dispensed: {gallons_pumped:.2f}")
    print(f"Price per Gallon:  ${price_per_gal:.2f}")
    print("---------------------------------------")
    print(f"Fuel Charge:       ${fuel_total:6.2f}")
    
    if car_wash:
        print(f"Car Wash Add-on:   ${wash_fee:6.2f}")
        print("   -> Wash Code: 49813 <-")
        
    print("---------------------------------------")
    print(f"TOTAL SALE:        ${grand_total:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
