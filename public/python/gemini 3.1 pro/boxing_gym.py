def main():
    print("--- IRON FIST BOXING GYM ---")
    fighter_name = input("Fighter: ")
    session_type = input("Entry (1=Open Gym $15, 2=Class $25, 3=Coach $80): ").strip()
    rent_gloves = input("Rent Sparring Gloves ($5)? (Y/N): ").strip().upper() == 'Y'
    rent_wraps = input("Buy Hand Wraps ($8)? (Y/N): ").strip().upper() == 'Y'

    entry_fee = 15.00
    if session_type == '2':
        entry_fee = 25.00
    elif session_type == '3':
        entry_fee = 80.00

    glove_fee = 5.00 if rent_gloves else 0.0
    wrap_fee = 8.00 if rent_wraps else 0.0

    total_due = entry_fee + glove_fee + wrap_fee

    print("\n========================================")
    print("             GYM CHECK-IN               ")
    print("========================================")
    print(f"Name: {fighter_name}")
    print("----------------------------------------")
    print(f"Session Access:      ${entry_fee:6.2f}")
    
    if rent_gloves:
        print(f"Glove Rental:        ${glove_fee:6.2f}")
        
    if rent_wraps:
        print(f"Hand Wraps Purchase: ${wrap_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${total_due:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
