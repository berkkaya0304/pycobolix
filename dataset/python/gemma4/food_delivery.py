from decimal import Decimal, ROUND_HALF_UP

def calculate_food_delivery():
    print("--- QUICK DASH FOOD DELIVERY ---")
    
    try:
        order_num = input("Order Number: ")
        food_subtotal = Decimal(input("Restaurant Food Subtotal ($): "))
        miles_away = Decimal(input("Distance from Restaurant (Miles): "))
        tip_pct = Decimal(input("Tip Percentage for Driver (e.g. 15, 20): "))
    except (ValueError, ArithmeticError):
        print("Invalid input. Please enter numeric values.")
        return

    # Calculations
    delivery_fee = Decimal("2.00") + (miles_away * Decimal("1.50"))
    service_fee = food_subtotal * Decimal("0.15")
    tax_amt = food_subtotal * Decimal("0.08")
    driver_tip = food_subtotal * (tip_pct / Decimal("100"))
    
    grand_total = food_subtotal + delivery_fee + service_fee + tax_amt + driver_tip

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("           DELIVERY INVOICE             ")
    print("========================================")
    print(f"Order ID: #{order_num}")
    print("----------------------------------------")
    print(f"Food Subtotal:      {format_currency(food_subtotal)}")
    print(f"Delivery Distance:  {format_currency(delivery_fee)}")
    print(f"App Service Fee:    {format_currency(service_fee)}")
    print(f"Local Taxes:        {format_currency(tax_amt)}")
    print(f"Driver Tip:         {format_currency(driver_tip)}")
    print("----------------------------------------")
    print(f"TOTAL CHARGE:       {format_currency(grand_total)}")
    print("========================================")

if __name__ == "__main__":
    calculate_food_delivery()
