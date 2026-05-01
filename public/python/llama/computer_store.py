# COMPUTER-STORE - Custom PC Builder
# Converted from COBOL to Python

def main():
    BUILD_FEE = 99.00

    print("--- CUSTOM PC BUILDER ---")
    cpu_choice = int(input("Select CPU: 1=i5($200), 2=i7($350), 3=i9($550): "))
    ram_choice = int(input("Select RAM: 1=16GB($80), 2=32GB($150): "))
    gpu_choice = int(input("Select GPU: 1=RTX4060($300), 2=RTX4080($900): "))

    if cpu_choice == 1:
        cpu_prc = 200.00
    elif cpu_choice == 2:
        cpu_prc = 350.00
    elif cpu_choice == 3:
        cpu_prc = 550.00
    else:
        cpu_prc = 200.00

    ram_prc = 150.00 if ram_choice == 2 else 80.00
    gpu_prc = 900.00 if gpu_choice == 2 else 300.00

    total_sys = cpu_prc + ram_prc + gpu_prc + BUILD_FEE

    print("")
    print("========================================")
    print("           PC BUILD QUOTE               ")
    print("========================================")
    print(f"Processor:   ${cpu_prc:,.2f}")
    print(f"Memory:      ${ram_prc:,.2f}")
    print(f"Graphics:    ${gpu_prc:,.2f}")
    print("----------------------------------------")
    print(f"Assembly Fee:${BUILD_FEE:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL SYSTEM COST: ${total_sys:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
