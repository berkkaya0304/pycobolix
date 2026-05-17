def main():
    # Rates
    HOURLY_RATE = 4.50
    PRINT_RATE = 0.15
    SNACK_PRICE = 2.00

    print("--- CYBER NET CAFE BILLING ---")
    
    try:
        pc_number = input("PC Station Number: ")
        hours_used = float(input("Hours Logged (e.g., 2.5): "))
        pages_printed = int(input("Pages Printed (Black & White): "))
        snacks_bought = int(input("Number of Snacks/Drinks: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculations
    pc_cost = hours_used * HOURLY_RATE
    print_cost = pages_printed * PRINT_RATE
    snack_cost = snacks_bought * SNACK_PRICE
    total_bill = pc_cost + print_cost + snack_cost

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("           CAFE INVOICE                 ")
    print("========================================")
    print(f"Station: PC-{pc_number}")
    print("----------------------------------------")
    
    print(f"Internet Time ({hours_used} hrs): {format_currency(pc_cost)}")
    
    if pages_printed > 0:
        print(f"Printing ({pages_printed} pgs):   {format_currency(print_cost)}")
        
    if snacks_bought > 0:
        print(f"Snacks & Drinks:      {format_currency(snack_cost)}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:     {format_currency(total_bill)}")
    print("========================================")

if __name__ == "__main__":
    main()
