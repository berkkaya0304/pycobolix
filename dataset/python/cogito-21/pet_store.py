def main():
    print("--- HAPPY PAWS PET EMPORIUM ---")
    
    food_bags = int(input("Dog/Cat Food Bags ($45 ea): "))
    toy_qty = int(input("Pet Toys ($12.50 ea): "))
    groom_items = int(input("Grooming Supplies ($18 ea): "))
    vip_member = input("VIP Rewards Member (15% off)? (Y/N): ").strip().upper()
    
    food_price = 45.00
    toy_price = 12.50
    groom_price = 18.00
    
    subtotal = (food_bags * food_price) + (toy_qty * toy_price) + (groom_items * groom_price)
    
    vip_disc = 0.0
    if vip_member == 'Y':
        vip_disc = subtotal * 0.15
    
    tax_amt = (subtotal - vip_disc) * 0.08
    grand_total = subtotal - vip_disc + tax_amt
    
    print("\n" + "=" * 40)
    print("            PET STORE RECEIPT           ")
    print("=" * 40)
    
    if food_bags > 0:
        print(f"{food_bags}x Pet Food:         ${food_bags * food_price:7.2f}")
    if toy_qty > 0:
        print(f"{toy_qty}x Toys:             ${toy_qty * toy_price:7.2f}")
    if groom_items > 0:
        print(f"{groom_items}x Grooming Items:   ${groom_items * groom_price:7.2f}")
    
    print("-" * 40)
    print(f"Subtotal:            ${subtotal:7.2f}")
    
    if vip_member == 'Y':
        print(f"VIP Discount (15%): -${vip_disc:7.2f}")
    
    print(f"Sales Tax (8%):      ${tax_amt:7.2f}")
    print("-" * 40)
    print(f"TOTAL BALANCE:       ${grand_total:7.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
