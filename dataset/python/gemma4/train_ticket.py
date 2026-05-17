def calculate_fare():
    print("--- RAILWAY TICKET BOOKING ---")
    
    passenger_name = input("Passenger Name: ")
    try:
        age = int(input("Passenger Age: "))
        distance_km = int(input("Travel Distance (KM): "))
    except ValueError:
        print("Invalid numeric input.")
        return

    class_type = input("Class (1=1AC, 2=2AC, S=Sleeper, G=General): ").upper()

    # Fare Calculation Logic
    reservation_fee = 20.00
    
    if class_type == '1':
        base_fare = distance_km * 3.50
    elif class_type == '2':
        base_fare = distance_km * 2.00
    elif class_type == 'S':
        base_fare = distance_km * 1.00
    elif class_type == 'G':
        base_fare = distance_km * 0.50
        reservation_fee = 0.00
    else:
        base_fare = distance_km * 0.50
        reservation_fee = 0.00

    # Concession Logic
    concession = 0.00
    if age >= 60:
        concession = base_fare * 0.40
    elif age <= 12:
        concession = base_fare * 0.50

    total_fare = base_fare + reservation_fee - concession

    # Issue Ticket (Display)
    print("\n===========================================")
    print("          E-TICKET CONFIRMATION            ")
    print("===========================================")
    print(f"Name: {passenger_name:<25} Age: {age} yrs")
    print(f"Distance: {distance_km} km")
    print("-------------------------------------------")
    print(f"Base Distance Fare: ${base_fare:,.2f}")
    
    if reservation_fee > 0:
        print(f"Reservation Fee:    ${reservation_fee:,.2f}")
    
    if concession > 0:
        print(f"Age Concession:    -${concession:,.2f}")
        
    print("-------------------------------------------")
    print(f"TOTAL FARE PAYABLE: ${total_fare:,.2f}")
    print("===========================================")

if __name__ == "__main__":
    calculate_fare()
