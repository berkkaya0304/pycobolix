"""
Municipal Water Dept - Water Bill
Converted from COBOL (water_bill.cbl) to Python
"""


def main():
    base_conn_fee = 24.50

    print("--- MUNICIPAL WATER DEPT ---")
    cust_name = input("Customer Name: ")
    gals_used = int(input("Water usage for cycle (Gallons): "))
    sewer_link = input("Connected to City Sewer? (Y/N): ").strip().upper()

    if gals_used <= 5000:
        usage_fee = (gals_used / 1000) * 3.50
    elif gals_used <= 10000:
        usage_fee = (5000 / 1000 * 3.50) + ((gals_used - 5000) / 1000 * 4.75)
    else:
        usage_fee = (5000 / 1000 * 3.50) + (5000 / 1000 * 4.75) + ((gals_used - 10000) / 1000 * 6.50)

    sewer_fee = usage_fee * 0.80 if sewer_link == "Y" else 0.0
    grand_total = base_conn_fee + usage_fee + sewer_fee

    print()
    print("=======================================")
    print("          WATER UTILITY BILL           ")
    print("=======================================")
    print(f"Account Name: {cust_name}")
    print(f"Consumption:  {gals_used} Gallons")
    print("---------------------------------------")
    print(f"Base Connection Fee: ${base_conn_fee:>9,.2f}")
    print(f"Tiered Water Usage:  ${usage_fee:>9,.2f}")
    if sewer_link == "Y":
        print(f"Sewer & Wastewater:  ${sewer_fee:>9,.2f}")
    print("---------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_total:>9,.2f}")
    print("=======================================")


if __name__ == "__main__":
    main()
