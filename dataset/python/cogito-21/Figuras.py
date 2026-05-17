def main():
    figura = input("Introduzca un nombre de figura en minusculas y sin accentos: ").strip().lower()
    area = 0

    if figura in ["triangulo", "t"]:
        area = calcular_area_triangulo()
    elif figura in ["cuadrado", "c"]:
        area = calcular_area_cuadrado()
    elif figura in ["pentagono", "p"]:
        area = calcular_area_pentagono()
    else:
        print("Figura no prevista")
        return

    if area != 0:
        print(f"El area es de: {area} u^2")

def pedir_base_altura():
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))
    return base, altura

def calcular_area_triangulo():
    base, altura = pedir_base_altura()
    return (base * altura) // 2

def calcular_area_cuadrado():
    base, altura = pedir_base_altura()
    return base * altura

def calcular_area_pentagono():
    apotema = int(input("Introduce el apotema: "))
    lado = int(input("Introduce el lado: "))
    return (5 * lado * apotema) // 2

if __name__ == "__main__":
    main()
