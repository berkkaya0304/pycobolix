def main():
    print("--- MUNICIPAL WATER DEPT ---")
    cust_name = input("Customer Name: ")
    try:
        gals_used = int(input("Water usage for cycle (Gallons): "))
    except ValueError:
        gals_used = 0
    has_sewer = input("Connected to City Sewer? (Y/N): ").strip().upper() == 'Y'

    base_conn_fee = 24.50
    usage_fee = 0.0
    sewer_fee = 0.0

    if gals_used <= 5000:
        usage_fee = (gals_used / 1000.0) * 3.50
    elif gals_used <= 10000:
        usage_fee = (5000.0 / 1000.0 * 3.50) + ((gals_used - 5000.0) / 1000.0 * 4.75)
    else:
        usage_fee = (5000.0 / 1000.0 * 3.50) + (5000.0 / 1000.0 * 4.75) + ((gals_used - 10000.0) / 1000.0 * 6.50)

    if has_sewer:
        sewer_fee = usage_fee * 0.80

    grand_total = base_conn_fee + usage_fee + sewer_fee

    print("\n=======================================")
    print("          WATER UTILITY BILL           ")
    print("=======================================")
    print(f"Account Name: {cust_name}")
    print(f"Consumption:  {gals_used:06d} Gallons")
    print("---------------------------------------")
    print(f"Base Connection Fee: ${base_conn_fee:6.2f}")
    print(f"Tiered Water Usage:  ${usage_fee:6.2f}")
    
    if has_sewer:
        print(f"Sewer & Wastewater:  ${sewer_fee:6.2f}")
        
    print("---------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${grand_total:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
