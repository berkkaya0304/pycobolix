def first_calculator():
    while True:
        try:
            x = int(input('Insert first number X in format S999: '))
            y = int(input('Insert second number Y in format S999: '))

            total = x + y
            difference = x - y
            product = x * y
            quotient = x / y if y != 0 else float('inf')

            print(f"X= {x}")
            print(f"Y = {y}")
            print(f"X + Y = {total}")
            print(f"X - Y = {difference}")
            print(f"X * Y = {product}")
            print(f"X / Y = {quotient:.2f}")

            answer = input("Do you want to repeat calculation? (Y/N): ").strip().upper()
            if answer != 'Y':
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    first_calculator()
