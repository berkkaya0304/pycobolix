# ORDER-PROCESSING - Online Order System
# Converted from COBOL to Python

def main():
    print("*** ONLINE ORDER SYSTEM ***")
    ord_number = input("Order Number: ")
    cust_name = input("Customer Name: ")
    ord_date = input("Date (YYYY-MM-DD): ")

    items = []
    grand_subtot = 0.0
    for i in range(1, 4):
        print(f"--- Enter Item {i} ---")
        prd_name = input("Product Name: ")
        prd_qty = int(input("Quantity: "))
        prd_price = float(input("Unit Price: "))
        prd_subtot = prd_qty * prd_price
        grand_subtot += prd_subtot
        items.append((prd_name, prd_qty, prd_price, prd_subtot))

    tax_amt = grand_subtot * 0.08
    shipping = 0.0 if grand_subtot > 500 else 15.00
    final_total = grand_subtot + tax_amt + shipping

    print("")
    print("=============================================")
    print(f"  INVOICE #{ord_number}    DATE: {ord_date}")
    print(f"  BILL TO: {cust_name}")
    print("---------------------------------------------")
    print("ITEM            QTY         PRICE       SUBTOTAL")
    print("---------------------------------------------")
    for name, qty, price, subtot in items:
        print(f"{name:<15} {qty:<11} {price:<11.2f} ${subtot:,.2f}")
    print("---------------------------------------------")
    print(f"  Goods Total:   ${grand_subtot:,.2f}")
    print(f"  Tax (8%):      ${tax_amt:,.2f}")
    print(f"  Shipping:      ${shipping:,.2f}")
    print("=============================================")
    print(f"  FINAL PAYABLE: ${final_total:,.2f}")
    print("=============================================")

if __name__ == "__main__":
    main()
