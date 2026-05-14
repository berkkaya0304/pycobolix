"""
Fibonacci Sequence Generator
Converted from COBOL (fibo.cob) to Python
"""


def main():
    n = int(input("Enter number of Fibonacci terms: "))

    print("Fibonacci sequence using loop: ")
    f1 = 0
    f2 = 1
    for _ in range(n):
        print(f1)
        f1, f2 = f2, f1 + f2


if __name__ == "__main__":
    main()
