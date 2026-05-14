import sys

def calculate_water_bill():
    # Constants
    BASE_CONN_FEE = 24.50

    print("--- MUNICIPAL WATER DEPT ---")
    cust_name = input("Customer Name: ")
    try:
        gals_used = int(input("Water usage for cycle (Gallons): "))
    except ValueError:
        gals_used = 0
    
    sewer_link = input("Connected to City Sewer? (Y/N): ").strip().upper()
    has_sewer = (sewer_link == 'Y')

    # Process Bill
    if gals_used <= 5000:
        usage_fee = (gals_used / 1000) * 3.50
    elif gals_used <= 10000:
        usage_fee = (5000 / 1000 * 3.50) + ((gals_used - 5000) / 1000 * 4.75)
    else:
        usage_fee = (5000 / 1000 * 3.50) + (5000 / 1000 * 4.75) + ((gals_used - 10000) / 1000 * 6.50)

    sewer_fee = 0.0
    if has_sewer:
        sewer_fee = usage_fee * 0.80

    grand_total = BASE_CONN_FEE + usage_fee + sewer_fee

    # Print Invoice
    print("\n=======================================")
    print("          WATER UTILITY BILL           ")
    print("=======================================")
    print(f"Account Name: {cust_name}")
    print(f"Consumption:  {gals_used} Gallons")
    print("---------------------------------------")
    print(f"Base Connection Fee: ${BASE_CONN_FEE:,.2f}")
    print(f"Tiered Water Usage:  ${usage_fee:,.2f}")
    
    if has_sewer:
        print(f"Sewer & Wastewater:  ${sewer_fee:,.2f}")
        
    print("---------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_total:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    calculate_water_bill()
