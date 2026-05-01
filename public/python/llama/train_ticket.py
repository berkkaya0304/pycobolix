# TRAIN-TICKET - Railway Ticket Booking
# Converted from COBOL to Python

def main():
    RESERVATION_FEE = 20.00

    print("--- RAILWAY TICKET BOOKING ---")
    passenger_name = input("Passenger Name: ")
    age = int(input("Passenger Age: "))
    distance_km = int(input("Travel Distance (KM): "))
    class_type = input("Class (1=1AC, 2=2AC, S=Sleeper, G=General): ").strip().upper()

    if class_type == '1':
        base_fare = distance_km * 3.50
        reservation_fee = RESERVATION_FEE
    elif class_type == '2':
        base_fare = distance_km * 2.00
        reservation_fee = RESERVATION_FEE
    elif class_type == 'S':
        base_fare = distance_km * 1.00
        reservation_fee = RESERVATION_FEE
    else:  # General or other
        base_fare = distance_km * 0.50
        reservation_fee = 0.0

    if age >= 60:
        concession = base_fare * 0.40
    elif age <= 12:
        concession = base_fare * 0.50
    else:
        concession = 0.0

    total_fare = base_fare + reservation_fee - concession

    print("")
    print("===========================================")
    print("          E-TICKET CONFIRMATION            ")
    print("===========================================")
    print(f"Name: {passenger_name}   Age: {age} yrs")
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
    main()
