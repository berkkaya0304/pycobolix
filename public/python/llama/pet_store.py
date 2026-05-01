# PET-STORE - Happy Paws Pet Emporium
# Converted from COBOL to Python

def main():
    FOOD_PRICE = 45.00
    TOY_PRICE = 12.50
    GROOM_PRICE = 18.00

    print("--- HAPPY PAWS PET EMPORIUM ---")
    food_bags = int(input("Dog/Cat Food Bags ($45 ea): "))
    toy_qty = int(input("Pet Toys ($12.50 ea): "))
    groom_items = int(input("Grooming Supplies ($18 ea): "))
    vip_member = input("VIP Rewards Member (15% off)? (Y/N): ").strip().upper()

    sub_tot = (food_bags * FOOD_PRICE) + (toy_qty * TOY_PRICE) + (groom_items * GROOM_PRICE)
    vip_disc = sub_tot * 0.15 if vip_member == 'Y' else 0.0
    tax_amt = (sub_tot - vip_disc) * 0.08
    g_total = sub_tot - vip_disc + tax_amt

    print("")
    print("========================================")
    print("            PET STORE RECEIPT           ")
    print("========================================")
    if food_bags > 0:
        print(f"{food_bags}x Pet Food:         ${food_bags * FOOD_PRICE:,.2f}")
    if toy_qty > 0:
        print(f"{toy_qty}x Toys:             ${toy_qty * TOY_PRICE:,.2f}")
    if groom_items > 0:
        print(f"{groom_items}x Grooming Items:   ${groom_items * GROOM_PRICE:,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:            ${sub_tot:,.2f}")
    if vip_member == 'Y':
        print(f"VIP Discount (15%): -${vip_disc:,.2f}")
    print(f"Sales Tax (8%):      ${tax_amt:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${g_total:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
