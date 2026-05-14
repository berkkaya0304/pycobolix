def calculate_fees(tier_level, extra_snacks, extra_gear):
    # Base Price Logic
    if tier_level == 1:
        base_price = 20.00
    elif tier_level == 2:
        base_price = 40.00
    elif tier_level == 3:
        base_price = 75.00
    else:
        base_price = 20.00
        print("Invalid tier, defaulted to Basic.")

    # Add-on Logic
    addon_price = 0.00
    if extra_snacks.upper() == 'Y':
        addon_price += 10.00
    if extra_gear.upper() == 'Y':
        addon_price += 25.00

    # Shipping Logic
    shipping = 5.00
    if tier_level == 3:
        shipping = 0.00

    monthly_total = base_price + addon_price + shipping
    annual_total = monthly_total * 12

    return base_price, addon_price, shipping, monthly_total, annual_total

def print_summary(name, base_price, addon_price, shipping, monthly_total, annual_total):
    print("\n=======================================")
    print("      SUBSCRIPTION ENROLLMENT          ")
    print("=======================================")
    print(f"Welcome, {name}!")
    print("---------------------------------------")
    print(f"Monthly Base Box:   ${base_price:,.2f}")
    
    if addon_price > 0:
        print(f"Monthly Add-ons:    ${addon_price:,.2f}")
        
    print(f"Shipping Fee:       ${shipping:,.2f}")
    print("---------------------------------------")
    print(f"TOTAL MONTHLY CHARGE: ${monthly_total:,.2f}")
    print(f"EST. ANNUAL COST:     ${annual_total:,.2f}")
    print("=======================================")

def main():
    print("--- GEEK CRATE SUBSCRIPTION ---")
    sub_name = input("Subscriber Name: ")
    
    try:
        tier_level = int(input("Tier (1=Basic $20, 2=Pro $40, 3=Elite $75): "))
    except ValueError:
        tier_level = 0

    extra_snacks = input("Add Snack Pack ($10/mo)? (Y/N): ")
    extra_gear = input("Add Premium Gear ($25/mo)? (Y/N): ")

    base_price, addon_price, shipping, monthly_total, annual_total = calculate_fees(
        tier_level, extra_snacks, extra_gear
    )

    print_summary(sub_name, base_price, addon_price, shipping, monthly_total, annual_total)

if __name__ == "__main__":
    main()
