def main():
    first_name = input("Enter your first name: ").strip()
    age = input("Enter your age: ").strip()

    try:
        age_int = int(age)
        response = f"Hello {first_name}, you are {age_int} years old."
        print(response)
    except ValueError:
        print("Invalid age entered. Please enter a numeric value.")

if __name__ == "__main__":
    main()
