def main():
    print("--- RAILWAY TICKET BOOKING ---")
    passenger_name = input("Passenger Name: ")
    try:
        age = int(input("Passenger Age: "))
    except ValueError:
        age = 0
    try:
        distance_km = int(input("Travel Distance (KM): "))
    except ValueError:
        distance_km = 0
    class_type = input("Class (1=1AC, 2=2AC, S=Sleeper, G=General): ").strip().upper()

    reservation_fee = 20.00

    if class_type == '1':
        base_fare = distance_km * 3.50
    elif class_type == '2':
        base_fare = distance_km * 2.00
    elif class_type == 'S':
        base_fare = distance_km * 1.00
    elif class_type == 'G':
        base_fare = distance_km * 0.50
        reservation_fee = 0.0
    else:
        base_fare = distance_km * 0.50
        reservation_fee = 0.0

    concession = 0.0
    if age >= 60:
        concession = base_fare * 0.40
    elif age <= 12:
        concession = base_fare * 0.50

    total_fare = base_fare + reservation_fee - concession

    print("\n===========================================")
    print("          E-TICKET CONFIRMATION            ")
    print("===========================================")
    print(f"Name: {passenger_name}   Age: {age:03d} yrs")
    print(f"Distance: {distance_km:04d} km")
    print("-------------------------------------------")
    print(f"Base Distance Fare: ${base_fare:6.2f}")
    
    if reservation_fee > 0:
        print(f"Reservation Fee:    ${reservation_fee:6.2f}")
        
    if concession > 0:
        print(f"Age Concession:    -${concession:6.2f}")
        
    print("-------------------------------------------")
    print(f"TOTAL FARE PAYABLE: ${total_fare:6.2f}")
    print("===========================================")

if __name__ == "__main__":
    main()
