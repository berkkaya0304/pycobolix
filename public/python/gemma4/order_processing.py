from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("*** ONLINE ORDER SYSTEM ***")
    
    order_number = input("Order Number: ")
    cust_name = input("Customer Name: ")
    ord_date = input("Date (YYYY-MM-DD): ")

    items = []
    grand_subtotal = Decimal('0.00')

    for i in range(1, 4):
        print(f"--- Enter Item {i} ---")
        prd_name = input("Product Name: ")
        try:
            prd_qty = int(input("Quantity: "))
            prd_price = Decimal(input("Unit Price: "))
        except ValueError:
            print("Invalid input. Using 0.")
            prd_qty = 0
            prd_price = Decimal('0.00')

        prd_subtotal = prd_qty * prd_price
        grand_subtotal += prd_subtotal
        
        items.append({
            'name': prd_name,
            'qty': prd_qty,
            'price': prd_price,
            'subtotal': prd_subtotal
        })

    # Calculate Totals
    tax_amt = (grand_subtotal * Decimal('0.08')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    shipping = Decimal('15.00')
    if grand_subtotal > 500:
        shipping = Decimal('0.00')
    
    final_total = grand_subtotal + tax_amt + shipping

    # Print Invoice
    print("\n=============================================")
    print(f"  INVOICE #{order_number}    DATE: {ord_date}")
    print(f"  BILL TO: {cust_name}")
    print("---------------------------------------------")
    print(f"{'ITEM':<15} {'QTY':<11} {'PRICE':<11} {'SUBTOTAL':<11}")
    print("---------------------------------------------")

    for item in items:
        print(f"{item['name']:<15} {item['qty']:<11} {item['price']:<11.2f} {format_currency(item['subtotal']):<11}")

    print("---------------------------------------------")
    print(f"  Goods Total:   {format_currency(grand_subtotal)}")
    print(f"  Tax (8%):      {format_currency(tax_amt)}")
    print(f"  Shipping:      {format_currency(shipping)}")
    print("=============================================")
    print(f"  FINAL PAYABLE: {format_currency(final_total)}")
    print("=============================================")

if __name__ == "__main__":
    main()
