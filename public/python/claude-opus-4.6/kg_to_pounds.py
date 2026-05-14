"""
Kilograms to Pounds Converter
Converted from COBOL (kg_to_pounds.cob) to Python
"""

CONVERSION_FACTOR = 2.20462


def main():
    ws_kg = float(input("Enter weight in kilograms: "))
    ws_pounds = ws_kg * CONVERSION_FACTOR
    print(f"Weight in pounds: {ws_pounds:.2f}")


if __name__ == "__main__":
    main()
