"""
Bubble Sort Array Program
Converted from COBOL (ARRAY-BURBUJEO.cbl) to Python
"""


def main():
    # 1000-INICIO: Initialize the array
    array = [5, 1, 4, 2, 8]

    # 2000-PROCESO
    display_array(array)
    sort_array(array)
    display_sorted_array(array)


def display_array(array):
    """2100-MOSTRAR-ARRAY: Display the current array."""
    print("EL ARRAY ACTUAL ES: ")
    for i in range(len(array)):
        if i < len(array) - 1:
            print(array[i], end=", ")
        else:
            print(array[i])


def sort_array(array):
    """2200-ORDENAR-ARRAY: Bubble sort the array in ascending order."""
    n = len(array)
    for i in range(1, n):
        for j in range(0, n - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def display_sorted_array(array):
    """2300-MOSTRAR-ARRAY-ORDENADO: Display the sorted array."""
    print("EL ARRAY ORDENADO ES: ")
    for i in range(len(array)):
        if i < len(array) - 1:
            print(array[i], end=", ")
        else:
            print(array[i])


if __name__ == "__main__":
    main()
