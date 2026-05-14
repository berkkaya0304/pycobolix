def main():
    first_name = input("Enter your first name: ").strip()
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age input.")
        return

    if age >= 18:
        response = f"Hello {first_name}, you are an adult."
    else:
        response = f"Hello {first_name}, you are a minor."

    print(response)

if __name__ == "__main__":
    main()
