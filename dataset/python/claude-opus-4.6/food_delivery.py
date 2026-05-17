"""
Quick Dash Food Delivery
Converted from COBOL (food_delivery.cbl) to Python
"""


def main():
    print("--- QUICK DASH FOOD DELIVERY ---")
    order_num = input("Order Number: ")
    food_subtotal = float(input("Restaurant Food Subtotal ($): "))
    miles_away = float(input("Distance from Restaurant (Miles): "))
    add_tip_pct = int(input("Tip Percentage for Driver (e.g. 15, 20): "))

    delivery_fee = 2.00 + (miles_away * 1.50)
    service_fee = food_subtotal * 0.15
    tax_amt = food_subtotal * 0.08
    driver_tip = food_subtotal * (add_tip_pct / 100)
    grand_tot = food_subtotal + delivery_fee + service_fee + tax_amt + driver_tip

    print()
    print("========================================")
    print("           DELIVERY INVOICE             ")
    print("========================================")
    print(f"Order ID: #{order_num}")
    print("----------------------------------------")
    print(f"Food Subtotal:      ${food_subtotal:>9,.2f}")
    print(f"Delivery Distance:  ${delivery_fee:>9,.2f}")
    print(f"App Service Fee:    ${service_fee:>9,.2f}")
    print(f"Local Taxes:        ${tax_amt:>9,.2f}")
    print(f"Driver Tip:         ${driver_tip:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL CHARGE:       ${grand_tot:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
