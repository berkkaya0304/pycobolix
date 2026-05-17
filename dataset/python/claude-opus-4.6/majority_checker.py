"""
Majority Checker (Adult/Minor)
Converted from COBOL (majority_checker.cbl) to Python
"""


def main():
    first_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))

    if age >= 18:
        response = f"Hello {first_name}, you are an adult."
    else:
        response = f"Hello {first_name}, you are a minor."

    print(response)


if __name__ == "__main__":
    main()
