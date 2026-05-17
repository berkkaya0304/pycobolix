def main():
    conversion_factor = 2.20462
    
    try:
        kg_input = input("Enter weight in kilograms: ")
        ws_kg = float(kg_input)
        
        ws_pounds = ws_kg * conversion_factor
        
        print(f"Weight in pounds: {ws_pounds:5.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
