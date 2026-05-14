def main():
    answer = 'Y'
    
    while answer == 'Y':
        print("Insert first number X in format S999: ")
        x = int(input())
        
        print("Insert second number Y in format S999: ")
        y = int(input())
        
        total = x + y
        difference = x - y
        product = x * y
        quotient = x / y if y != 0 else 0
        
        print(f"X= {x}")
        print(f"Y = {y}")
        print(f"X + Y = {total}")
        print(f"X - Y = {difference}")
        print(f"X * Y = {product}")
        print(f"X / Y = {quotient}")
        
        answer = input("Do you want repete calculation? (Y/N): ").upper()

if __name__ == "__main__":
    main()
