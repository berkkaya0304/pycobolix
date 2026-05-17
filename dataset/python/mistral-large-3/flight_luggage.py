def flight_luggage():
    print("--- AIRPORT LUGGAGE SCANNER ---")
    flight_num = input("Flight Number: ").strip()
    passenger_id = input("Passenger ID: ").strip()
    bag_weight_kg = float(input("Bag Weight (kg): "))
    bag_length = int(input("Bag Length (cm): "))
    bag_width = int(input("Bag Width (cm): "))
    bag_height = int(input("Bag Height (cm): "))

    max_weight = 23
    max_dim = 158

    total_dim = bag_length + bag_width + bag_height
    weight_ovr = bag_weight_kg - max_weight
    dim_ovr = total_dim - max_dim

    over_wt_fee = max(weight_ovr * 15.00, 0) if weight_ovr > 0 else 0
    over_sz_fee = 50.00 if dim_ovr > 0 else 0
    total_fee = over_wt_fee + over_sz_fee

    print("\n=======================================")
    print("           LUGGAGE TAG & FEE           ")
    print("=======================================")
    print(f"Flight: {flight_num} | Pass ID: {passenger_id}")
    print("---------------------------------------")
    print(f"Bag Weight: {bag_weight_kg:.2f} kg")
    print(f"Bag Dims:   {total_dim} cm total")

    if over_wt_fee > 0 or over_sz_fee > 0:
        print("---------------------------------------")
        print(">>> BAG EXCEEDS ALLOWANCE <<<")
        if over_wt_fee > 0:
            print(f"Overweight Fee: ${over_wt_fee:,.2f}")
        if over_sz_fee > 0:
            print(f"Oversized Fee:  ${over_sz_fee:,.2f}")
        print("---------------------------------------")
        print(f"EXCESS FEES TO PAY: ${total_fee:,.2f}")
    else:
        print("---------------------------------------")
        print("Status: OK TO LOAD (No Fees)")
    print("=======================================")

if __name__ == "__main__":
    flight_luggage()
