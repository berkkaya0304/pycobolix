def is_a_g(char):
    return ('A' <= char <= 'G') or ('a' <= char <= 'g') or ('7' <= char <= '9')

def is_a_g_upper(char):
    return 'A' <= char <= 'G'

def is_a_g_lower(char):
    return 'a' <= char <= 'g'

def is_binario(char):
    return char in ('0', '1')

def is_hex(char):
    return ('0' <= char <= '9') or ('A' <= char <= 'F') or ('a' <= char <= 'f')

def check_all_chars(value, check_func):
    return all(check_func(c) for c in value)

def initialize_variables():
    return {
        'WK-VALOR1': '    ',
        'WK-VALOR2': '    ',
        'WK-VALOR3': '    ',
        'WK-VALOR4': '        '
    }

def solicita_valor1(variables):
    print("--------------------------------------------")
    print("Introduce cuatro caracteres en mayúscula entre A y G:")
    print("--------------------------------------------")
    variables['WK-VALOR1'] = input().strip()[:4].ljust(4)

def comprueba_valor1(variables):
    if check_all_chars(variables['WK-VALOR1'], lambda c: is_a_g_upper(c) or is_a_g_lower(c)):
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR1']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR1']} y no está en el rango")
        print("--------------------------------------------")

def solicita_valor2(variables):
    print("Introduce cuatro caracteres:")
    print("--------------------------------------------")
    variables['WK-VALOR2'] = input().strip()[:4].ljust(4)

def comprueba_valor2(variables):
    for attempt in range(3):
        if check_all_chars(variables['WK-VALOR2'], is_a_g):
            print("--------------------------------------------")
            print(f"Has escrito {variables['WK-VALOR2']} y está en el rango")
            print("--------------------------------------------")
            break
        else:
            print("--------------------------------------------")
            print(f"Has escrito {variables['WK-VALOR2']} y no está en el rango")
            print("--------------------------------------------")
            if attempt < 2:
                if attempt == 0:
                    print("INTÉNTALO DE NUEVO")
                elif attempt == 1:
                    print("ÚLTIMO INTENTO")
                print("--------------------------------------------")
                variables['WK-VALOR2'] = input().strip()[:4].ljust(4)
                print("--------------------------------------------")
            else:
                print("Has escrito tres veces y fuera de rango")
                print("--------------------------------------------")

def solicita_valor3(variables):
    print("Introduce un binario de 4 dígitos:")
    print("--------------------------------------------")
    variables['WK-VALOR3'] = input().strip()[:4].ljust(4)

def comprueba_valor3(variables):
    if check_all_chars(variables['WK-VALOR3'], is_binario):
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR3']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR3']} y no está en el rango")
        print("--------------------------------------------")

def solicita_valor4(variables):
    print("Introduce un hexadecimal de 6 dígitos:")
    print("--------------------------------------------")
    variables['WK-VALOR4'] = input().strip()[:6].ljust(6)

def comprueba_valor4(variables):
    if check_all_chars(variables['WK-VALOR4'], is_hex):
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR4']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {variables['WK-VALOR4']} y no está en el rango")
        print("--------------------------------------------")

def main():
    variables = initialize_variables()

    solicita_valor1(variables)
    comprueba_valor1(variables)

    solicita_valor2(variables)
    comprueba_valor2(variables)

    solicita_valor3(variables)
    comprueba_valor3(variables)

    solicita_valor4(variables)
    comprueba_valor4(variables)

if __name__ == "__main__":
    main()
