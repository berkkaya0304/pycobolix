def main():
    num_mayor = 0
    contador = 0

    print("Introduce diez números y te digo cual es el mayor")
    print("Introduce el primer número")
    num_mayor = int(input())
    contador += 1

    while contador < 10:
        print("Introduce otro número")
        num_teclado = int(input())
        if num_teclado > num_mayor:
            num_mayor = num_teclado
        contador += 1

    print(f"El mayor de los diez es: {num_mayor}")

if __name__ == "__main__":
    main()
