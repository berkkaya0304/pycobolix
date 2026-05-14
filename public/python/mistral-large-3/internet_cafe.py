def internet_cafe():
    print("--- CYBER NET CAFE BILLING ---")
    pc_number = int(input("PC Station Number: "))
    hours_used = float(input("Hours Logged (e.g., 2.5): "))
    pages_printed = int(input("Pages Printed (Black & White): "))
    snacks_bought = int(input("Number of Snacks/Drinks: "))

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
    internet_cafe()
