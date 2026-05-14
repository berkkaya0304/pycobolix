def is_joven(edad):
    return 1 <= edad <= 39

def is_maduro(edad):
    return 40 <= edad <= 65

def is_anciano(edad):
    return 66 <= edad <= 100

def is_primarios(color):
    return color.strip().upper() in ["AMARILLO", "AZUL", "ROJO"]

def is_secundarios(color):
    return color.strip().upper() in ["NARANJA", "VERDE", "VIOLETA"]

def main():
    # 2100-COMPRUEBA-EDAD
    try:
        wk_edad = int(input("INTRODUCE TU EDAD:\n"))
    except ValueError:
        wk_edad = 0

    if is_joven(wk_edad):
        print("ERES JOVEN, ", end="")
    if is_maduro(wk_edad):
        print("ERES MADURO, ", end="")
    if is_anciano(wk_edad):
        print("ERES ANCIANO, ", end="")

    print(f"TIENES {wk_edad:03d} AÑOS.")

    # 2200-COMPRUEBA-EDAD-EVALUATE
    try:
        wk_edad = int(input("INTRODUCE TU EDAD: \n"))
    except ValueError:
        wk_edad = 0

    if 1 <= wk_edad <= 39:
        print(f"ERES JOVEN, TU EDAD ES {wk_edad:03d}.")
    elif 40 <= wk_edad <= 65:
        print(f"ERES MADURO, TU EDAD ES {wk_edad:03d}.")
    elif 66 <= wk_edad <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {wk_edad:03d}.")
    else:
        print("EDAD INCORRECTA.")

    # 2300-COMPRUEBA-EVALUATE-TRUE
    try:
        wk_edad = int(input("INTRODUCE TU EDAD: \n"))
    except ValueError:
        wk_edad = 0

    if is_joven(wk_edad):
        print(f"ERES JOVEN, TU EDAD ES {wk_edad:03d}.")
    elif is_maduro(wk_edad):
        print(f"ERES MADURO, TU EDAD ES {wk_edad:03d}.")
    elif is_anciano(wk_edad):
        print(f"ERES ANCIANO, TU EDAD ES {wk_edad:03d}.")
    else:
        print("EDAD INCORRECTA.")

    # 2400-SELECCIONA-COLOR
    wk_colores = input("INTRODUCE UN COLOR:\n")

    if is_primarios(wk_colores):
        print("ESE COLOR ES PRIMARIO.")
    elif is_secundarios(wk_colores):
        print("ESE COLOR ES SECUNDARIO.")
    else:
        print("NO TENGO ALMACENADO ESE COLOR.")

if __name__ == "__main__":
    main()
