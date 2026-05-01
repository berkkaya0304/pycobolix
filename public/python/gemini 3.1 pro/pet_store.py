def main():
    print("--- HAPPY PAWS PET EMPORIUM ---")
    try:
        food_bags = int(input("Dog/Cat Food Bags ($45 ea): "))
    except ValueError:
        food_bags = 0
    try:
        toy_qty = int(input("Pet Toys ($12.50 ea): "))
    except ValueError:
        toy_qty = 0
    try:
        groom_items = int(input("Grooming Supplies ($18 ea): "))
    except ValueError:
        groom_items = 0
        
    vip_member = input("VIP Rewards Member (15% off)? (Y/N): ").strip().upper() == 'Y'

    food_price = 45.00
    toy_price = 12.50
    groom_price = 18.00

    sub_tot = (food_bags * food_price) + (toy_qty * toy_price) + (groom_items * groom_price)

    vip_disc = 0.0
    if vip_member:
        vip_disc = sub_tot * 0.15

    tax_amt = (sub_tot - vip_disc) * 0.08
    g_total = sub_tot - vip_disc + tax_amt

    print("\n========================================")
    print("            PET STORE RECEIPT           ")
    print("========================================")
    
    if food_bags > 0:
        disp = food_bags * food_price
        print(f"{food_bags:02d}x Pet Food:         ${disp:6.2f}")
    if toy_qty > 0:
        disp = toy_qty * toy_price
        print(f"{toy_qty:02d}x Toys:             ${disp:6.2f}")
    if groom_items > 0:
        disp = groom_items * groom_price
        print(f"{groom_items:02d}x Grooming Items:   ${disp:6.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:            ${sub_tot:6.2f}")
    if vip_member:
        print(f"VIP Discount (15%): -${vip_disc:6.2f}")
    print(f"Sales Tax (8%):      ${tax_amt:6.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${g_total:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
