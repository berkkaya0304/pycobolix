def main():
    print("--- CUSTOM PC BUILDER ---")
    
    cpu_choice = int(input("Select CPU: 1=i5($200), 2=i7($350), 3=i9($550): "))
    ram_choice = int(input("Select RAM: 1=16GB($80), 2=32GB($150): "))
    gpu_choice = int(input("Select GPU: 1=RTX4060($300), 2=RTX4080($900): "))
    
    cpu_prices = {1: 200.00, 2: 350.00, 3: 550.00}
    ram_prices = {1: 80.00, 2: 150.00}
    gpu_prices = {1: 300.00, 2: 900.00}
    
    cpu_price = cpu_prices.get(cpu_choice, 200.00)
    ram_price = ram_prices.get(ram_choice, 80.00)
    gpu_price = gpu_prices.get(gpu_choice, 300.00)
    build_fee = 99.00
    total_sys = cpu_price + ram_price + gpu_price + build_fee
    
    print("\n" + "=" * 40)
    print("           PC BUILD QUOTE               ")
    print("=" * 40)
    print(f"Processor:   ${cpu_price:,.2f}")
    print(f"Memory:      ${ram_price:,.2f}")
    print(f"Graphics:    ${gpu_price:,.2f}")
    print("-" * 40)
    print(f"Assembly Fee:${build_fee:,.2f}")
    print("-" * 40)
    print(f"TOTAL SYSTEM COST: ${total_sys:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
