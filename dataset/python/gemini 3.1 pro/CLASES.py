import re

def is_a_g(val, ignore_case=True):
    pattern = r'^[A-Ga-g7-9]+$' if ignore_case else r'^[A-Ga-g7-9]+$'
    return bool(re.match(pattern, val))

def is_a_g_upper(val):
    return bool(re.match(r'^[A-G]+$', val))

def is_a_g_lower(val):
    return bool(re.match(r'^[a-g]+$', val))

def is_binario(val):
    return bool(re.match(r'^[01]+$', val))

def is_hex(val):
    return bool(re.match(r'^[0-9A-Fa-f]+$', val))

def main():
    # 1000-INICIO
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
    if is_a_g_upper(wk_valor1) or is_a_g_lower(wk_valor1):
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
    if is_a_g(wk_valor2):
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
        if is_a_g(wk_valor2):
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
            if is_a_g(wk_valor2):
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
    if is_binario(wk_valor3):
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
    if is_hex(wk_valor4):
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor4} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {wk_valor4} y no está en el rango")
        print("--------------------------------------------")

if __name__ == "__main__":
    main()
