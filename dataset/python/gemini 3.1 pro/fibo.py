def main():
    try:
        n = int(input("Enter number of Fibonacci terms: "))
    except ValueError:
        n = 0

    f1 = 0
    f2 = 1

    print("Fibonacci sequence using loop: ")
    for i in range(1, n + 1):
        print(f"{f1:09d}")
        temp = f1 + f2
        f1 = f2
        f2 = temp

if __name__ == "__main__":
    main()
