def main():
    wk_aux = 0
    wk_indice_array = 0
    wk_contador = 0
    wk_valor_array = [0] * 5

    # 1000-INICIO
    wk_valor_array[0] = 5
    wk_valor_array[1] = 1
    wk_valor_array[2] = 4
    wk_valor_array[3] = 2
    wk_valor_array[4] = 8

    # 2000-PROCESO
    # 2100-MOSTRAR-ARRAY
    print("EL ARRAY ACTUAL ES: ", end="")
    for idx in range(5):
        print(wk_valor_array[idx], end="")
        if idx < 4:
            print(", ", end="")
        else:
            print(" ")

    # 2200-ORDENAR-ARRAY (Bubble Sort)
    wk_indice_array = 1
    while wk_indice_array <= 4:
        wk_contador = 1
        while wk_contador <= 5 - wk_indice_array:
            if wk_valor_array[wk_contador - 1] > wk_valor_array[wk_contador]:
                wk_aux = wk_valor_array[wk_contador - 1]
                wk_valor_array[wk_contador - 1] = wk_valor_array[wk_contador]
                wk_valor_array[wk_contador] = wk_aux
            wk_contador += 1
        wk_indice_array += 1

    # 2300-MOSTRAR-ARRAY-ORDENADO
    print("EL ARRAY ORDENADO ES: ", end="")
    wk_indice_array = 1
    while wk_indice_array <= 5:
        print(wk_valor_array[wk_indice_array - 1], end="")
        if wk_indice_array < 5:
            print(", ", end="")
        wk_indice_array += 1
    print()

if __name__ == "__main__":
    main()
