def boat_rental():
    print("--- LAKESIDE MARINA RENTALS ---")
    customer = input("Customer Name: ")
    
    print("Boat (1=Kayak $15/h, 2=Pontoon $75, 3=Speed $120): ")
    boat_type = int(input().strip())
    
    print("Rental Duration (Hours): ")
    hours_rent = int(input().strip())
    
    print("Extra Life Jackets Needed ($5 flat ea): ")
    life_jackets = int(input().strip())
    
    hourly_rate = 0.0
    insur_fee = 25.00
    
    if boat_type == 1:  # Kayak
        hourly_rate = 15.00
        insur_fee = 0.00
    elif boat_type == 2:  # Pontoon
        hourly_rate = 75.00
    elif boat_type == 3:  # Speedboat
        hourly_rate = 120.00
    else:
        hourly_rate = 15.00
        insur_fee = 0.00
    
    boat_total = hours_rent * hourly_rate
    jacket_fee = life_jackets * 5.00
    gross_amt = boat_total + jacket_fee + insur_fee
    
    print("\n" + "="*40)
    print("          MARINA RENTAL AGREEMENT       ")
    print("="*40)
    print(f"Renter: {customer}")
    print(f"Duration: {hours_rent} hours")
    print("-"*40)
    print(f"Vessel Rental Fee:  ${boat_total:,.2f}")
    
    if jacket_fee > 0:
        print(f"Life Jacket Rental: ${jacket_fee:,.2f}")
    
    if insur_fee > 0:
        print(f"Damage Insurance:   ${insur_fee:,.2f}")
    
    print("-"*40)
    print(f"TOTAL BALANCE DUE:  ${gross_amt:,.2f}")
    print("="*40)

if __name__ == "__main__":
    boat_rental()
