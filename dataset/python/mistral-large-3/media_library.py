def media_library():
    print("--- CITY LIBRARY RETURNS ---")
    member_id = input("Member ID: ").strip()
    item_type = int(input("Item Type (1=Book, 2=DVD, 3=Laptop): ").strip())
    days_overdue = int(input("Days Overdue: ").strip())

    rate_per_day = 0.0
    max_fine = 0.0
    process_fee = 0.0

    if item_type == 1:  # Book
        rate_per_day = 0.25
        max_fine = 10.00
    elif item_type == 2:  # DVD
        rate_per_day = 1.50
        max_fine = 30.00
    elif item_type == 3:  # Laptop
        rate_per_day = 20.00
        max_fine = 500.00
        process_fee = 15.00
    else:  # Default to book rates
        rate_per_day = 0.25
        max_fine = 10.00

    calc_fine = days_overdue * rate_per_day

    if calc_fine > max_fine:
        calc_fine = max_fine
        print(">>> Fine capped at Maximum Amount.")

    total_bill = calc_fine + process_fee

    print("\n========================================")
    print("          LIBRARY FINE NOTICE           ")
    print("========================================")
    print(f"Member: {member_id}")
    print(f"Days Late: {days_overdue}")
    print("----------------------------------------")

    if days_overdue == 0:
        print("Item returned on time. No fines.")
    else:
        print(f"Late Fine:         ${calc_fine:,.2f}")
        if process_fee > 0:
            print(f"Processing Fee:    ${process_fee:,.2f}")
        print("----------------------------------------")
        print(f"TOTAL DUE:         ${total_bill:,.2f}")

    print("========================================")

if __name__ == "__main__":
    media_library()
