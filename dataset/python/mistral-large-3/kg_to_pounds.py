def kg_to_pounds():
    conversion_factor = 2.20462
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * conversion_factor
    print(f"Weight in pounds: {pounds:.2f}")

if __name__ == "__main__":
    kg_to_pounds()
