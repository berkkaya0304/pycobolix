def main():
    print("--- CITY LIBRARY RETURNS ---")
    member_id = input("Member ID: ")
    
    while True:
        try:
            item_type = int(input("Item Type (1=Book, 2=DVD, 3=Laptop): "))
            if item_type in (1, 2, 3):
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            days_overdue = int(input("Days Overdue: "))
            if days_overdue >= 0:
                break
            print("Please enter a non-negative number")
        except ValueError:
            print("Please enter a valid number")
    
    rate_per_day = 0.0
    max_fine = 0.0
    process_fee = 0.0
    
    if item_type == 1:
        rate_per_day = 0.25
        max_fine = 10.00
    elif item_type == 2:
        rate_per_day = 1.50
        max_fine = 30.00
    elif item_type == 3:
        rate_per_day = 20.00
        max_fine = 500.00
        process_fee = 15.00
    else:
        rate_per_day = 0.25
        max_fine = 10.00
    
    calc_fine = days_overdue * rate_per_day
    capped = False
    
    if calc_fine > max_fine:
        calc_fine = max_fine
        capped = True
    
    total_bill = calc_fine + process_fee
    
    print("\n" + "=" * 40)
    print("          LIBRARY FINE NOTICE           ")
    print("=" * 40)
    print(f"Member: {member_id}")
    print(f"Days Late: {days_overdue}")
    print("-" * 40)
    
    if days_overdue == 0:
        print("Item returned on time. No fines.")
    else:
        if capped:
            print(">>> Fine capped at Maximum Amount.")
        print(f"Late Fine:         ${calc_fine:,.2f}")
        if process_fee > 0:
            print(f"Processing Fee:    ${process_fee:,.2f}")
        print("-" * 40)
        print(f"TOTAL DUE:         ${total_bill:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
