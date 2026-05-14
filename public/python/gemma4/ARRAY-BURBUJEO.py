def main():
    # 1000-INCIO: Initialize the array
    # COBOL arrays are 1-indexed; Python lists are 0-indexed.
    wk_valor_array = [5, 1, 4, 2, 8]

    # 2000-PROCESO: Process the array
    mostrar_array(wk_valor_array, "EL ARRAY ACTUAL ES: ")
    ordenar_array(wk_valor_array)
    mostrar_array(wk_valor_array, "EL ARRAY ORDENADO ES: ")

def mostrar_array(arr, message):
    # 2100-MOSTRAR-ARRAY and 2300-MOSTRAR-ARRAY-ORDENADO
    print(message, end="")
    for i in range(len(arr)):
        print(arr[i], end="")
        if i < len(arr) - 1:
            print(", ", end="")
    print()

def ordenar_array(arr):
    # 2200-ORDENAR-ARRAY: Bubble Sort implementation
    n = len(arr)
    # WK-INDICE-ARRAY loop
    for i in range(n - 1):
        # WK-CONTADOR loop
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap using WK-AUX logic
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

if __name__ == "__main__":
    main()
