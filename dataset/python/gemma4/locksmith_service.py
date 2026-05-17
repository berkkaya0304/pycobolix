def main():
    # Constants
    TRIP_FEE = 45.00
    KEY_UNIT_PRICE = 5.00
    NIGHT_SURCHARGE_AMOUNT = 40.00
    
    # Input Section
    print("--- METRO LOCK & KEY ---")
    client = input("Client: ")
    
    call_type_input = input("Service (1=House $60, 2=Auto $80, 3=Safe $150): ")
    try:
        call_type = int(call_type_input)
    except ValueError:
        call_type = 0

    keys_cut_input = input("Duplicate Keys Cut On-Site ($5 ea): ")
    try:
        keys_cut = int(keys_cut_input)
    except ValueError:
        keys_cut = 0

    after_hours = input("Is this an After-Hours Emergency (+ $40)? (Y/N): ").upper()

    # Business Logic: Determine Labor Fee
    if call_type == 1:
        labor_fee = 60.00
    elif call_type == 2:
        labor_fee = 80.00
    elif call_type == 3:
        labor_fee = 150.00
    else:
        labor_fee = 60.00

    # Calculate Fees
    keys_fee = keys_cut * KEY_UNIT_PRICE
    night_surchg = NIGHT_SURCHARGE_AMOUNT if after_hours == 'Y' else 0.00
    total_chg = TRIP_FEE + labor_fee + keys_fee + night_surchg

    # Output Section (Invoice)
    print("\n========================================")
    print("            SERVICE INVOICE             ")
    print("========================================")
    print(f"Client: {client}")
    print("----------------------------------------")
    print(f"Service Call Trip:  ${TRIP_FEE:,.2f}")
    print(f"Unlock Labor Rate:  ${labor_fee:,.2f}")
    
    if keys_cut > 0:
        print(f"Keys Cut ({keys_cut}):       ${keys_fee:,.2f}")
    
    if after_hours == 'Y':
        print(f"After-Hours Fee:    ${night_surchg:,.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_chg:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
