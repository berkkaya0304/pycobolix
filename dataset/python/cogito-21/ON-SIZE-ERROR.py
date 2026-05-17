def main():
    wk_numero1 = 200
    wk_numero2 = 100
    wk_numero3 = 3
    wk_numero4 = 4
    wk_resultado = 0
    wk_resultado_grande = 0

    def parrafo_2100():
        nonlocal wk_resultado
        try:
            temp = wk_numero1 * wk_numero2
            if temp > 999:
                raise OverflowError
            wk_resultado = temp
        except OverflowError:
            print("NUMERO DEMASIADO GRANDE")
            print(wk_resultado)

    def parrafo_2200():
        nonlocal wk_resultado, wk_resultado_grande
        try:
            temp = wk_numero1 * wk_numero2
            if temp > 999:
                raise OverflowError
            wk_resultado = temp
        except OverflowError:
            wk_resultado_grande = wk_numero1 * wk_numero2
            print(wk_resultado_grande)

    def parrafo_2300():
        nonlocal wk_resultado
        try:
            temp = wk_numero1 * wk_numero2
            if temp > 999:
                raise OverflowError
            wk_resultado = temp
            print(wk_resultado)
        except OverflowError:
            print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
            print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
            wk_resultado = 200
        print(wk_resultado)

    def parrafo_2400():
        nonlocal wk_resultado
        try:
            temp = wk_numero3 * wk_numero4
            if temp > 999:
                raise OverflowError
            wk_resultado = temp
            print(wk_resultado)
        except OverflowError:
            print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
            print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
            wk_resultado = 200

    parrafo_2100()
    parrafo_2200()
    parrafo_2300()
    parrafo_2400()

if __name__ == "__main__":
    main()
