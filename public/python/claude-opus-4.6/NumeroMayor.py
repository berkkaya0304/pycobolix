"""
Find the Largest Number
Converted from COBOL (NumeroMayor.cbl) to Python

Reads 10 numbers from the user and determines the largest one.
"""


def main():
    print("Introduce diez números y te digo cual es el mayor")

    print("Introduce el primer número")
    num_mayor = int(input())
    contador = 1

    while contador < 10:
        print("Introduce otro número")
        num_teclado = int(input())
        if num_teclado > num_mayor:
            num_mayor = num_teclado
        contador += 1

    print(f"El mayor de los diez es: {num_mayor}")


if __name__ == "__main__":
    main()
