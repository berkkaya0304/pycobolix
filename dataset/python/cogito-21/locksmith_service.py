def main():
    print("--- METRO LOCK & KEY ---")
    client = input("Client: ")
    
    print("Service (1=House $60, 2=Auto $80, 3=Safe $150): ", end="")
    call_type = int(input())
    
    print("Duplicate Keys Cut On-Site ($5 ea): ", end="")
    keys_cut = int(input())
    
    print("Is this an After-Hours Emergency (+ $40)? (Y/N): ", end="")
    after_hours = input().strip().upper()
    
    trip_fee = 45.00
    labor_fee = 0.0
    keys_fee = 0.0
    night_surchg = 0.0
    
    if call_type == 1:
        labor_fee = 60.00
    elif call_type == 2:
        labor_fee = 80.00
    elif call_type == 3:
        labor_fee = 150.00
    else:
        labor_fee = 60.00
    
    keys_fee = keys_cut * 5.00
    
    if after_hours == 'Y':
        night_surchg = 40.00
    
    total_chg = trip_fee + labor_fee + keys_fee + night_surchg
    
    print("\n" + "="*40)
    print("            SERVICE INVOICE             ")
    print("="*40)
    print(f"Client: {client}")
    print("-"*40)
    print(f"Service Call Trip:  ${trip_fee:6.2f}")
    print(f"Unlock Labor Rate:  ${labor_fee:6.2f}")
    
    if keys_cut > 0:
        print(f"Keys Cut ({keys_cut}):       ${keys_fee:6.2f}")
    
    if after_hours == 'Y':
        print(f"After-Hours Fee:    ${night_surchg:6.2f}")
    
    print("-"*40)
    print(f"TOTAL BALANCE:      ${total_chg:6.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
