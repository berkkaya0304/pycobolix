def main():
    tabla_frutas = [""] * 10
    indice = 0

    def introducir_frutas():
        nonlocal indice
        fruta_tecleada = input("Teclea el nombre de una fruta: ").strip()
        tabla_frutas[indice] = fruta_tecleada
        indice += 1

    def continuar_pregunta():
        while True:
            respuesta = input("Deseas continuar? (S/N) ").strip().lower()
            if respuesta in ("s", "n"):
                return respuesta == "s"
            print("Por favor, introduce S o N.")

    def evaluar_resultado():
        if indice >= 10:
            print("La tabla está llena.")
        else:
            print("Aún quedan elementos por rellenar.")

    while indice < 10:
        introducir_frutas()
        if indice < 10 and not continuar_pregunta():
            break

    evaluar_resultado()

if __name__ == "__main__":
    main()
