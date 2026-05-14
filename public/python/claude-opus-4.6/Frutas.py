"""
Fruit Table Input Program
Converted from COBOL (Frutas.cbl) to Python

Allows the user to enter up to 10 fruit names into a table,
with the option to stop early.
"""


def main():
    tabla_frutas = [""] * 10
    indice = 0

    while indice < 10:
        fruta = input("Teclea el nombre de una fruta: ")
        tabla_frutas[indice] = fruta
        indice += 1

        if indice < 10:
            continuar = input("Deseas continuar? (S/N) ").strip().upper()
            if continuar == "N":
                break

    if indice >= 10:
        print("La tabla está llena.")
    else:
        print("Aún quedan elementos por rellenar.")


if __name__ == "__main__":
    main()
