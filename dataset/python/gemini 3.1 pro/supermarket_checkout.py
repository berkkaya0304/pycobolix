def main():
    print("--- FRESH MART CHECKOUT ---")
    mem_card = input("Do you have a loyalty card? (Y/N): ").strip().upper() == 'Y'

    item_names = []
    pricing_types = []
    price_pers = []
    qty_or_weights = []
    sub_totals = []
    gross_total = 0.0

    for idx in range(3):
        item_name = input(f"Item {idx + 1} Name: ")
        pricing_type = input("Pricing (U=Unit, W=Weight/lbs): ").strip().upper()
        try:
            price_per = float(input("Price per U/W ($): "))
        except ValueError:
            price_per = 0.0
            
        if pricing_type == 'U':
            try:
                qty_or_weight = float(input("Quantity: "))
            except ValueError:
                qty_or_weight = 0.0
        else:
            try:
                qty_or_weight = float(input("Weight (lbs): "))
            except ValueError:
                qty_or_weight = 0.0

        sub_total = price_per * qty_or_weight
        gross_total += sub_total
        
        item_names.append(item_name)
        pricing_types.append(pricing_type)
        price_pers.append(price_per)
        qty_or_weights.append(qty_or_weight)
        sub_totals.append(sub_total)

    if mem_card:
        gross_total = gross_total * 0.95
        print("(5% Member Discount Applied)")

    tax_amount = gross_total * 0.02
    net_total = gross_total + tax_amount

    print("\n=======================================")
    print("          FRESH MART RECEIPT           ")
    print("=======================================")
    
    for idx in range(3):
        print(f"{item_names[idx].ljust(15)} x {qty_or_weights[idx]:4.2f}    ${sub_totals[idx]:6.2f}")
        
    print("---------------------------------------")
    print(f"Subtotal:        ${gross_total:6.2f}")
    print(f"Tax (2%):        ${tax_amount:6.2f}")
    print("---------------------------------------")
    print(f"TOTAL BALANCE:   ${net_total:6.2f}")
    print("=======================================")

if __name__ == "__main__":
    main()
