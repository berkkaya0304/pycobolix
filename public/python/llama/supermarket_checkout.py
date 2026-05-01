# SUPERMARKET - Fresh Mart Checkout
# Converted from COBOL to Python

def main():
    print("--- FRESH MART CHECKOUT ---")
    mem_card = input("Do you have a loyalty card? (Y/N): ").strip().upper()

    items = []
    gross_total = 0.0
    for i in range(1, 4):
        item_name = input(f"Item {i} Name: ")
        pricing_type = input("Pricing (U=Unit, W=Weight/lbs): ").strip().upper()
        price_per = float(input("Price per U/W ($): "))
        if pricing_type == 'U':
            qty_or_weight = float(input("Quantity: "))
        else:
            qty_or_weight = float(input("Weight (lbs): "))
        sub_total = price_per * qty_or_weight
        gross_total += sub_total
        items.append((item_name, qty_or_weight, sub_total))

    if mem_card == 'Y':
        gross_total = gross_total * 0.95
        print("(5% Member Discount Applied)")

    tax_amount = gross_total * 0.02
    net_total = gross_total + tax_amount

    print("")
    print("=======================================")
    print("          FRESH MART RECEIPT           ")
    print("=======================================")
    for name, qty, subtot in items:
        print(f"{name} x {qty}    ${subtot:,.2f}")
    print("---------------------------------------")
    print(f"Subtotal:        ${gross_total:,.2f}")
    print(f"Tax (2%):        ${tax_amount:,.2f}")
    print("---------------------------------------")
    print(f"TOTAL BALANCE:   ${net_total:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
