def locksmith_service():
    print("--- METRO LOCK & KEY ---")

    client = input("Client: ").strip()
    call_type = int(input("Service (1=House $60, 2=Auto $80, 3=Safe $150): "))
    keys_cut = int(input("Duplicate Keys Cut On-Site ($5 ea): "))
    after_hours = input("Is this an After-Hours Emergency (+ $40)? (Y/N): ").strip().upper()

    trip_fee = 45.00
    labor_fee = 0.00
    keys_fee = 0.00
    night_surcharge = 0.00

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
        night_surcharge = 40.00

    total_charge = trip_fee + labor_fee + keys_fee + night_surcharge

    print("\n========================================")
    print("            SERVICE INVOICE             ")
    print("========================================")
    print(f"Client: {client}")
    print("----------------------------------------")
    print(f"Service Call Trip:  ${trip_fee:,.2f}")
    print(f"Unlock Labor Rate:  ${labor_fee:,.2f}")

    if keys_cut > 0:
        print(f"Keys Cut ({keys_cut}):       ${keys_fee:,.2f}")

    if after_hours == 'Y':
        print(f"After-Hours Fee:    ${night_surcharge:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:      ${total_charge:,.2f}")
    print("========================================")

if __name__ == "__main__":
    locksmith_service()
