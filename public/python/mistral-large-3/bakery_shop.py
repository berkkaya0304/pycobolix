def bakery_shop():
    # Initialize order quantities
    cust_name = ""
    cake_qty = 0
    bread_qty = 0
    pastry_qty = 0

    # Item prices
    cake_prc = 25.00
    bread_prc = 4.50
    pastry_prc = 3.00

    # Calculations
    cake_tot = 0.0
    bread_tot = 0.0
    pastry_tot = 0.0
    sub_total = 0.0
    discount = 0.0
    final_tot = 0.0

    def format_currency(amount):
        return f"${amount:,.2f}"

    def process_order():
        nonlocal cake_tot, bread_tot, pastry_tot, sub_total, discount, final_tot
        cake_tot = cake_qty * cake_prc
        bread_tot = bread_qty * bread_prc
        pastry_tot = pastry_qty * pastry_prc
        sub_total = cake_tot + bread_tot + pastry_tot

        if sub_total >= 50.00:
            discount = sub_total * 0.10

        final_tot = sub_total - discount

    def print_bill():
        print("\n=========================================")
        print("          BAKERY ORDER RECEIPT           ")
        print("=========================================")
        print(f"Customer: {cust_name}")
        print("-----------------------------------------")

        if cake_qty > 0:
            print(f"{cake_qty} x Cakes:         {format_currency(cake_tot)}")
        if bread_qty > 0:
            print(f"{bread_qty} x Bread Loaves:  {format_currency(bread_tot)}")
        if pastry_qty > 0:
            print(f"{pastry_qty} x Pastries:      {format_currency(pastry_tot)}")

        print("-----------------------------------------")
        print(f"Subtotal:         {format_currency(sub_total)}")

        if discount > 0:
            print(f"Bulk Discount:   -{format_currency(discount)}")

        print("-----------------------------------------")
        print(f"TOTAL DUE:        {format_currency(final_tot)}")
        print("=========================================")

    # Main program flow
    print("--- SUNRISE BAKERY POS ---")
    cust_name = input("Customer Name: ")
    cake_qty = int(input("Whole Cakes ($25.00 ea): "))
    bread_qty = int(input("Loaves of Bread ($4.50 ea): "))
    pastry_qty = int(input("Assorted Pastries ($3.00 ea): "))

    process_order()
    print_bill()

if __name__ == "__main__":
    bakery_shop()
