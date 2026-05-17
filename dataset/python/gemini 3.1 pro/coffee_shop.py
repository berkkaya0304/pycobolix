def main():
    print("--- MORNING BREW CAFE ---")
    customer_name = input("Customer Name: ")
    drink_size = input("Size (S/M/L): ").strip().upper()
    milk_type = input("Milk (1=Whole, 2=Skim, 3=Oat, 4=Almond): ").strip()
    try:
        syrup_pumps = int(input("Syrup Pumps ($0.50 each): "))
    except ValueError:
        syrup_pumps = 0

    if drink_size == 'S':
        base_price = 3.50
    elif drink_size == 'M':
        base_price = 4.50
    elif drink_size == 'L':
        base_price = 5.50
    else:
        print("Invalid size, defaulted to Small.")
        base_price = 3.50

    milk_surcharge = 1.00 if milk_type in ('3', '4') else 0.0
    syrup_fee = syrup_pumps * 0.50
    drink_total = base_price + milk_surcharge + syrup_fee

    print("\n==================================")
    print("         CAFE RECEIPT             ")
    print("==================================")
    print(f"Order for: {customer_name}")
    print("----------------------------------")
    print(f"Drink Base Price:  ${base_price:6.2f}")
    
    if milk_surcharge > 0:
        print(f"Premium Milk:      ${milk_surcharge:6.2f}")
        
    if syrup_fee > 0:
        print(f"Syrup ({syrup_pumps}) pumps:   ${syrup_fee:6.2f}")
        
    print("----------------------------------")
    print(f"TOTAL AMOUNT DUE:  ${drink_total:6.2f}")
    print("==================================")

if __name__ == "__main__":
    main()
