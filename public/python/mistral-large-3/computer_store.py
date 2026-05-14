def computer_store():
    class PcParts:
        def __init__(self):
            self.cpu_choice = 0
            self.ram_choice = 0
            self.gpu_choice = 0

    class Prices:
        def __init__(self):
            self.cpu_prc = 0.0
            self.ram_prc = 0.0
            self.gpu_prc = 0.0
            self.build_fee = 99.00
            self.total_sys = 0.0

    pc_parts = PcParts()
    prices = Prices()

    print("--- CUSTOM PC BUILDER ---")
    pc_parts.cpu_choice = int(input("Select CPU: 1=i5($200), 2=i7($350), 3=i9($550): "))
    pc_parts.ram_choice = int(input("Select RAM: 1=16GB($80), 2=32GB($150): "))
    pc_parts.gpu_choice = int(input("Select GPU: 1=RTX4060($300), 2=RTX4080($900): "))

    calc_system(pc_parts, prices)
    print_quote(prices)

def calc_system(pc_parts, prices):
    if pc_parts.cpu_choice == 1:
        prices.cpu_prc = 200.00
    elif pc_parts.cpu_choice == 2:
        prices.cpu_prc = 350.00
    elif pc_parts.cpu_choice == 3:
        prices.cpu_prc = 550.00
    else:
        prices.cpu_prc = 200.00

    if pc_parts.ram_choice == 1:
        prices.ram_prc = 80.00
    elif pc_parts.ram_choice == 2:
        prices.ram_prc = 150.00
    else:
        prices.ram_prc = 80.00

    if pc_parts.gpu_choice == 1:
        prices.gpu_prc = 300.00
    elif pc_parts.gpu_choice == 2:
        prices.gpu_prc = 900.00
    else:
        prices.gpu_prc = 300.00

    prices.total_sys = prices.cpu_prc + prices.ram_prc + prices.gpu_prc + prices.build_fee

def print_quote(prices):
    def format_currency(value):
        return f"${value:,.2f}"

    print()
    print("========================================")
    print("           PC BUILD QUOTE               ")
    print("========================================")
    print(f"Processor:   {format_currency(prices.cpu_prc)}")
    print(f"Memory:      {format_currency(prices.ram_prc)}")
    print(f"Graphics:    {format_currency(prices.gpu_prc)}")
    print("----------------------------------------")
    print(f"Assembly Fee:{format_currency(prices.build_fee)}")
    print("----------------------------------------")
    print(f"TOTAL SYSTEM COST: {format_currency(prices.total_sys)}")
    print("=======================================")

if __name__ == "__main__":
    computer_store()
