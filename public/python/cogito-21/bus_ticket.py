def main():
    print("--- INTERSTATE EXPRESS TICKETING ---")
    passenger = input("Passenger Name: ").strip()
    
    print("Route (1=NY-DC $35, 2=NY-BOS $40, 3=NY-CHI $55): ", end="")
    route_id = int(input())
    
    print("Passenger Age: ", end="")
    age = int(input())
    
    print("Extra Luggage (First bag free, $15 after): ", end="")
    extra_bags = int(input())
    
    base_fare = 0.0
    if route_id == 1:
        base_fare = 35.00
    elif route_id == 2:
        base_fare = 40.00
    elif route_id == 3:
        base_fare = 55.00
    else:
        base_fare = 35.00
        print("Unknown Route - Default NY-DC.")
    
    baggage_fee = 0.0
    if extra_bags > 0:
        baggage_fee = extra_bags * 15.00
    
    discount = 0.0
    if age >= 65:
        discount = base_fare * 0.15
    elif age <= 12:
        discount = base_fare * 0.25
    
    final_fare = base_fare + baggage_fee - discount
    
    print("\n" + "=" * 40)
    print("          BOARDING PASS                 ")
    print("=" * 40)
    print(f"Passenger: {passenger} (Age: {age})")
    print("-" * 40)
    print(f"Route Base Fare:    ${base_fare:,.2f}")
    
    if baggage_fee > 0:
        print(f"Extra Baggage Fee:  ${baggage_fee:,.2f}")
    
    if discount > 0:
        print(f"Age Discount:      -${discount:,.2f}")
    
    print("-" * 40)
    print(f"TOTAL TICKET PRICE: ${final_fare:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
