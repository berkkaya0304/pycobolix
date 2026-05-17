def main():
    print("--- INTERSTATE EXPRESS TICKETING ---")
    
    passenger = input("Passenger Name: ")
    
    try:
        route_id = int(input("Route (1=NY-DC $35, 2=NY-BOS $40, 3=NY-CHI $55): "))
    except ValueError:
        route_id = 0

    try:
        age = int(input("Passenger Age: "))
    except ValueError:
        age = 0

    try:
        extra_bags = int(input("Extra Luggage (First bag free, $15 after): "))
    except ValueError:
        extra_bags = 0

    # Determine Base Fare
    if route_id == 1:
        base_fare = 35.00
    elif route_id == 2:
        base_fare = 40.00
    elif route_id == 3:
        base_fare = 55.00
    else:
        base_fare = 35.00
        print("Unknown Route - Default NY-DC.")

    # Calculate Baggage Fee
    baggage_fee = 0.0
    if extra_bags > 0:
        baggage_fee = extra_bags * 15.00

    # Calculate Discount
    discount = 0.0
    if age >= 65:
        discount = base_fare * 0.15
    elif age <= 12:
        discount = base_fare * 0.25

    final_fare = base_fare + baggage_fee - discount

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(value):
        return f"${value:,.2f}"

    print("\n========================================")
    print("          BOARDING PASS                 ")
    print("========================================")
    print(f"Passenger: {passenger} (Age: {age})")
    print("----------------------------------------")
    print(f"Route Base Fare:    {format_currency(base_fare)}")
    
    if baggage_fee > 0:
        print(f"Extra Baggage Fee:  {format_currency(baggage_fee)}")
    
    if discount > 0:
        print(f"Age Discount:      -{format_currency(discount)}")
        
    print("----------------------------------------")
    print(f"TOTAL TICKET PRICE: {format_currency(final_fare)}")
    print("========================================")

if __name__ == "__main__":
    main()
