def main():
    num_mayor = 0
    contador = 0

    print("Introduce diez números y te digo cual es el mayor")
    try:
        num_mayor = int(input("Introduce el primer número\n"))
    except ValueError:
        num_mayor = 0
    
    contador += 1

    while contador < 10:
        try:
            num_teclado = int(input("Introduce otro número\n"))
        except ValueError:
            num_teclado = 0
            
        if num_teclado > num_mayor:
            num_mayor = num_teclado
            
        contador += 1

    print(f"El mayor de los diez es: {num_mayor:02d}")

if __name__ == "__main__":
    main()
