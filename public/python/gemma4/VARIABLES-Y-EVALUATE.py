from dataclasses import dataclass, field
from typing import List

@dataclass
class Alumno:
    nombre: str = ""
    apellido1: str = ""
    apellido2: str = ""
    telefono1: str = ""
    telefono2: str = ""

@dataclass
class Profesor:
    nombre: str = ""
    apellido1: str = ""
    apellido2: str = ""
    telefono1: str = ""
    telefono2: str = ""

@dataclass
class Usuario:
    alumno: Alumno = field(default_factory=Alumno)
    profesor: Profesor = field(default_factory=Profesor)

class VariablesYEvaluate:
    def __init__(self):
        self.usuario = Usuario()
        self.otra_variable_independiente = 0
        self.edad = 0
        self.colores = ""

    @property
    def is_joven(self) -> bool:
        return 1 <= self.edad <= 39

    @property
    def is_maduro(self) -> bool:
        return 40 <= self.edad <= 65

    @property
    def is_anciano(self) -> bool:
        return 66 <= self.edad <= 100

    @property
    def is_primario(self) -> bool:
        return self.colores.strip().upper() in ["AMARILLO", "AZUL", "ROJO"]

    @property
    def is_secundario(self) -> bool:
        return self.colores.strip().upper() in ["NARANJA", "VERDE", "VIOLETA"]

    def inicio(self):
        pass

    def proceso(self):
        self.comprueba_edad()
        self.comprueba_edad_evaluate()
        self.comprueba_evaluate_true()
        self.selecciona_color()

    def comprueba_edad(self):
        try:
            self.edad = int(input("INTRODUCE TU EDAD:\n"))
        except ValueError:
            self.edad = 0

        output = ""
        if self.is_joven:
            output += "ERES JOVEN, "
        if self.is_maduro:
            output += "ERES MADURO, "
        if self.is_anciano:
            output += "ERES ANCIANO, "
        
        print(f"{output}TIENES {self.edad} AÑOS.")

    def comprueba_edad_evaluate(self):
        try:
            self.edad = int(input("INTRODUCE TU EDAD: "))
        except ValueError:
            self.edad = -1

        if 1 <= self.edad <= 39:
            print(f"ERES JOVEN, TU EDAD ES {self.edad}.")
        elif 40 <= self.edad <= 65:
            print(f"ERES MADURO, TU EDAD ES {self.edad}.")
        elif 66 <= self.edad <= 100:
            print(f"ERES ANCIANO, TU EDAD ES {self.edad}.")
        else:
            print("EDAD INCORRECTA.")

    def comprueba_evaluate_true(self):
        try:
            self.edad = int(input("INTRODUCE TU EDAD: "))
        except ValueError:
            self.edad = 0

        if self.is_joven:
            print(f"ERES JOVEN, TU EDAD ES {self.edad}.")
        elif self.is_maduro:
            print(f"ERES MADURO, TU EDAD ES {self.edad}.")
        elif self.is_anciano:
            print(f"ERES ANCIANO, TU EDAD ES {self.edad}.")
        else:
            print("EDAD INCORRECTA.")

    def selecciona_color(self):
        self.colores = input("INTRODUCE UN COLOR:\n")
        if self.is_primario:
            print("ESE COLOR ES PRIMARIO.")
        elif self.is_secundario:
            print("ESE COLOR ES SECUNDARIO.")
        else:
            print("NO TENGO ALMACENADO ESE COLOR.")

    def fin(self):
        pass

if __name__ == "__main__":
    app = VariablesYEvaluate()
    app.inicio()
    app.proceso()
    app.fin()
