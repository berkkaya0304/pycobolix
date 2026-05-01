def main():
    print("*** ONLINE ORDER SYSTEM ***")
    try:
        ord_number = int(input("Order Number: "))
    except ValueError:
        ord_number = 0
    cust_name = input("Customer Name: ")
    ord_date = input("Date (YYYY-MM-DD): ")

    prd_names = []
    prd_qtys = []
    prd_prices = []
    prd_subtots = []
    grand_subtot = 0.0

    for i in range(1, 4):
        print(f"--- Enter Item {i} ---")
        prd_name = input("Product Name: ")
        try:
            prd_qty = int(input("Quantity: "))
        except ValueError:
            prd_qty = 0
        try:
            prd_price = float(input("Unit Price: "))
        except ValueError:
            prd_price = 0.0
            
        prd_subtot = prd_qty * prd_price
        
        prd_names.append(prd_name)
        prd_qtys.append(prd_qty)
        prd_prices.append(prd_price)
        prd_subtots.append(prd_subtot)
        
        grand_subtot += prd_subtot

    tax_amt = grand_subtot * 0.08
    shipping = 0.0 if grand_subtot > 500 else 15.00
    final_total = grand_subtot + tax_amt + shipping

    print("\n=============================================")
    print(f"  INVOICE #{ord_number:06d}    DATE: {ord_date}")
    print(f"  BILL TO: {cust_name}")
    print("---------------------------------------------")
    print("ITEM            QTY         PRICE       SUBTOTAL")
    print("---------------------------------------------")
    
    for i in range(3):
        n = prd_names[i].ljust(15)[:15]
        q = f"{prd_qtys[i]:03d}".ljust(11)
        p = f"{prd_prices[i]:07.2f}".ljust(11)
        s = f"${prd_subtots[i]:10.2f}"
        print(f"{n} {q} {p} {s}")
        
    print("---------------------------------------------")
    print(f"  Goods Total:   ${grand_subtot:10.2f}")
    print(f"  Tax (8%):      ${tax_amt:10.2f}")
    print(f"  Shipping:      ${shipping:10.2f}")
    print("=============================================")
    print(f"  FINAL PAYABLE: ${final_total:11.2f}")
    print("=============================================")

if __name__ == "__main__":
    main()
