def main():
    # Define headers
    struct_headers = "lp|    number|   decimal|  currency"

    # Define separator line
    var_line = "-" * 80

    # Define row structure with initial values
    var_lp = 0
    var_number = 0
    var_decimal = -317.21
    var_currency = 317.21

    # Display headers and separator
    print(struct_headers)
    print(var_line)

    # Update values
    var_lp = 1
    var_number = 3721

    # Format and display row
    formatted_row = (
        f"{var_lp:02d}|"
        f"{var_number:>10}|"
        f"{var_decimal:+9.2f}|"
        f"${var_currency:8.2f}"
    )
    print(formatted_row)

if __name__ == "__main__":
    main()
