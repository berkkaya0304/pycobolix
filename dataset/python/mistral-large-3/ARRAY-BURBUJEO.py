def main():
    # Initialize array
    array = [0] * 5
    array[0] = 5
    array[1] = 1
    array[2] = 4
    array[3] = 2
    array[4] = 8

    def mostrar_array(arr):
        print("EL ARRAY ACTUAL ES:", ", ".join(map(str, arr)))

    def ordenar_array(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def mostrar_array_ordenado(arr):
        print("EL ARRAY ORDENADO ES:", ", ".join(map(str, arr)))

    mostrar_array(array)
    ordenar_array(array)
    mostrar_array_ordenado(array)

if __name__ == "__main__":
    main()
