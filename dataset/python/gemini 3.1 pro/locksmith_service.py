def main():
    print("--- METRO LOCK & KEY ---")
    client = input("Client: ")
    call_type = input("Service (1=House $60, 2=Auto $80, 3=Safe $150): ").strip()
    try:
        keys_cut = int(input("Duplicate Keys Cut On-Site ($5 ea): "))
    except ValueError:
        keys_cut = 0
    after_hours = input("Is this an After-Hours Emergency (+ $40)? (Y/N): ").strip().upper() == 'Y'

    trip_fee = 45.00
    
    if call_type == '1':
        labor_fee = 60.00
    elif call_type == '2':
        labor_fee = 80.00
    elif call_type == '3':
        labor_fee = 150.00
    else:
        labor_fee = 60.00

    keys_fee = keys_cut * 5.00
    night_surchg = 40.00 if after_hours else 0.0

    total_chg = trip_fee + labor_fee + keys_fee + night_surchg

    print("\n========================================")
    print("            SERVICE INVOICE             ")
    print("========================================")
    print(f"Client: {client}")
    print("----------------------------------------")
    print(f"Service Call Trip:  ${trip_fee:6.2f}")
    print(f"Unlock Labor Rate:  ${labor_fee:6.2f}")
    
    if keys_cut > 0:
        print(f"Keys Cut ({keys_cut}):       ${keys_fee:6.2f}")
        
    if after_hours:
        print(f"After-Hours Fee:    ${night_surchg:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_chg:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
