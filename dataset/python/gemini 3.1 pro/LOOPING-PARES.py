def main():
    contador = 0
    try:
        numerador = int(input("DIGITE UM NUMERO: "))
    except ValueError:
        numerador = 0

    print("********************************")
    print("***** CONTANDO 'N' NUMEROS *****")
    print("********************************")

    while contador != numerador:
        contador += 1
        print(f"CONTADOR: {contador:02d}")

if __name__ == "__main__":
    main()
