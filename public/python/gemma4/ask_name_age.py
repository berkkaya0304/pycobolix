def main():
    first_name = input("Enter your first name: ").strip()
    age = input("Enter your age: ").strip()

    response = f"Hello {first_name}, you are {age} years old."
    
    print(response)

if __name__ == "__main__":
    main()
