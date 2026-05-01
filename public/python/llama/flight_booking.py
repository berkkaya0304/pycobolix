# FLIGHT-BOOKING - Airline Reservation
# Converted from COBOL to Python

def main():
    print("--- AIRLINE RESERVATION ---")
    continue_prog = 'Y'
    while continue_prog.upper() == 'Y':
        passenger_name = input("Passenger Name: ")
        print("Destinations: 1=New York($300), 2=London($600), 3=Tokyo($900)")
        destination = int(input("Select Destination (1/2/3): "))
        ticket_class = input("Class (E=Economy, B=Business +50%, F=First +100%): ").strip().upper()
        luggage_count = int(input("Number of checked bags ($50 each): "))

        if destination == 1:
            base_fare = 300.00
        elif destination == 2:
            base_fare = 600.00
        elif destination == 3:
            base_fare = 900.00
        else:
            base_fare = 300.00
            print("Invalid destination, defaulted to NY.")

        if ticket_class == 'E':
            class_surcharge = 0.0
        elif ticket_class == 'B':
            class_surcharge = base_fare * 0.50
        elif ticket_class == 'F':
            class_surcharge = base_fare * 1.00
        else:
            class_surcharge = 0.0

        luggage_fee = luggage_count * 50.00
        total_cost = base_fare + class_surcharge + luggage_fee
        tax_amount = total_cost * 0.10
        grand_total = total_cost + tax_amount

        print("")
        print("=============================================")
        print("               BOARDING PASS                 ")
        print("=============================================")
        print(f"Name: {passenger_name}")
        print(f"Base Fare:       ${base_fare:,.2f}")
        if class_surcharge > 0:
            print(f"Class Upgrade:   ${class_surcharge:,.2f}")
        if luggage_fee > 0:
            print(f"Baggage Fees:    ${luggage_fee:,.2f}")
        print("---------------------------------------------")
        print(f"Taxes (10%):     ${tax_amount:,.2f}")
        print(f"TOTAL FARE:      ${grand_total:,.2f}")
        print("=============================================")

        continue_prog = input("Book another flight? (Y/N): ").strip()

    print("System Terminated.")

if __name__ == "__main__":
    main()
