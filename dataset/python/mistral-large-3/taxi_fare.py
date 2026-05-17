def taxi_fare():
    # Constants
    BASE_DROP = 3.50
    MILE_RATE = 2.75
    WAIT_RATE = 0.50
    NIGHT_FEE = 2.00

    # Input collection
    print("--- CITY CAB METER ---")
    passenger_name = input("Passenger Name: ").strip()
    distance_miles = float(input("Distance Traveled (Miles): "))
    wait_minutes = int(input("Traffic/Wait Time (Minutes): "))
    night_surcharge = input("Is it between 8PM and 6AM? (Y/N): ").strip().upper() == 'Y'

    # Calculations
    distance_fee = distance_miles * MILE_RATE
    time_fee = wait_minutes * WAIT_RATE
    total_fare = BASE_DROP + distance_fee + time_fee

    if night_surcharge:
        total_fare += NIGHT_FEE

    # Receipt display
    print("\n========================================")
    print("             TAXI RECEIPT               ")
    print("========================================")
    print(f"Passenger: {passenger_name}")
    print(f"Distance:  {distance_miles:.1f} mi")
    print("----------------------------------------")
    print(f"Initial Drop:       ${BASE_DROP:.2f}")
    print(f"Mileage Fare:       ${distance_fee:.2f}")

    if time_fee > 0:
        print(f"Wait/Idle Time:     ${time_fee:.2f}")

    if night_surcharge:
        print(f"Night Surcharge:    ${NIGHT_FEE:.2f}")

    print("----------------------------------------")
    print(f"TOTAL FARE DUE:     ${total_fare:.2f}")
    print("========================================")

if __name__ == "__main__":
    taxi_fare()
