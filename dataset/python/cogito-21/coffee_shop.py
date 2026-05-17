def main():
    print("--- MORNING BREW CAFE ---")
    customer_name = input("Customer Name: ")
    
    while True:
        drink_size = input("Size (S/M/L): ").upper()
        if drink_size in ['S', 'M', 'L']:
            break
        print("Invalid size. Please enter S, M, or L.")
    
    while True:
        try:
            milk_type = int(input("Milk (1=Whole, 2=Skim, 3=Oat, 4=Almond): "))
            if 1 <= milk_type <= 4:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            syrup_pumps = int(input("Syrup Pumps ($0.50 each): "))
            if syrup_pumps >= 0:
                break
            print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
    
    base_price, milk_surcharge, syrup_fee, drink_total = calculate_order(drink_size, milk_type, syrup_pumps)
    print_receipt(customer_name, drink_size, milk_type, syrup_pumps, base_price, milk_surcharge, syrup_fee, drink_total)

def calculate_order(drink_size, milk_type, syrup_pumps):
    if drink_size == 'S':
        base_price = 3.50
    elif drink_size == 'M':
        base_price = 4.50
    elif drink_size == 'L':
        base_price = 5.50
    else:
        base_price = 3.50
        print("Invalid size, defaulted to Small.")
    
    milk_surcharge = 1.00 if milk_type in [3, 4] else 0.00
    syrup_fee = syrup_pumps * 0.50
    drink_total = base_price + milk_surcharge + syrup_fee
    
    return base_price, milk_surcharge, syrup_fee, drink_total

def print_receipt(customer_name, drink_size, milk_type, syrup_pumps, base_price, milk_surcharge, syrup_fee, drink_total):
    milk_names = {
        1: "Whole Milk",
        2: "Skim Milk",
        3: "Oat Milk",
        4: "Almond Milk"
    }
    
    print("\n==================================")
    print("         CAFE RECEIPT             ")
    print("==================================")
    print(f"Order for: {customer_name}")
    print("----------------------------------")
    print(f"Drink Base Price:  ${base_price:.2f}")
    
    if milk_surcharge > 0:
        print(f"Premium Milk:      ${milk_surcharge:.2f}")
    
    if syrup_fee > 0:
        print(f"Syrup ({syrup_pumps}) pumps:   ${syrup_fee:.2f}")
    
    print("----------------------------------")
    print(f"TOTAL AMOUNT DUE:  ${drink_total:.2f}")
    print("==================================")

if __name__ == "__main__":
    main()
