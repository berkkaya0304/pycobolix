def main():
    CONVERSION_FACTOR = 2.20462
    
    try:
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * CONVERSION_FACTOR
        print(f"Weight in pounds: {pounds:7.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
