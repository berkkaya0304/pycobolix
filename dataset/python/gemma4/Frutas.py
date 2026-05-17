def main():
    tabla_frutas = []
    continuar = True

    while len(tabla_frutas) < 10 and continuar:
        fruta_tecleada = input("Teclea el nombre de una fruta: ")
        tabla_frutas.append(fruta_tecleada)
        
        respuesta = input("Deseas continuar? (S/N)").upper()
        if respuesta == 'N':
            continuar = False

    if len(tabla_frutas) >= 10:
        print("La tabla está llena.")
    else:
        print("Aún quedan elementos por rellenar.")

if __name__ == "__main__":
    main()
