def main():
    array = [5, 1, 4, 2, 8]
    
    print("EL ARRAY ACTUAL ES: ", end="")
    print(*array, sep=", ")
    
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    print("EL ARRAY ORDENADO ES: ", end="")
    print(*array, sep=", ")

if __name__ == "__main__":
    main()
