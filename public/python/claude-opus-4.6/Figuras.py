"""
Geometric Figures Area Calculator
Converted from COBOL (Figuras.cbl) to Python

Calculates the area of a triangle, square/rectangle, or pentagon
based on user input.
"""


def calc_area_triangle(base, altura):
    """Calculate area of a triangle."""
    return base * altura / 2


def calc_area_cuadrado(base, altura):
    """Calculate area of a rectangle/square."""
    return base * altura


def calc_area_pentagono(apotema, lado):
    """Calculate area of a regular pentagon."""
    return (5 * lado * apotema) / 2


def pedir_base_altura():
    """Request base and height from user."""
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))
    return base, altura


def main():
    area_figura = 0

    print("Introduzca un nombre de figura en minusculas y sin accentos")
    figura = input().strip().lower()

    triangulo_vals = ("triangulo", "t")
    cuadrado_vals = ("cuadrado", "c")
    pentagono_vals = ("pentagono", "p")

    if figura in triangulo_vals:
        base, altura = pedir_base_altura()
        area_figura = calc_area_triangle(base, altura)
    elif figura in cuadrado_vals:
        base, altura = pedir_base_altura()
        area_figura = calc_area_cuadrado(base, altura)
    elif figura in pentagono_vals:
        apotema = int(input("Introduce el apotema: "))
        lado = int(input("Introduce el lado: "))
        area_figura = calc_area_pentagono(apotema, lado)
    else:
        print("Figura no prevista")

    if area_figura != 0:
        print(f"El area es de: {int(area_figura)} u^2")


if __name__ == "__main__":
    main()
