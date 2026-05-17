"""
Sunrise Bakery POS
Converted from COBOL (bakery_shop.cbl) to Python
"""


def main():
    cake_prc = 25.00
    bread_prc = 4.50
    pastry_prc = 3.00

    print("--- SUNRISE BAKERY POS ---")
    cust_name = input("Customer Name: ")
    cake_qty = int(input("Whole Cakes ($25.00 ea): "))
    bread_qty = int(input("Loaves of Bread ($4.50 ea): "))
    pastry_qty = int(input("Assorted Pastries ($3.00 ea): "))

    cake_tot = cake_qty * cake_prc
    bread_tot = bread_qty * bread_prc
    pastry_tot = pastry_qty * pastry_prc
    sub_total = cake_tot + bread_tot + pastry_tot

    discount = sub_total * 0.10 if sub_total >= 50.00 else 0.0
    final_tot = sub_total - discount

    print()
    print("=========================================")
    print("          BAKERY ORDER RECEIPT           ")
    print("=========================================")
    print(f"Customer: {cust_name}")
    print("-----------------------------------------")
    if cake_qty > 0:
        print(f"{cake_qty} x Cakes:         ${cake_tot:>9,.2f}")
    if bread_qty > 0:
        print(f"{bread_qty} x Bread Loaves:  ${bread_tot:>9,.2f}")
    if pastry_qty > 0:
        print(f"{pastry_qty} x Pastries:      ${pastry_tot:>9,.2f}")
    print("-----------------------------------------")
    print(f"Subtotal:         ${sub_total:>9,.2f}")
    if discount > 0:
        print(f"Bulk Discount:   -${discount:>9,.2f}")
    print("-----------------------------------------")
    print(f"TOTAL DUE:        ${final_tot:>9,.2f}")
    print("=========================================")


if __name__ == "__main__":
    main()
