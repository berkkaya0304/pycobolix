class Usuario:
    def __init__(self):
        self.alumno = {
            'nombre': '',
            'apellidos': {
                'apellido1': '',
                'apellido2': ''
            },
            'telefonos': {
                'telefono1': '',
                'telefono2': ''
            }
        }
        self.profesor = {
            'nombre': '',
            'apellidos': {
                'apellido1': '',
                'apellido2': ''
            },
            'telefonos': {
                'telefono1': '',
                'telefono2': ''
            }
        }
        self.otra_variable_independiente = 0
        self.edad = 0
        self.color = ''

def es_joven(edad):
    return 1 <= edad <= 39

def es_maduro(edad):
    return 40 <= edad <= 65

def es_anciano(edad):
    return 66 <= edad <= 100

def es_color_primario(color):
    return color.upper() in ["AMARILLO", "AZUL", "ROJO"]

def es_color_secundario(color):
    return color.upper() in ["NARANJA", "VERDE", "VIOLETA"]

def comprobar_edad():
    usuario = Usuario()
    usuario.edad = int(input("INTRODUCE TU EDAD:"))

    if es_joven(usuario.edad):
        print("ERES JOVEN, ", end='')
    if es_maduro(usuario.edad):
        print("ERES MADURO, ", end='')
    if es_anciano(usuario.edad):
        print("ERES ANCIANO, ", end='')

    print(f"TIENES {usuario.edad} AÑOS.")

def comprobar_edad_evaluate():
    usuario = Usuario()
    usuario.edad = int(input("INTRODUCE TU EDAD: "))

    if 1 <= usuario.edad <= 39:
        print(f"ERES JOVEN, TU EDAD ES {usuario.edad}.")
    elif 40 <= usuario.edad <= 65:
        print(f"ERES MADURO, TU EDAD ES {usuario.edad}.")
    elif 66 <= usuario.edad <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {usuario.edad}.")
    else:
        print("EDAD INCORRECTA.")

def comprobar_evaluate_true():
    usuario = Usuario()
    usuario.edad = int(input("INTRODUCE TU EDAD: "))

    if es_joven(usuario.edad):
        print(f"ERES JOVEN, TU EDAD ES {usuario.edad}.")
    elif es_maduro(usuario.edad):
        print(f"ERES MADURO, TU EDAD ES {usuario.edad}.")
    elif es_anciano(usuario.edad):
        print(f"ERES ANCIANO, TU EDAD ES {usuario.edad}.")
    else:
        print("EDAD INCORRECTA.")

def seleccionar_color():
    usuario = Usuario()
    usuario.color = input("INTRODUCE UN COLOR:")

    if es_color_primario(usuario.color):
        print("ESE COLOR ES PRIMARIO.")
    elif es_color_secundario(usuario.color):
        print("ESE COLOR ES SECUNDARIO.")
    else:
        print("NO TENGO ALMACENADO ESE COLOR.")

def inicio():
    pass

def proceso():
    comprobar_edad()
    comprobar_edad_evaluate()
    comprobar_evaluate_true()
    seleccionar_color()

def fin():
    pass

def main():
    inicio()
    proceso()
    fin()

if __name__ == "__main__":
    main()
