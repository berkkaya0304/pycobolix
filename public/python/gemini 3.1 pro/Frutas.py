def main():
    tabla_frutas = [""] * 10
    indice = 1
    
    while True:
        if indice > 10:
            break
            
        print("Teclea el nombre de una fruta: ")
        fruta_tecleada = input()
        
        tabla_frutas[indice - 1] = fruta_tecleada
        indice += 1
        
        print("Deseas continuar? (S/N)")
        continuar_si_no = input()
        
        if continuar_si_no in ["N", "n"]:
            break
            
    if indice > 10:
        print("La tabla está llena.")
    else:
        print("Aún quedan elementos por rellenar.")

if __name__ == "__main__":
    main()
