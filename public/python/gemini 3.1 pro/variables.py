def main():
    struct_headers = "lp|    number|   decimal|  currency"
    var_line = "-" * 80

    var_lp = 1
    var_number = 3721
    var_decimal = -317.21
    var_currency = 317.21

    print(struct_headers)
    print(var_line)

    # Note: formatting closely matches the COBOL PIC clauses
    # PIC 9(2) | PIC z(10) | PIC +z(7).zz | PIC $z(7).zz
    row = f"{var_lp:02d}|{var_number:10d}|{var_decimal:+11.2f}|${var_currency:10.2f}"
    print(row)

if __name__ == "__main__":
    main()
