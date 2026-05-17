def main():
    print("--- INTERSTATE EXPRESS TICKETING ---")
    passenger = input("Passenger Name: ")
    route_id = input("Route (1=NY-DC $35, 2=NY-BOS $40, 3=NY-CHI $55): ").strip()
    try:
        age = int(input("Passenger Age: "))
    except ValueError:
        age = 0
    try:
        extra_bags = int(input("Extra Luggage (First bag free, $15 after): "))
    except ValueError:
        extra_bags = 0

    if route_id == '1':
        base_fare = 35.00
    elif route_id == '2':
        base_fare = 40.00
    elif route_id == '3':
        base_fare = 55.00
    else:
        print("Unknown Route - Default NY-DC.")
        base_fare = 35.00

    baggage_fee = extra_bags * 15.00 if extra_bags > 0 else 0.0

    discount = 0.0
    if age >= 65:
        discount = base_fare * 0.15
    elif age <= 12:
        discount = base_fare * 0.25

    final_fare = base_fare + baggage_fee - discount

    print("\n========================================")
    print("          BOARDING PASS                 ")
    print("========================================")
    print(f"Passenger: {passenger} (Age: {age})")
    print("----------------------------------------")
    print(f"Route Base Fare:    ${base_fare:6.2f}")
    
    if baggage_fee > 0:
        print(f"Extra Baggage Fee:  ${baggage_fee:6.2f}")
        
    if discount > 0:
        print(f"Age Discount:      -${discount:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL TICKET PRICE: ${final_fare:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
