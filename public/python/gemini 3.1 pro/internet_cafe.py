def main():
    print("--- CYBER NET CAFE BILLING ---")
    try:
        pc_number = int(input("PC Station Number: "))
    except ValueError:
        pc_number = 0
    try:
        hours_used = float(input("Hours Logged (e.g., 2.5): "))
    except ValueError:
        hours_used = 0.0
    try:
        pages_printed = int(input("Pages Printed (Black & White): "))
    except ValueError:
        pages_printed = 0
    try:
        snacks_bought = int(input("Number of Snacks/Drinks: "))
    except ValueError:
        snacks_bought = 0

    hourly_rate = 4.50
    print_rate = 0.15
    snack_price = 2.00

    pc_cost = hours_used * hourly_rate
    print_cost = pages_printed * print_rate
    snack_cost = snacks_bought * snack_price

    total_bill = pc_cost + print_cost + snack_cost

    print("\n========================================")
    print("           CAFE INVOICE                 ")
    print("========================================")
    print(f"Station: PC-{pc_number:02d}")
    print("----------------------------------------")
    print(f"Internet Time ({hours_used:.1f} hrs): ${pc_cost:6.2f}")
    
    if pages_printed > 0:
        print(f"Printing ({pages_printed} pgs):   ${print_cost:6.2f}")
        
    if snacks_bought > 0:
        print(f"Snacks & Drinks:      ${snack_cost:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:     ${total_bill:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
