def main():
    ws_conversion_factor = 2.20462

    try:
        ws_kg = float(input("Enter weight in kilograms: "))
    except ValueError:
        ws_kg = 0.0

    ws_pounds = ws_kg * ws_conversion_factor
    print(f"Weight in pounds: {ws_pounds:9.2f}")

if __name__ == "__main__":
    main()
