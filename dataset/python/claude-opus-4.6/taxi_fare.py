"""
City Cab Meter - Taxi Fare
Converted from COBOL (taxi_fare.cbl) to Python
"""


def main():
    base_drop = 3.50
    mile_rate = 2.75
    wait_rate = 0.50
    night_fee = 2.00

    print("--- CITY CAB METER ---")
    passenger_name = input("Passenger Name: ")
    distance_miles = float(input("Distance Traveled (Miles): "))
    wait_minutes = int(input("Traffic/Wait Time (Minutes): "))
    night_surcharge = input("Is it between 8PM and 6AM? (Y/N): ").strip().upper()

    distance_fee = distance_miles * mile_rate
    time_fee = wait_minutes * wait_rate
    total_fare = base_drop + distance_fee + time_fee
    if night_surcharge == "Y":
        total_fare += night_fee

    print()
    print("========================================")
    print("             TAXI RECEIPT               ")
    print("========================================")
    print(f"Passenger: {passenger_name}")
    print(f"Distance:  {distance_miles} mi")
    print("----------------------------------------")
    print(f"Initial Drop:       ${base_drop:>9,.2f}")
    print(f"Mileage Fare:       ${distance_fee:>9,.2f}")
    if time_fee > 0:
        print(f"Wait/Idle Time:     ${time_fee:>9,.2f}")
    if night_surcharge == "Y":
        print(f"Night Surcharge:    ${night_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL FARE DUE:     ${total_fare:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
