class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name1 = ""
        self.last_name2 = ""
        self.phone1 = ""
        self.phone2 = ""

class Teacher:
    def __init__(self):
        self.first_name = ""
        self.last_name1 = ""
        self.last_name2 = ""
        self.phone1 = ""
        self.phone2 = ""

class User:
    def __init__(self):
        self.student = Student()
        self.teacher = Teacher()

def check_age_if(age):
    if 1 <= age <= 39:
        print("ERES JOVEN, ", end="")
    if 40 <= age <= 65:
        print("ERES MADURO, ", end="")
    if 66 <= age <= 100:
        print("ERES ANCIANO, ", end="")
    print(f"TIENES {age} AÑOS.")

def check_age_evaluate(age):
    if 1 <= age <= 39:
        print(f"ERES JOVEN, TU EDAD ES {age}.")
    elif 40 <= age <= 65:
        print(f"ERES MADURO, TU EDAD ES {age}.")
    elif 66 <= age <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {age}.")
    else:
        print("EDAD INCORRECTA.")

def check_age_evaluate_true(age):
    if 1 <= age <= 39:
        print(f"ERES JOVEN, TU EDAD ES {age}.")
    elif 40 <= age <= 65:
        print(f"ERES MADURO, TU EDAD ES {age}.")
    elif 66 <= age <= 100:
        print(f"ERES ANCIANO, TU EDAD ES {age}.")
    else:
        print("EDAD INCORRECTA.")

def select_color():
    primary_colors = {"AMARILLO", "AZUL", "ROJO"}
    secondary_colors = {"NARANJA", "VERDE", "VIOLETA"}
    
    color = input("INTRODUCE UN COLOR: ").strip().upper()
    
    if color in primary_colors:
        print("ESE COLOR ES PRIMARIO.")
    elif color in secondary_colors:
        print("ESE COLOR ES SECUNDARIO.")
    else:
        print("NO TENGO ALMACENADO ESE COLOR.")

def main():
    user = User()
    independent_variable = 0
    age = 0
    
    print("INTRODUCE TU EDAD:")
    try:
        age = int(input())
        check_age_if(age)
    except ValueError:
        print("EDAD INCORRECTA.")
    
    print("INTRODUCE TU EDAD: ")
    try:
        age = int(input())
        check_age_evaluate(age)
    except ValueError:
        print("EDAD INCORRECTA.")
    
    print("INTRODUCE TU EDAD: ")
    try:
        age = int(input())
        check_age_evaluate_true(age)
    except ValueError:
        print("EDAD INCORRECTA.")
    
    select_color()

if __name__ == "__main__":
    main()
