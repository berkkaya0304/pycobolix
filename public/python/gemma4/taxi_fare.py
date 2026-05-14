from decimal import Decimal, ROUND_HALF_UP

def calculate_taxi_fare():
    # Rates and Fees
    BASE_DROP = Decimal('3.50')
    MILE_RATE = Decimal('2.75')
    WAIT_RATE = Decimal('0.50')
    NIGHT_FEE = Decimal('2.00')

    print("--- CITY CAB METER ---")
    
    passenger_name = input("Passenger Name: ")
    
    try:
        distance_miles = Decimal(input("Distance Traveled (Miles): "))
        wait_minutes = Decimal(input("Traffic/Wait Time (Minutes): "))
    except Exception:
        print("Invalid numeric input.")
        return

    night_surcharge = input("Is it between 8PM and 6AM? (Y/N): ").strip().upper()
    is_night = night_surcharge == 'Y'

    # Calculations
    distance_fee = (distance_miles * MILE_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    time_fee = (wait_minutes * WAIT_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    total_fare = BASE_DROP + distance_fee + time_fee
    
    if is_night:
        total_fare += NIGHT_FEE

    # Formatting helper for currency
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("             TAXI RECEIPT               ")
    print("========================================")
    print(f"Passenger: {passenger_name}")
    print(f"Distance:  {distance_miles} mi")
    print("----------------------------------------")
    print(f"Initial Drop:       {format_currency(BASE_DROP)}")
    print(f"Mileage Fare:       {format_currency(distance_fee)}")
    
    if time_fee > 0:
        print(f"Wait/Idle Time:     {format_currency(time_fee)}")
    
    if is_night:
        print(f"Night Surcharge:    {format_currency(NIGHT_FEE)}")
        
    print("----------------------------------------")
    print(f"TOTAL FARE DUE:     {format_currency(total_fare)}")
    print("========================================")

if __name__ == "__main__":
    calculate_taxi_fare()
