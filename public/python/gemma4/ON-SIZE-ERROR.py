class OnSizeErrorProgram:
    def __init__(self):
        # PIC 9(3) -> Max 999
        self.wk_numero1 = 200
        self.wk_numero2 = 100
        self.wk_numero3 = 3
        self.wk_numero4 = 4
        self.wk_resultado = 0
        # PIC 9(5) -> Max 99999
        self.wk_resultado_grande = 0

    def run(self):
        self.inicio()
        self.proceso()
        self.fin()

    def inicio(self):
        pass

    def proceso(self):
        self.parrafo_2100()
        self.parrafo_2200()
        self.parrafo_2300()
        self.parrafo_2400()

    def parrafo_2100(self):
        result = self.wk_numero1 * self.wk_numero2
        if result > 999:
            print("NUMERO DEMASIADO GRANDE")
            print(self.wk_resultado)
        else:
            self.wk_resultado = result

    def parrafo_2200(self):
        result = self.wk_numero1 * self.wk_numero2
        if result > 999:
            self.wk_resultado_grande = result
            print(self.wk_resultado_grande)
        else:
            self.wk_resultado = result

    def parrafo_2300(self):
        result = self.wk_numero1 * self.wk_numero2
        if result > 999:
            print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
            print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
            self.wk_resultado = 200
        else:
            self.wk_resultado = result
            print(self.wk_resultado)
        
        print(self.wk_resultado)

    def parrafo_2400(self):
        result = self.wk_numero3 * self.wk_numero4
        if result > 999:
            print("EL NUMERO ES MUY GRANDE, NO SE VISUALIZA ENTERO")
            print("SE HA ESTABLECIDO EL VALOR POR DEFECTO (200)")
            self.wk_resultado = 200
        else:
            self.wk_resultado = result
            print(self.wk_resultado)

    def fin(self):
        pass

if __name__ == "__main__":
    program = OnSizeErrorProgram()
    program.run()
