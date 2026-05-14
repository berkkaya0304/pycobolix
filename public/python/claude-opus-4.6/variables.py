"""
Variables and Evaluate - Demo Program
Converted from COBOL (variables.cbl) to Python
"""


def main():
    # Struct headers
    headers = f"{'lp'}|{'number':>10}|{'decimal':>10}|{'currency':>10}"
    line = "-" * 80

    print(headers)
    print(line)

    lp = 1
    number = 3721
    decimal_val = -317.21
    currency_val = 317.21

    row = f"{lp:02d}|{number:>10d}|{decimal_val:>+10.2f}|${currency_val:>9.2f}"
    print(row)


if __name__ == "__main__":
    main()
