def coffee_shop():
    print("--- MORNING BREW CAFE ---")

    customer_name = input("Customer Name: ").strip()
    drink_size = input("Size (S/M/L): ").strip().upper()
    milk_type = int(input("Milk (1=Whole, 2=Skim, 3=Oat, 4=Almond): ").strip())
    syrup_pumps = int(input("Syrup Pumps ($0.50 each): ").strip())

    base_price, size_message = calculate_base_price(drink_size)
    milk_surcharge = calculate_milk_surcharge(milk_type)
    syrup_fee = syrup_pumps * 0.50
    drink_total = base_price + milk_surcharge + syrup_fee

    print_receipt(customer_name, base_price, milk_surcharge, syrup_pumps, syrup_fee, drink_total, size_message)

def calculate_base_price(drink_size):
    size_message = None
    if drink_size == 'S':
        base_price = 3.50
    elif drink_size == 'M':
        base_price = 4.50
    elif drink_size == 'L':
        base_price = 5.50
    else:
        base_price = 3.50
        size_message = "Invalid size, defaulted to Small."
    return base_price, size_message

def calculate_milk_surcharge(milk_type):
    if milk_type in (3, 4):
        return 1.00
    return 0.00

def format_currency(amount):
    return f"${amount:,.2f}"

def print_receipt(customer_name, base_price, milk_surcharge, syrup_pumps, syrup_fee, drink_total, size_message):
    print()
    print("=" * 34)
    print("         CAFE RECEIPT             ")
    print("=" * 34)
    print(f"Order for: {customer_name}")
    print("-" * 34)
    print(f"Drink Base Price:  {format_currency(base_price)}")
    if size_message:
        print(size_message)
    if milk_surcharge > 0:
        print(f"Premium Milk:      {format_currency(milk_surcharge)}")
    if syrup_fee > 0:
        print(f"Syrup ({syrup_pumps}) pumps:   {format_currency(syrup_fee)}")
    print("-" * 34)
    print(f"TOTAL AMOUNT DUE:  {format_currency(drink_total)}")
    print("=" * 34)

if __name__ == "__main__":
    coffee_shop()
