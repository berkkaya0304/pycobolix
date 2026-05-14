def pedir_base_altura():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    return base, altura

def calc_area_triangulo():
    base, altura = pedir_base_altura()
    return (base * altura) / 2

def calc_area_cuadrado():
    base, altura = pedir_base_altura()
    return base * altura

def calc_area_pentagono():
    apotema = float(input("Introduce el apotema: "))
    lado = float(input("Introduce el lado: "))
    return (5 * lado * apotema) / 2

def main():
    print("Introduzca un nombre de figura en minusculas y sin accentos")
    figura = input().strip().lower()

    area_figura = 0

    if figura in ["triangulo", "t"]:
        area_figura = calc_area_triangulo()
    elif figura in ["cuadrado", "c"]:
        area_figura = calc_area_cuadrado()
    elif figura in ["pentagono", "p"]:
        area_figura = calc_area_pentagono()
    else:
        print("Figura no prevista")

    if area_figura != 0:
        print(f"El area es de: {area_figura} u^2")

if __name__ == "__main__":
    main()
