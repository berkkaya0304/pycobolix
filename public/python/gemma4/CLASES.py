import string

def is_in_class(value, char_set):
    if not value:
        return False
    return all(char in char_set for char in value)

def main():
    # Define Classes
    class_a_g = set(string.ascii_uppercase[0:7] + string.ascii_lowercase[0:7] + "789")
    class_a_g_upper = set(string.ascii_uppercase[0:7])
    class_a_g_lower = set(string.ascii_lowercase[0:7])
    class_binario = set("01")
    class_hex = set(string.digits + "ABCDEFabcdef")

    # Working Storage
    wk_valor1 = ""
    wk_valor2 = ""
    wk_valor3 = ""
    wk_valor4 = ""

    # 1000-INICIO / 1100-INICIAR-VARIABLES
    wk_valor1 = ""
    wk_valor2 = ""
    wk_valor3 = ""
    wk_valor4 = ""

    # 2000-PROCESO
    
    # 2100-SOLICITA-VALOR1
    print("--------------------------------------------")
    print("Introduce cuatro caracteres en mayúscula entre A y G:")
    print("--------------------------------------------")
    wk_valor1 = input()

    # 2101-COMPRUEBA-VALOR1
    if is_in_class(wk_valor1, class_a_g_upper) or is_in_class(wk_valor1, class_a_g_lower):
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor1} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor1} y no está en el rango")
        print("--------------------------------------------")

    # 2200-SOLICITA-VALOR2
    print("Introduce cuatro caracteres:")
    print("--------------------------------------------")
    wk_valor2 = input()

    # 2201-COMPRUEBA-VALOR2
    if is_in_class(wk_valor2, class_a_g):
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor2} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor2} y no está en el rango")
        print("--------------------------------------------")
        print("INTÉNTALO DE NUEVO")
        print("--------------------------------------------")
        wk_valor2 = input()
        print("--------------------------------------------")
        
        if is_in_class(wk_valor2, class_a_g):
            print("--------------------------------------------")
            print(f"Has escrito {wk_valor2} y está en el rango")
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
            print("Has escrito dos veces y fuera de rango")
            print("--------------------------------------------")
            print("ÚLTIMO INTENTO")
            print("--------------------------------------------")
            wk_valor2 = input()
            print("--------------------------------------------")
            
            if is_in_class(wk_valor2, class_a_g):
                print("--------------------------------------------")
                print(f"Has escrito {wk_valor2} y está en el rango")
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
                print("Has escrito tres veces y fuera de rango")
                print("--------------------------------------------")

    # 2300-SOLICITA-VALOR3
    print("Introduce un binario de 4 dígitos:")
    print("--------------------------------------------")
    wk_valor3 = input()

    # 2301-COMPRUEBA-VALOR3
    if is_in_class(wk_valor3, class_binario):
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor3} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor3} y no está en el rango")
        print("--------------------------------------------")

    # 2400-SOLICITA-VALOR4
    print("Introduce un hexadecimal de 6 dígitos:")
    print("--------------------------------------------")
    wk_valor4 = input()

    # 2401-COMPRUEBA-VALOR4
    if is_in_class(wk_valor4, class_hex):
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor4} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor4} y no está en el rango")
        print("--------------------------------------------")

if __name__ == "__main__":
    main()
