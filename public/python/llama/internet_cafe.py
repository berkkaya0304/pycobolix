# INTERNET-CAFE - Cyber Net Cafe Billing
# Converted from COBOL to Python

def main():
    HOURLY_RATE = 4.50
    PRINT_RATE = 0.15
    SNACK_PRICE = 2.00

    print("--- CYBER NET CAFE BILLING ---")
    pc_number = input("PC Station Number: ")
    hours_used = float(input("Hours Logged (e.g., 2.5): "))
    pages_printed = int(input("Pages Printed (Black & White): "))
    snacks_bought = int(input("Number of Snacks/Drinks: "))

    pc_cost = hours_used * HOURLY_RATE
    print_cost = pages_printed * PRINT_RATE
    snack_cost = snacks_bought * SNACK_PRICE
    total_bill = pc_cost + print_cost + snack_cost

    print("")
    print("========================================")
    print("           CAFE INVOICE                 ")
    print("========================================")
    print(f"Station: PC-{pc_number}")
    print("----------------------------------------")
    print(f"Internet Time ({hours_used} hrs): ${pc_cost:,.2f}")
    if pages_printed > 0:
        print(f"Printing ({pages_printed} pgs):   ${print_cost:,.2f}")
    if snacks_bought > 0:
        print(f"Snacks & Drinks:      ${snack_cost:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:     ${total_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
