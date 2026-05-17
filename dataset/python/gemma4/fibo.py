def main():
    try:
        n_input = input("Enter number of Fibonacci terms: ")
        n = int(n_input)
    except ValueError:
        return

    print("Fibonacci sequence using loop: ")
    
    f1 = 0
    f2 = 1
    
    for _ in range(n):
        print(f1)
        temp = f1 + f2
        f1 = f2
        f2 = temp

if __name__ == "__main__":
    main()
