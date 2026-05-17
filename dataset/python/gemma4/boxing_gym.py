def main():
    print("--- IRON FIST BOXING GYM ---")
    
    fighter_name = input("Fighter: ")
    session_type_input = input("Entry (1=Open Gym $15, 2=Class $25, 3=Coach $80): ")
    rent_gloves_input = input("Rent Sparring Gloves ($5)? (Y/N): ").upper()
    rent_wraps_input = input("Buy Hand Wraps ($8)? (Y/N): ").upper()

    # Determine Entry Fee
    session_map = {
        "1": 15.00,
        "2": 25.00,
        "3": 80.00
    }
    entry_fee = session_map.get(session_type_input, 15.00)

    # Determine Equipment Fees
    glove_fee = 5.00 if rent_gloves_input == 'Y' else 0.00
    wrap_fee = 8.00 if rent_wraps_input == 'Y' else 0.00

    total_due = entry_fee + glove_fee + wrap_fee

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("             GYM CHECK-IN               ")
    print("========================================")
    print(f"Name: {fighter_name}")
    print("----------------------------------------")
    print(f"Session Access:      {format_currency(entry_fee)}")
    
    if glove_fee > 0:
        print(f"Glove Rental:        {format_currency(glove_fee)}")
    
    if wrap_fee > 0:
        print(f"Hand Wraps Purchase: {format_currency(wrap_fee)}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       {format_currency(total_due)}")
    print("========================================")

if __name__ == "__main__":
    main()
