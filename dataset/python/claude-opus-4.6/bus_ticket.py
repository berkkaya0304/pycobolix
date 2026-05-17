"""
Interstate Express Bus Ticketing
Converted from COBOL (bus_ticket.cbl) to Python
"""


def main():
    print("--- INTERSTATE EXPRESS TICKETING ---")
    passenger = input("Passenger Name: ")
    route_id = int(input("Route (1=NY-DC $35, 2=NY-BOS $40, 3=NY-CHI $55): "))
    age = int(input("Passenger Age: "))
    extra_bags = int(input("Extra Luggage (First bag free, $15 after): "))

    if route_id == 1:
        base_fare = 35.00
    elif route_id == 2:
        base_fare = 40.00
    elif route_id == 3:
        base_fare = 55.00
    else:
        base_fare = 35.00
        print("Unknown Route - Default NY-DC.")

    baggage_fee = extra_bags * 15.00 if extra_bags > 0 else 0.0

    if age >= 65:
        discount = base_fare * 0.15
    elif age <= 12:
        discount = base_fare * 0.25
    else:
        discount = 0.0

    final_fare = base_fare + baggage_fee - discount

    print()
    print("========================================")
    print("          BOARDING PASS                 ")
    print("========================================")
    print(f"Passenger: {passenger} (Age: {age})")
    print("----------------------------------------")
    print(f"Route Base Fare:    ${base_fare:>9,.2f}")
    if baggage_fee > 0:
        print(f"Extra Baggage Fee:  ${baggage_fee:>9,.2f}")
    if discount > 0:
        print(f"Age Discount:      -${discount:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL TICKET PRICE: ${final_fare:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
