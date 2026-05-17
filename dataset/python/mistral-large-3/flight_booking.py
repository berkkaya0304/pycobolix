def main():
    print("--- AIRLINE RESERVATION ---")
    continue_prog = 'Y'

    while continue_prog.upper() == 'Y':
        passenger_info = get_details()
        charges = calculate_fare(passenger_info)
        print_ticket(passenger_info, charges)
        continue_prog = input("Book another flight? (Y/N): ").strip()
    print("System Terminated.")

def get_details():
    passenger_name = input("Passenger Name: ").strip()
    print("Destinations: 1=New York($300), 2=London($600), 3=Tokyo($900)")
    destination = int(input("Select Destination (1/2/3): ").strip())
    print("Class (E=Economy, B=Business +50%, F=First +100%): ")
    ticket_class = input().strip().upper()
    luggage_count = int(input("Number of checked bags ($50 each): ").strip())

    return {
        'passenger_name': passenger_name,
        'destination': destination,
        'ticket_class': ticket_class,
        'luggage_count': luggage_count
    }

def calculate_fare(passenger_info):
    base_fare = 0.0
    if passenger_info['destination'] == 1:
        base_fare = 300.00
    elif passenger_info['destination'] == 2:
        base_fare = 600.00
    elif passenger_info['destination'] == 3:
        base_fare = 900.00
    else:
        base_fare = 300.00
        print("Invalid destination, defaulted to NY.")

    class_surcharge = 0.0
    if passenger_info['ticket_class'] == 'E':
        class_surcharge = 0.0
    elif passenger_info['ticket_class'] == 'B':
        class_surcharge = base_fare * 0.50
    elif passenger_info['ticket_class'] == 'F':
        class_surcharge = base_fare * 1.00
    else:
        class_surcharge = 0.0

    luggage_fee = passenger_info['luggage_count'] * 50.00
    total_cost = base_fare + class_surcharge + luggage_fee
    tax_amount = total_cost * 0.10
    grand_total = total_cost + tax_amount

    return {
        'base_fare': base_fare,
        'class_surcharge': class_surcharge,
        'luggage_fee': luggage_fee,
        'total_cost': total_cost,
        'tax_amount': tax_amount,
        'grand_total': grand_total
    }

def format_currency(value):
    return "${:,.2f}".format(value)

def print_ticket(passenger_info, charges):
    print("")
    print("=============================================")
    print("               BOARDING PASS                 ")
    print("=============================================")
    print(f"Name: {passenger_info['passenger_name']}")
    print(f"Base Fare:       {format_currency(charges['base_fare'])}")

    if charges['class_surcharge'] > 0:
        print(f"Class Upgrade:   {format_currency(charges['class_surcharge'])}")

    if charges['luggage_fee'] > 0:
        print(f"Baggage Fees:    {format_currency(charges['luggage_fee'])}")

    print("---------------------------------------------")
    print(f"Taxes (10%):     {format_currency(charges['tax_amount'])}")
    print(f"TOTAL FARE:      {format_currency(charges['grand_total'])}")
    print("=============================================")

if __name__ == "__main__":
    main()
