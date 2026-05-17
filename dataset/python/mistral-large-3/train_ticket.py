def main():
    print("--- RAILWAY TICKET BOOKING ---")
    passenger_name = input("Passenger Name: ").strip()
    age = int(input("Passenger Age: ").strip())
    distance_km = int(input("Travel Distance (KM): ").strip())
    class_type = input("Class (1=1AC, 2=2AC, S=Sleeper, G=General): ").strip().upper()

    base_fare, reservation_fee = calculate_fare(distance_km, class_type)
    concession = calculate_concession(base_fare, age)
    total_fare = base_fare + reservation_fee - concession

    issue_ticket(passenger_name, age, distance_km, class_type,
                 base_fare, reservation_fee, concession, total_fare)

def calculate_fare(distance_km, class_type):
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
    return base_fare, reservation_fee

def calculate_concession(base_fare, age):
    if age >= 60:
        return base_fare * 0.40
    elif age <= 12:
        return base_fare * 0.50
    return 0.00

def issue_ticket(name, age, distance, class_type, base_fare, reservation_fee, concession, total_fare):
    print("\n===========================================")
    print("          E-TICKET CONFIRMATION            ")
    print("===========================================")
    print(f"Name: {name:<25} Age: {age} yrs")
    print(f"Distance: {distance} km")
    print("-------------------------------------------")
    print(f"Base Distance Fare:    ${base_fare:,.2f}")

    if reservation_fee > 0:
        print(f"Reservation Fee:       ${reservation_fee:,.2f}")

    if concession > 0:
        print(f"Age Concession:       -${concession:,.2f}")

    print("-------------------------------------------")
    print(f"TOTAL FARE PAYABLE:    ${total_fare:,.2f}")
    print("===========================================")

if __name__ == "__main__":
    main()
