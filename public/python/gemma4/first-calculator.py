def main():
    while True:
        try:
            x = int(input('Insert first number X in format S999: '))
            y = int(input('Insert second number Y in format S999: '))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        total = x + y
        difference = x - y
        product = x * y
        
        try:
            quotient = x / y
        except ZeroDivisionError:
            quotient = "Undefined (Division by Zero)"

        print(f"X= {x}")
        print(f"Y = {y}")
        print(f"X + Y = {total}")
        print(f"X - Y = {difference}")
        print(f"X * Y = {product}")
        print(f"X / Y = {quotient}")

        answer = input("Do you want repete calculation? (Y/N): ").strip().upper()
        if answer != 'Y':
            break

if __name__ == "__main__":
    main()
