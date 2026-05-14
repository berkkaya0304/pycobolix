"""
Custom PC Builder - Computer Store
Converted from COBOL (computer_store.cbl) to Python
"""


def main():
    print("--- CUSTOM PC BUILDER ---")
    cpu_choice = int(input("Select CPU: 1=i5($200), 2=i7($350), 3=i9($550): "))
    ram_choice = int(input("Select RAM: 1=16GB($80), 2=32GB($150): "))
    gpu_choice = int(input("Select GPU: 1=RTX4060($300), 2=RTX4080($900): "))

    # CPU pricing
    if cpu_choice == 1:
        cpu_prc = 200.00
    elif cpu_choice == 2:
        cpu_prc = 350.00
    elif cpu_choice == 3:
        cpu_prc = 550.00
    else:
        cpu_prc = 200.00

    # RAM pricing
    if ram_choice == 1:
        ram_prc = 80.00
    elif ram_choice == 2:
        ram_prc = 150.00
    else:
        ram_prc = 80.00

    # GPU pricing
    if gpu_choice == 1:
        gpu_prc = 300.00
    elif gpu_choice == 2:
        gpu_prc = 900.00
    else:
        gpu_prc = 300.00

    build_fee = 99.00
    total_sys = cpu_prc + ram_prc + gpu_prc + build_fee

    print()
    print("========================================")
    print("           PC BUILD QUOTE               ")
    print("========================================")
    print(f"Processor:   ${cpu_prc:>9,.2f}")
    print(f"Memory:      ${ram_prc:>9,.2f}")
    print(f"Graphics:    ${gpu_prc:>9,.2f}")
    print("----------------------------------------")
    print(f"Assembly Fee:${build_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SYSTEM COST: ${total_sys:>9,.2f}")
    print("=======================================")


if __name__ == "__main__":
    main()
