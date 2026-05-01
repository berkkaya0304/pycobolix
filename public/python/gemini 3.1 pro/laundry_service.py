def main():
    print("=== FRESH & CLEAN DRY CLEANERS ===")
    cust_name = input("Customer Name: ")
    phone_num = input("Phone Number: ")

    try:
        shirts_qty = int(input("Number of Shirts ($4.50 ea): "))
    except ValueError:
        shirts_qty = 0
    try:
        pants_qty = int(input("Number of Pants ($6.00 ea): "))
    except ValueError:
        pants_qty = 0
    try:
        suits_qty = int(input("Number of Suits ($15.00 ea): "))
    except ValueError:
        suits_qty = 0
        
    rush_service = input("Rush 24-hour service? (+$10 flat) (Y/N): ").strip().upper() == 'Y'

    shirt_cost = shirts_qty * 4.50
    pant_cost = pants_qty * 6.00
    suit_cost = suits_qty * 15.00
    
    total_bill = shirt_cost + pant_cost + suit_cost

    rush_fee = 10.00 if rush_service else 0.0
    total_bill += rush_fee

    print("\n-----------------------------------------")
    print("          LAUNDRY CLAIM TICKET           ")
    print("-----------------------------------------")
    print(f"Name: {cust_name} | Ph: {phone_num}")
    print("-----------------------------------------")
    
    if shirts_qty > 0:
        print(f"{shirts_qty} x Shirts:       ${shirt_cost:6.2f}")
    if pants_qty > 0:
        print(f"{pants_qty} x Pants:        ${pant_cost:6.2f}")
    if suits_qty > 0:
        print(f"{suits_qty} x Suits:        ${suit_cost:6.2f}")
        
    print("-----------------------------------------")
    
    if rush_fee > 0:
        print(f"Rush Service Fee: ${rush_fee:6.2f}")
        
    print(f"GRAND TOTAL:      ${total_bill:6.2f}")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()
