def supermarket_checkout():
    items = []
    for _ in range(3):
        item = {
            'name': '',
            'pricing_type': '',
            'price_per': 0.0,
            'qty_or_weight': 0.0,
            'sub_total': 0.0
        }
        items.append(item)

    billing = {
        'gross_total': 0.0,
        'tax_amount': 0.0,
        'net_total': 0.0
    }

    print("--- FRESH MART CHECKOUT ---")
    mem_card = input("Do you have a loyalty card? (Y/N): ").strip().upper()

    for idx in range(3):
        print(f"Item {idx + 1} Name: ")
        items[idx]['name'] = input().strip()

        while True:
            print("Pricing (U=Unit, W=Weight/lbs): ")
            items[idx]['pricing_type'] = input().strip().upper()
            if items[idx]['pricing_type'] in ('U', 'W'):
                break

        print("Price per U/W ($): ")
        items[idx]['price_per'] = float(input())

        if items[idx]['pricing_type'] == 'U':
            print("Quantity: ")
        else:
            print("Weight (lbs): ")
        items[idx]['qty_or_weight'] = float(input())

        items[idx]['sub_total'] = items[idx]['price_per'] * items[idx]['qty_or_weight']
        billing['gross_total'] += items[idx]['sub_total']

    process_bill(billing, mem_card)
    print_receipt(items, billing)

def process_bill(billing, mem_card):
    if mem_card == 'Y':
        billing['gross_total'] *= 0.95
        print("(5% Member Discount Applied)")

    billing['tax_amount'] = billing['gross_total'] * 0.02
    billing['net_total'] = billing['gross_total'] + billing['tax_amount']

def print_receipt(items, billing):
    print("\n=======================================")
    print("          FRESH MART RECEIPT           ")
    print("=======================================")

    for item in items:
        print(f"{item['name']} x {item['qty_or_weight']:.2f}    ${item['sub_total']:.2f}")

    print("---------------------------------------")
    print(f"Subtotal:        ${billing['gross_total']:.2f}")
    print(f"Tax (2%):        ${billing['tax_amount']:.2f}")
    print("---------------------------------------")
    print(f"TOTAL BALANCE:   ${billing['net_total']:.2f}")
    print("=======================================")

if __name__ == "__main__":
    supermarket_checkout()
