def main():
    print("Introduce diez números y te digo cual es el mayor")
    
    try:
        num_mayor = int(input("Introduce el primer número: "))
        contador = 1
        
        while contador < 10:
            num_teclado = int(input("Introduce otro número: "))
            if num_teclado > num_mayor:
                num_mayor = num_teclado
            contador += 1
            
        print(f"El mayor de los diez es: {num_mayor}")
    except ValueError:
        print("Error: Por favor, introduce solo números enteros.")

if __name__ == "__main__":
    main()
