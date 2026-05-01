# LOCKSMITH-SERVICE - Metro Lock & Key
# Converted from COBOL to Python

def main():
    TRIP_FEE = 45.00

    print("--- METRO LOCK & KEY ---")
    client = input("Client: ")
    call_type = int(input("Service (1=House $60, 2=Auto $80, 3=Safe $150): "))
    keys_cut = int(input("Duplicate Keys Cut On-Site ($5 ea): "))
    after_hours = input("Is this an After-Hours Emergency (+ $40)? (Y/N): ").strip().upper()

    if call_type == 1:
        labor_fee = 60.00
    elif call_type == 2:
        labor_fee = 80.00
    elif call_type == 3:
        labor_fee = 150.00
    else:
        labor_fee = 60.00

    keys_fee = keys_cut * 5.00
    night_surchg = 40.00 if after_hours == 'Y' else 0.0
    total_chg = TRIP_FEE + labor_fee + keys_fee + night_surchg

    print("")
    print("========================================")
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
