from decimal import Decimal, ROUND_HALF_UP

def format_currency(value):
    return f"${value:,.2f}"

def main():
    items = []
    gross_total = Decimal('0.00')
    
    print("--- FRESH MART CHECKOUT ---")
    mem_card = input("Do you have a loyalty card? (Y/N): ").strip().upper()

    for i in range(1, 4):
        print(f"\nItem {i}:")
        name = input("Item Name: ")
        pricing_type = input("Pricing (U=Unit, W=Weight/lbs): ").strip().upper()
        
        try:
            price_per = Decimal(input("Price per U/W ($): "))
            if pricing_type == 'U':
                qty_weight = Decimal(input("Quantity: "))
            else:
                qty_weight = Decimal(input("Weight (lbs): "))
        except Exception:
            print("Invalid numeric input. Defaulting to 0.")
            price_per = Decimal('0.00')
            qty_weight = Decimal('0.00')

        sub_total = (price_per * qty_weight).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        items.append({
            'name': name,
            'qty': qty_weight,
            'sub_total': sub_total
        })
        
        gross_total += sub_total

    # Process Bill
    if mem_card == 'Y':
        gross_total = (gross_total * Decimal('0.95')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print("\n(5% Member Discount Applied)")

    tax_amount = (gross_total * Decimal('0.02')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    net_total = gross_total + tax_amount

    # Print Receipt
    print("\n=======================================")
    print("          FRESH MART RECEIPT           ")
    print("=======================================")
    
    for item in items:
        print(f"{item['name']:<15} x {item['qty']:<8} {format_currency(item['sub_total']):>10}")
    
    print("---------------------------------------")
    print(f"Subtotal:        {format_currency(gross_total):>15}")
    print(f"Tax (2%):        {format_currency(tax_amount):>15}")
    print("---------------------------------------")
    print(f"TOTAL BALANCE:   {format_currency(net_total):>15}")
    print("=======================================")

if __name__ == "__main__":
    main()
