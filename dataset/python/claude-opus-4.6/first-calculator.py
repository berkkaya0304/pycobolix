"""
First Calculator
Converted from COBOL (first-calculator.cbl) to Python
"""


def main():
    while True:
        x = int(input("Insert first number X in format S999: "))
        y = int(input("Insert second number Y in format S999: "))

        total = x + y
        difference = x - y
        product = x * y
        quotient = x / y if y != 0 else 0

        print(f"X= {x}")
        print(f"Y = {y}")
        print(f"X + Y = {total}")
        print(f"X - Y = {difference}")
        print(f"X * Y = {product}")
        print(f"X / Y = {quotient:.2f}")

        answer = input("Do you want repete calculation? (Y/N): ").strip().upper()
        if answer != "Y":
            break


if __name__ == "__main__":
    main()
