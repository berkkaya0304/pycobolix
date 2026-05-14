def main():
    wk_numero1 = 200
    wk_numero2 = 100
    wk_numero3 = 3
    wk_numero4 = 4
    wk_resultado = 0
    wk_resultado_grande = 0

    # 2100-PARRAFO
    # Simulating PIC 9(3) overflow
    temp_resultado = wk_numero1 * wk_numero2
    if temp_resultado > 999:
        print("NUMERO DEMASIADO GRANDE")
        print(f"{wk_resultado:03d}")
    else:
        wk_resultado = temp_resultado
        
    # 2200-PARRAFO
    temp_resultado = wk_numero1 * wk_numero2
    if temp_resultado > 999:
        wk_resultado_grande = temp_resultado
        print(f"{wk_resultado_grande:05d}")
    else:
        wk_resultado = temp_resultado

    # 2300-PARRAFO
    temp_resultado = wk_numero1 * wk_numero2
    if temp_resultado > 999:
        print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
        print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
        wk_resultado = 200
        # NOT ON SIZE ERROR block won't run
    else:
        wk_resultado = temp_resultado
        print(f"{wk_resultado:03d}")

    print(f"{wk_resultado:03d}")

    # 2400-PARRAFO
    temp_resultado = wk_numero3 * wk_numero4
    if temp_resultado > 999:
        print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
        print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
        wk_resultado = 200
    else:
        wk_resultado = temp_resultado
        print(f"{wk_resultado:03d}")

if __name__ == "__main__":
    main()
