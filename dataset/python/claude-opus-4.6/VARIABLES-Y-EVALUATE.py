"""
Variables and Evaluate (EVALUATE TRUE / IF-ELSE) Demonstration
Converted from COBOL (VARIABLES-Y-EVALUATE.cbl) to Python

Demonstrates structured data (student/teacher records), level-88
condition names for age ranges, EVALUATE TRUE for age classification,
and color classification using condition-name value lists.
"""


def main():
    # Data structure for users
    usuario = {
        "alumno": {
            "nombre": "",
            "apellido1": "",
            "apellido2": "",
            "telefono1": "",
            "telefono2": "",
        },
        "profesor": {
            "nombre": "",
            "apellido1": "",
            "apellido2": "",
            "telefono1": "",
            "telefono2": "",
        },
    }

    otra_variable_independiente = 0

    # 2000-PROCESO
    comprueba_edad()
    comprueba_edad_evaluate()
    comprueba_evaluate_true()
    selecciona_color()


def comprueba_edad():
    """2100-COMPRUEBA-EDAD: Check age using IF statements."""
    print("INTRODUCE TU EDAD:")
    edad = int(input())

    if 1 <= edad <= 39:
        print("ERES JOVEN, ", end="")
    elif 40 <= edad <= 65:
        print("ERES MADURO, ", end="")
    elif 66 <= edad <= 100:
        print("ERES ANCIANO, ", end="")

    print(f"TIENES {edad:03d} AÑOS.")


def comprueba_edad_evaluate():
    """2200-COMPRUEBA-EDAD-EVALUATE: Check age using EVALUATE-style logic."""
    print("INTRODUCE TU EDAD: ")
    edad = int(input())

    if 1 <= edad <= 39:
        print(f"ERES JOVEN, TU EDAD ES {edad:03d}.")
    elif 40 <= edad <= 65:
        print(f"ERES MADURO, TU EDAD ES {edad:03d}.")
    elif 66 <= edad <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {edad:03d}.")
    else:
        print("EDAD INCORRECTA.")


def comprueba_evaluate_true():
    """2300-COMPRUEBA-EVALUATE-TRUE: Same check using EVALUATE TRUE."""
    print("INTRODUCE TU EDAD: ")
    edad = int(input())

    if 1 <= edad <= 39:
        print(f"ERES JOVEN, TU EDAD ES {edad:03d}.")
    elif 40 <= edad <= 65:
        print(f"ERES MADURO, TU EDAD ES {edad:03d}.")
    elif 66 <= edad <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {edad:03d}.")
    else:
        print("EDAD INCORRECTA.")


def selecciona_color():
    """2400-SELECCIONA-COLOR: Classify a color as primary or secondary."""
    primarios = ("AMARILLO", "AZUL", "ROJO")
    secundarios = ("NARANJA", "VERDE", "VIOLETA")

    print("INTRODUCE UN COLOR:")
    color = input().strip().upper()

    if color in primarios:
        print("ESE COLOR ES PRIMARIO.")
    elif color in secundarios:
        print("ESE COLOR ES SECUNDARIO.")
    else:
        print("NO TENGO ALMACENADO ESE COLOR.")


if __name__ == "__main__":
    main()
