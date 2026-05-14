def main():
    n = int(input("Enter number of Fibonacci terms: "))

    f1, f2 = 0, 1
    print("Fibonacci sequence using loop:")

    for _ in range(n):
        print(f1)
        f1, f2 = f2, f1 + f2

if __name__ == "__main__":
    main()
