"""
Character Class Validation Program
Converted from COBOL (CLASES.cbl) to Python

Demonstrates character class checking (A-G uppercase, A-G lowercase,
binary digits, hexadecimal digits) with retry logic for validation.
"""

import re


def is_a_g_upper(value):
    """Check if all characters are uppercase A-G."""
    return bool(re.fullmatch(r'[A-G]+', value))


def is_a_g_lower(value):
    """Check if all characters are lowercase a-g."""
    return bool(re.fullmatch(r'[a-g]+', value))


def is_a_g(value):
    """Check if all characters are in A-G (upper or lower) or 7-9."""
    return bool(re.fullmatch(r'[A-Ga-g7-9]+', value))


def is_binary(value):
    """Check if all characters are binary (0 or 1)."""
    return bool(re.fullmatch(r'[01]+', value))


def is_hex(value):
    """Check if all characters are hexadecimal."""
    return bool(re.fullmatch(r'[0-9A-Fa-f]+', value))


def main():
    # 1000-INICIO: Initialize variables
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

    # 2201-COMPRUEBA-VALOR2 (with up to 3 attempts)
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
    if is_binary(wk_valor3):
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

    # 3000-FIN
    print("Program finished.")


if __name__ == "__main__":
    main()
