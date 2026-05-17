def main():
    while True:
        try:
            x = int(input('Insert first number X in format S999: ').strip())
            y = int(input('Insert second number Y in format S999: ').strip())
            
            total = x + y
            difference = x - y
            product = x * y
            
            if y == 0:
                quotient = "undefined (division by zero)"
            else:
                quotient = x / y
            
            print(f"X = {x}")
            print(f"Y = {y}")
            print(f"X + Y = {total}")
            print(f"X - Y = {difference}")
            print(f"X * Y = {product}")
            print(f"X / Y = {quotient}")
            
            answer = input("Do you want to repeat calculation? (Y/N): ").strip().upper()
            if answer != 'Y':
                break
                
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
