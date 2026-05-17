def main():
    try:
        numerador_input = input("DIGITE UM NUMERO: ")
        numerador = int(numerador_input)
    except ValueError:
        return

    print("********************************")
    print("***** CONTANDO 'N' NUMEROS *****")
    print("********************************")

    contador = 0
    while contador != numerador:
        contador += 1
        print(f"CONTADOR: {contador}")

if __name__ == "__main__":
    main()
