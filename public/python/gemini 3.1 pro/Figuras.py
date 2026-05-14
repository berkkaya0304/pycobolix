def main():
    area_figura = 0

    print("Introduzca un nombre de figura en minusculas y sin accentos")
    figura = input()

    if figura in ["triangulo", "TRIANGULO", "t", "T"]:
        print("Introduce la base: ")
        base = int(input())
        print("Introduce la altura: ")
        altura = int(input())
        area_figura = base * altura / 2
    elif figura in ["cuadrado", "CUADRADO", "c", "C"]:
        print("Introduce la base: ")
        base = int(input())
        print("Introduce la altura: ")
        altura = int(input())
        area_figura = base * altura
    elif figura in ["pentagono", "PENTAGONO", "p", "P"]:
        print("Introduce el apotema: ")
        apotema = int(input())
        print("Introduce el lado: ")
        lado = int(input())
        area_figura = 5 * lado
        area_figura = area_figura * apotema
        area_figura = area_figura / 2
    else:
        print("Figura no prevista")

    if area_figura != 0:
        print(f"El area es de: {int(area_figura):04d} u^2")

if __name__ == "__main__":
    main()
