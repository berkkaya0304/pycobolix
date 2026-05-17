def main():
    first_name = input("Enter your first name: ").strip()
    try:
        age = int(input("Enter your age: ").strip())
        if age >= 18:
            response = f"Hello {first_name}, you are an adult."
        else:
            response = f"Hello {first_name}, you are a minor."
        print(response)
    except ValueError:
        print("Invalid age entered. Please enter a valid number.")

if __name__ == "__main__":
    main()
