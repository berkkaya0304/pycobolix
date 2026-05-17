class CharacterClasses:
    @staticmethod
    def is_a_g_upper(char):
        return 'A' <= char <= 'G'
    
    @staticmethod
    def is_a_g_lower(char):
        return 'a' <= char <= 'g'
    
    @staticmethod
    def is_a_g(char):
        return CharacterClasses.is_a_g_upper(char) or CharacterClasses.is_a_g_lower(char) or ('7' <= char <= '9')
    
    @staticmethod
    def is_binary(char):
        return char in ('0', '1')
    
    @staticmethod
    def is_hex(char):
        return ('0' <= char <= '9') or ('A' <= char <= 'F') or ('a' <= char <= 'f')

def check_all_chars(string, check_func):
    return all(check_func(char) for char in string)

def main():
    valores = {
        'WK-VALOR1': 'ABCD',
        'WK-VALOR2': 'A9cD',
        'WK-VALOR3': '0101',
        'WK-VALOR4': 'aC24FF'
    }
    
    # Reset values to spaces
    for key in valores:
        valores[key] = ' ' * len(valores[key])
    
    # Process WK-VALOR1
    print("--------------------------------------------")
    print("Introduce cuatro caracteres en mayúscula entre A y G:")
    print("--------------------------------------------")
    valores['WK-VALOR1'] = input().strip().upper().ljust(4)[:4]
    
    if check_all_chars(valores['WK-VALOR1'], CharacterClasses.is_a_g_upper):
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR1']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR1']} y no está en el rango")
        print("--------------------------------------------")
    
    # Process WK-VALOR2
    print("Introduce cuatro caracteres:")
    print("--------------------------------------------")
    valores['WK-VALOR2'] = input().strip().ljust(4)[:4]
    
    attempts = 0
    while attempts < 3:
        if check_all_chars(valores['WK-VALOR2'], CharacterClasses.is_a_g):
            print("--------------------------------------------")
            print(f"Has escrito {valores['WK-VALOR2']} y está en el rango")
            print("--------------------------------------------")
            break
        else:
            attempts += 1
            if attempts < 3:
                print("--------------------------------------------")
                print(f"Has escrito {valores['WK-VALOR2']} y no está en el rango")
                print("--------------------------------------------")
                print("INTÉNTALO DE NUEVO")
                print("--------------------------------------------")
                valores['WK-VALOR2'] = input().strip().ljust(4)[:4]
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
                print("Has escrito tres veces y fuera de rango")
                print("--------------------------------------------")
    
    # Process WK-VALOR3
    print("Introduce un binario de 4 dígitos:")
    print("--------------------------------------------")
    valores['WK-VALOR3'] = input().strip().ljust(4)[:4]
    
    if check_all_chars(valores['WK-VALOR3'], CharacterClasses.is_binary):
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR3']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR3']} y no está en el rango")
        print("--------------------------------------------")
    
    # Process WK-VALOR4
    print("Introduce un hexadecimal de 6 dígitos:")
    print("--------------------------------------------")
    valores['WK-VALOR4'] = input().strip().upper().ljust(6)[:6]
    
    if check_all_chars(valores['WK-VALOR4'], CharacterClasses.is_hex):
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR4']} y está en el rango")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Has escrito {valores['WK-VALOR4']} y no está en el rango")
        print("--------------------------------------------")

if __name__ == "__main__":
    main()
