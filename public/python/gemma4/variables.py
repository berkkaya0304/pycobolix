def main():
    # Header definition
    headers = "lp|    number|   decimal|  currency"
    separator = "-" * 80

    # Initial values for the row
    var_lp = 0
    var_number = 0
    var_decimal = -317.21
    var_currency = 317.21

    print(headers)
    print(separator)

    # Update variables as per PROCEDURE DIVISION
    var_lp = 1
    var_number = 3721

    # Formatting the row to match COBOL PIC clauses
    # var_lp: PIC 9(2) -> 2 digits, zero padded
    # var_number: PIC z(10) -> 10 chars, right aligned, zero suppressed
    # var_decimal: PIC +z(7).zz -> sign, 7 digits, 2 decimals, zero suppressed
    # var_currency: PIC $z(7).zz -> $, 7 digits, 2 decimals, zero suppressed
    
    row = (
        f"{var_lp:02d}|"
        f"{var_number:>10}|"
        f"{var_decimal:>10.2f}|"
        f"${var_currency:>9.2f}"
    )

    print(row)

if __name__ == "__main__":
    main()
