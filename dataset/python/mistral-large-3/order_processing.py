def order_processing():
    print("*** ONLINE ORDER SYSTEM ***")

    order_number = input("Order Number: ").strip()
    cust_name = input("Customer Name: ").strip()
    ord_date = input("Date (YYYY-MM-DD): ").strip()

    items = []
    grand_subtot = 0.0

    for i in range(3):
        print(f"--- Enter Item {i + 1} ---")
        prd_name = input("Product Name: ").strip()
        prd_qty = int(input("Quantity: ").strip())
        prd_price = float(input("Unit Price: ").strip())

        prd_subtot = prd_qty * prd_price
        grand_subtot += prd_subtot

        items.append({
            "name": prd_name,
            "qty": prd_qty,
            "price": prd_price,
            "subtot": prd_subtot
        })

    tax_amt = grand_subtot * 0.08
    shipping = 0.0 if grand_subtot > 500 else 15.00
    final_total = grand_subtot + tax_amt + shipping

    print("\n=============================================")
    print(f"  INVOICE #{order_number}    DATE: {ord_date}")
    print(f"  BILL TO: {cust_name}")
    print("---------------------------------------------")
    print("ITEM            QTY         PRICE       SUBTOTAL")
    print("---------------------------------------------")

    for item in items:
        print(f"{item['name'].ljust(15)} {str(item['qty']).rjust(3)}          "
              f"{item['price']:.2f}     ${item['subtot']:,.2f}")

    print("---------------------------------------------")
    print(f"  Goods Total:   ${grand_subtot:,.2f}")
    print(f"  Tax (8%):      ${tax_amt:,.2f}")
    print(f"  Shipping:      ${shipping:,.2f}")
    print("=============================================")
    print(f"  FINAL PAYABLE: ${final_total:,.2f}")
    print("=============================================")

if __name__ == "__main__":
    order_processing()
