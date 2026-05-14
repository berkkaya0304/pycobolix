"""
ON SIZE ERROR Handling Demonstration
Converted from COBOL (ON-SIZE-ERROR.cbl) to Python

Demonstrates arithmetic overflow handling similar to COBOL's
ON SIZE ERROR clause, using Python try/except and range checks.
"""


def main():
    wk_numero1 = 200
    wk_numero2 = 100
    wk_numero3 = 3
    wk_numero4 = 4
    max_resultado = 999          # PIC 9(3) max value
    max_resultado_grande = 99999  # PIC 9(5) max value

    # 2100-PARRAFO: Multiply and detect overflow in 3-digit result
    resultado = wk_numero1 * wk_numero2
    if resultado > max_resultado:
        print("NUMERO DEMASIADO GRANDE")
        print(0)  # COBOL would show zeroed-out result
    else:
        print(resultado)

    # 2200-PARRAFO: On overflow, use a larger result variable
    resultado = wk_numero1 * wk_numero2
    if resultado > max_resultado:
        resultado_grande = wk_numero1 * wk_numero2
        if resultado_grande <= max_resultado_grande:
            print(resultado_grande)
    else:
        print(resultado)

    # 2300-PARRAFO: On overflow set default; otherwise display result
    resultado = wk_numero1 * wk_numero2
    if resultado > max_resultado:
        print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
        print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
        resultado = 200
    else:
        print(resultado)
    print(resultado)

    # 2400-PARRAFO: Small multiplication that fits
    resultado = wk_numero3 * wk_numero4
    if resultado > max_resultado:
        print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
        print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
        resultado = 200
    else:
        print(resultado)


if __name__ == "__main__":
    main()
