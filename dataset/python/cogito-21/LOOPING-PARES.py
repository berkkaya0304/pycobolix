def main():
    contador = 0
    numerador = int(input("DIGITE UM NUMERO: "))
    
    print("********************************")
    print("***** CONTANDO 'N' NUMEROS *****")
    print("********************************")
    
    while contador < numerador:
        contador += 1
        print(f"CONTADOR: {contador}")

if __name__ == "__main__":
    main()
