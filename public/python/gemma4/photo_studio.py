def main():
    print("--- LENS APERTURE STUDIO ---")
    
    client_name = input("Client: ")
    session_type = input("Session (1=Headshot $99, 2=Family $150, 3=Event): ")
    
    try:
        phy_prints = int(input("Physical Prints Wanted ($15 per sheet): "))
    except ValueError:
        phy_prints = 0
        
    digital_copy = input("USB Drive with Digital Masters ($50)? (Y/N): ").upper()

    # Determine Sitting Fee
    if session_type == '1':
        sitting_fee = 99.00
    elif session_type == '2':
        sitting_fee = 150.00
    elif session_type == '3':
        sitting_fee = 300.00
    else:
        sitting_fee = 99.00

    # Calculate Print Fee
    print_fee = phy_prints * 15.00

    # Determine Digital Fee
    digital_fee = 50.00 if digital_copy == 'Y' else 0.00

    # Calculate Grand Total
    grand_total = sitting_fee + print_fee + digital_fee

    # Display Invoice
    print("\n========================================")
    print("          STUDIO INVOICE                ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    print(f"Session/Sitting Fee: ${sitting_fee:,.2f}")
    
    if print_fee > 0:
        print(f"Physical Prints ({phy_prints}):  ${print_fee:,.2f}")
        
    if digital_fee > 0:
        print(f"Digital Masters USB: ${digital_fee:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL CHARGED:       ${grand_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
