import decimal
from decimal import Decimal

def calculate_order():
    print("--- MARIO'S PIZZERIA ---")
    
    cust_name = input("Customer Name: ")
    pizza_size = input("Size (S=Small $10, M=Medium $14, L=Large $18): ").upper()
    
    try:
        crust_type = int(input("Crust (1=Thin, 2=Thick, 3=Stuffed +$3): "))
    except ValueError:
        crust_type = 0
        
    try:
        topping_qty = int(input("Number of Extra Toppings ($1.50 ea): "))
    except ValueError:
        topping_qty = 0

    # Base Price Calculation
    if pizza_size == 'S':
        base_price = Decimal('10.00')
    elif pizza_size == 'M':
        base_price = Decimal('14.00')
    elif pizza_size == 'L':
        base_price = Decimal('18.00')
    else:
        base_price = Decimal('10.00')
        print("Invalid Size, Default to Small.")

    # Crust Fee Calculation
    crust_fee = Decimal('3.00') if crust_type == 3 else Decimal('0.00')

    # Topping Fee Calculation
    topping_fee = Decimal(topping_qty) * Decimal('1.50')

    # Totals Calculation
    sub_total = base_price + crust_fee + topping_fee
    tax_amt = sub_total * Decimal('0.08')
    grand_total = sub_total + tax_amt

    print_receipt(cust_name, base_price, crust_fee, topping_fee, topping_qty, sub_total, tax_amt, grand_total)

def print_receipt(name, base, crust, toppings, qty, subtotal, tax, total):
    def fmt(val):
        return f"${val:,.2f}"

    print("\n========================================")
    print("          PIZZA ORDER RECEIPT           ")
    print("========================================")
    print(f"Order for: {name}")
    print("----------------------------------------")
    print(f"Base Pizza:       {fmt(base)}")
    
    if crust > 0:
        print(f"Stuffed Crust:    {fmt(crust)}")
    
    if toppings > 0:
        print(f"Toppings ({qty}):    {fmt(toppings)}")
        
    print("----------------------------------------")
    print(f"Subtotal:         {fmt(subtotal)}")
    print(f"Tax (8%):         {fmt(tax)}")
    print("========================================")
    print(f"TOTAL AMOUNT DUE: {fmt(total)}")
    print("========================================")

if __name__ == "__main__":
    calculate_order()
