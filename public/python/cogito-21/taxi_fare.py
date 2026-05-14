def main():
    print("--- CITY CAB METER ---")
    passenger_name = input("Passenger Name: ")
    distance_miles = float(input("Distance Traveled (Miles): "))
    wait_minutes = float(input("Traffic/Wait Time (Minutes): "))
    night_surcharge = input("Is it between 8PM and 6AM? (Y/N): ").strip().upper()
    
    base_drop = 3.50
    mile_rate = 2.75
    wait_rate = 0.50
    night_fee = 2.00
    
    distance_fee = distance_miles * mile_rate
    time_fee = wait_minutes * wait_rate
    
    total_fare = base_drop + distance_fee + time_fee
    
    is_night = night_surcharge == 'Y'
    if is_night:
        total_fare += night_fee
    
    print("\n" + "=" * 40)
    print("             TAXI RECEIPT               ")
    print("=" * 40)
    print(f"Passenger: {passenger_name}")
    print(f"Distance:  {distance_miles} mi")
    print("-" * 40)
    print(f"Initial Drop:       ${base_drop:.2f}")
    print(f"Mileage Fare:       ${distance_fee:.2f}")
    
    if time_fee > 0:
        print(f"Wait/Idle Time:     ${time_fee:.2f}")
    
    if is_night:
        print(f"Night Surcharge:    ${night_fee:.2f}")
    
    print("-" * 40)
    print(f"TOTAL FARE DUE:     ${total_fare:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
