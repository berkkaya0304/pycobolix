def subscription_box():
    print("--- GEEK CRATE SUBSCRIPTION ---")
    sub_name = input("Subscriber Name: ").strip()
    tier_level = int(input("Tier (1=Basic $20, 2=Pro $40, 3=Elite $75): ").strip())
    extra_snacks = input("Add Snack Pack ($10/mo)? (Y/N): ").strip().upper() == 'Y'
    extra_gear = input("Add Premium Gear ($25/mo)? (Y/N): ").strip().upper() == 'Y'

    base_price = 0.0
    addon_price = 0.0
    shipping = 5.00

    if tier_level == 1:
        base_price = 20.00
    elif tier_level == 2:
        base_price = 40.00
    elif tier_level == 3:
        base_price = 75.00
    else:
        base_price = 20.00
        print("Invalid tier, defaulted to Basic.")

    if extra_snacks:
        addon_price += 10.00

    if extra_gear:
        addon_price += 25.00

    if tier_level == 3:
        shipping = 0.00

    monthly_total = base_price + addon_price + shipping
    annual_total = monthly_total * 12

    print()
    print("=======================================")
    print("      SUBSCRIPTION ENROLLMENT          ")
    print("=======================================")
    print(f"Welcome, {sub_name}!")
    print("---------------------------------------")
    print(f"Monthly Base Box:   ${base_price:,.2f}")
    if addon_price > 0:
        print(f"Monthly Add-ons:    ${addon_price:,.2f}")
    print(f"Shipping Fee:       ${shipping:,.2f}")
    print("---------------------------------------")
    print(f"TOTAL MONTHLY CHARGE: ${monthly_total:,.2f}")
    print(f"EST. ANNUAL COST:     ${annual_total:,.2f}")
    print("=======================================")

if __name__ == "__main__":
    subscription_box()
