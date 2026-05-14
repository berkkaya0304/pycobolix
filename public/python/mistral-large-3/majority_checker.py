def majority_checker():
    first_name = input("Enter your first name: ").strip()
    age = int(input("Enter your age: ").strip())

    if age >= 18:
        response = f"Hello {first_name}, you are an adult."
    else:
        response = f"Hello {first_name}, you are a minor."

    print(response)

if __name__ == "__main__":
    majority_checker()
