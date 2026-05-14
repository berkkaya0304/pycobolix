"""
Online Order System - Order Processing
Converted from COBOL (order_processing.cbl) to Python
"""


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

    print()
    print("=============================================")
    print(f"  INVOICE #{ord_number}    DATE: {ord_date}")
    print(f"  BILL TO: {cust_name}")
    print("---------------------------------------------")
    print(f"{'ITEM':<16}{'QTY':>4}{'PRICE':>12}{'SUBTOTAL':>14}")
    print("---------------------------------------------")

    for name, qty, price, subtot in items:
        print(f"{name:<16}{qty:>4}{price:>12.2f}{subtot:>14.2f}")

    print("---------------------------------------------")
    print(f"  Goods Total:   ${grand_subtot:>12,.2f}")
    print(f"  Tax (8%):      ${tax_amt:>12,.2f}")
    print(f"  Shipping:      ${shipping:>12,.2f}")
    print("=============================================")
    print(f"  FINAL PAYABLE: ${final_total:>12,.2f}")
    print("=============================================")


if __name__ == "__main__":
    main()
