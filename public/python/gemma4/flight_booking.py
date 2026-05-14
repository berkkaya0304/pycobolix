import sys

def get_details():
    name = input("Passenger Name: ")
    print("Destinations: 1=New York($300), 2=London($600), 3=Tokyo($900)")
    dest_input = input("Select Destination (1/2/3): ")
    class_input = input("Class (E=Economy, B=Business +50%, F=First +100%): ").upper()
    try:
        luggage_count = int(input("Number of checked bags ($50 each): "))
    except ValueError:
        luggage_count = 0
    
    return {
        "name": name,
        "destination": dest_input,
        "ticket_class": class_input,
        "luggage_count": luggage_count
    }

def calculate_fare(details):
    # Base Fare
    dest_map = {"1": 300.00, "2": 600.00, "3": 900.00}
    base_fare = dest_map.get(details["destination"])
    if base_fare is None:
        print("Invalid destination, defaulted to NY.")
        base_fare = 300.00

    # Class Surcharge
    class_surcharge = 0.0
    if details["ticket_class"] == 'B':
        class_surcharge = base_fare * 0.50
    elif details["ticket_class"] == 'F':
        class_surcharge = base_fare * 1.00
    elif details["ticket_class"] != 'E':
        # Default to 0 for others as per COBOL logic
        class_surcharge = 0.0

    luggage_fee = details["luggage_count"] * 50.00
    total_cost = base_fare + class_surcharge + luggage_fee
    tax_amount = total_cost * 0.10
    grand_total = total_cost + tax_amount

    return {
        "base_fare": base_fare,
        "class_surcharge": class_surcharge,
        "luggage_fee": luggage_fee,
        "tax_amount": tax_amount,
        "grand_total": grand_total
    }

def print_ticket(details, fares):
    print("\n=============================================")
    print("               BOARDING PASS                 ")
    print("=============================================")
    print(f"Name: {details['name']}")
    print(f"Base Fare:       ${fares['base_fare']:,.2f}")
    
    if fares['class_surcharge'] > 0:
        print(f"Class Upgrade:   ${fares['class_surcharge']:,.2f}")
    
    if fares['luggage_fee'] > 0:
        print(f"Baggage Fees:    ${fares['luggage_fee']:,.2f}")
        
    print("---------------------------------------------")
    print(f"Taxes (10%):     ${fares['tax_amount']:,.2f}")
    print(f"TOTAL FARE:      ${fares['grand_total']:,.2f}")
    print("=============================================")

def main():
    print("--- AIRLINE RESERVATION ---")
    continue_prog = 'Y'
    
    while continue_prog.upper() == 'Y':
        details = get_details()
        fares = calculate_fare(details)
        print_ticket(details, fares)
        
        continue_prog = input("Book another flight? (Y/N): ")
    
    print("System Terminated.")

if __name__ == "__main__":
    main()
