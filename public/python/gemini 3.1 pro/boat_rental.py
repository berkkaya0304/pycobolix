def main():
    print("--- LAKESIDE MARINA RENTALS ---")
    customer = input("Customer Name: ")
    boat_type = input("Boat (1=Kayak $15/h, 2=Pontoon $75, 3=Speed $120): ").strip()
    try:
        hours_rent = float(input("Rental Duration (Hours): "))
    except ValueError:
        hours_rent = 0.0
    try:
        life_jackets = int(input("Extra Life Jackets Needed ($5 flat ea): "))
    except ValueError:
        life_jackets = 0

    insur_fee = 25.00
    if boat_type == '1':
        hourly_rate = 15.00
        insur_fee = 0.0
    elif boat_type == '2':
        hourly_rate = 75.00
    elif boat_type == '3':
        hourly_rate = 120.00
    else:
        hourly_rate = 15.00
        insur_fee = 0.0

    boat_total = hours_rent * hourly_rate
    jacket_fee = life_jackets * 5.00
    gross_amt = boat_total + jacket_fee + insur_fee

    print("\n========================================")
    print("          MARINA RENTAL AGREEMENT       ")
    print("========================================")
    print(f"Renter: {customer}")
    print(f"Duration: {hours_rent} hours")
    print("----------------------------------------")
    print(f"Vessel Rental Fee:  ${boat_total:6.2f}")
    
    if jacket_fee > 0:
        print(f"Life Jacket Rental: ${jacket_fee:6.2f}")
        
    if insur_fee > 0:
        print(f"Damage Insurance:   ${insur_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE DUE:  ${gross_amt:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
