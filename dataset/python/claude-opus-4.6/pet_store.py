"""
Happy Paws Pet Emporium - Pet Store
Converted from COBOL (pet_store.cbl) to Python
"""


def main():
    food_price = 45.00
    toy_price = 12.50
    groom_price = 18.00

    print("--- HAPPY PAWS PET EMPORIUM ---")
    food_bags = int(input("Dog/Cat Food Bags ($45 ea): "))
    toy_qty = int(input("Pet Toys ($12.50 ea): "))
    groom_items = int(input("Grooming Supplies ($18 ea): "))
    vip_member = input("VIP Rewards Member (15% off)? (Y/N): ").strip().upper()

    sub_tot = (food_bags * food_price) + (toy_qty * toy_price) + (groom_items * groom_price)
    vip_disc = sub_tot * 0.15 if vip_member == "Y" else 0.0
    tax_amt = (sub_tot - vip_disc) * 0.08
    g_total = sub_tot - vip_disc + tax_amt

    print()
    print("========================================")
    print("            PET STORE RECEIPT           ")
    print("========================================")
    if food_bags > 0:
        print(f"{food_bags}x Pet Food:         ${food_bags * food_price:>9,.2f}")
    if toy_qty > 0:
        print(f"{toy_qty}x Toys:             ${toy_qty * toy_price:>9,.2f}")
    if groom_items > 0:
        print(f"{groom_items}x Grooming Items:   ${groom_items * groom_price:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:            ${sub_tot:>9,.2f}")
    if vip_member == "Y":
        print(f"VIP Discount (15%): -${vip_disc:>8,.2f}")
    print(f"Sales Tax (8%):      ${tax_amt:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${g_total:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
