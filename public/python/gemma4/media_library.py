import sys

def main():
    print("--- CITY LIBRARY RETURNS ---")
    
    member_id = input("Member ID: ").strip()
    
    try:
        item_type = int(input("Item Type (1=Book, 2=DVD, 3=Laptop): "))
        days_overdue = int(input("Days Overdue: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for type and days.")
        return

    # Configuration for item types
    # (rate_per_day, max_fine, process_fee)
    rates = {
        1: (0.25, 10.00, 0.00),  # Book
        2: (1.50, 30.00, 0.00),  # DVD
        3: (20.00, 500.00, 15.00) # Laptop
    }

    # Default to Book if type is not recognized (COBOL 'WHEN OTHER')
    rate_per_day, max_fine, process_fee = rates.get(item_type, rates[1])

    # Calculate Fine
    calc_fine = days_overdue * rate_per_day
    
    if calc_fine > max_fine:
        calc_fine = max_fine
        print(">>> Fine capped at Maximum Amount.")

    total_bill = calc_fine + process_fee

    # Print Notice
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
    main()
