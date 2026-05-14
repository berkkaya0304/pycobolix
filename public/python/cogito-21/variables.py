class Variables:
    def __init__(self):
        self.struct_headers = "lp|    number|   decimal|  currency"
        self.var_line = "-" * 80
        
        self.var_lp = 0
        self.var_number = 0
        self.var_decimal = -317.21
        self.var_currency = 317.21
    
    def format_row(self):
        lp = f"{self.var_lp:02d}"
        number = f"{self.var_number:10d}"
        decimal = f"{self.var_decimal:+10.2f}"
        currency = f"${self.var_currency:9.2f}"
        return f"{lp}|{number}|{decimal}|{currency}"
    
    def display(self):
        print(self.struct_headers)
        print(self.var_line)
        print(self.format_row())

def main():
    prog = Variables()
    prog.var_lp = 1
    prog.var_number = 3721
    prog.display()

if __name__ == "__main__":
    main()
