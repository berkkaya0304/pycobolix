"""
Counting Even Numbers (Looping Pares)
Converted from COBOL (LOOPING-PARES.cbl) to Python

Accepts a number from the user and counts up to it,
displaying each count value.
"""


def main():
    print("DIGITE UM NUMERO: ")
    numerador = int(input())

    print("********************************")
    print("***** CONTANDO 'N' NUMEROS *****")
    print("********************************")

    for contador in range(1, numerador + 1):
        print(f"CONTADOR: {contador:02d}")


if __name__ == "__main__":
    main()
