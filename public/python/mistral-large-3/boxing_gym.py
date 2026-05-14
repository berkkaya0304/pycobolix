def boxing_gym():
    print("--- IRON FIST BOXING GYM ---")
    fighter_name = input("Fighter: ").strip()

    print("Entry (1=Open Gym $15, 2=Class $25, 3=Coach $80): ")
    session_type = int(input().strip())

    print("Rent Sparring Gloves ($5)? (Y/N): ")
    rent_gloves = input().strip().upper() == 'Y'

    print("Buy Hand Wraps ($8)? (Y/N): ")
    rent_wraps = input().strip().upper() == 'Y'

    entry_fee = 0.0
    if session_type == 1:
        entry_fee = 15.00
    elif session_type == 2:
        entry_fee = 25.00
    elif session_type == 3:
        entry_fee = 80.00
    else:
        entry_fee = 15.00

    glove_fee = 5.00 if rent_gloves else 0.0
    wrap_fee = 8.00 if rent_wraps else 0.0
    total_due = entry_fee + glove_fee + wrap_fee

    print("")
    print("========================================")
    print("             GYM CHECK-IN               ")
    print("========================================")
    print(f"Name: {fighter_name}")
    print("----------------------------------------")
    print(f"Session Access:      ${entry_fee:,.2f}")

    if rent_gloves:
        print(f"Glove Rental:        ${glove_fee:,.2f}")

    if rent_wraps:
        print(f"Hand Wraps Purchase: ${wrap_fee:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${total_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    boxing_gym()
