class CompConversionTest:
    def __init__(self):
        self.ws_comp_val = 0
        self.ws_disp_val = 0
        self.ws_dyn_disp_val = "   "
        self.ws_input = 0

    def main_procedure(self):
        self.ws_comp_val = 12
        self.ws_comp_val *= 2
        print(f"COMP: {self.ws_comp_val:03d}")

        self.ws_disp_val = self.ws_comp_val
        print(f"DISP:{self.ws_disp_val:03d}")

        self.ws_dyn_disp_val = f"{self.ws_comp_val:3d}"
        print(f"DYNA: {self.ws_dyn_disp_val}")

        try:
            self.ws_input = int(input("INPUT: "))
        except ValueError:
            self.ws_input = 0

        print(f"INPUT: {self.ws_input:03d}")

        self.ws_comp_val = self.ws_input
        print(f"COMP: {self.ws_comp_val:03d}")

if __name__ == "__main__":
    program = CompConversionTest()
    program.main_procedure()
