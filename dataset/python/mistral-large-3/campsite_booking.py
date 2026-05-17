def campsite_booking():
    print("--- PINE RIDGE CAMPGROUND ---")

    camper_name = input("Camper Name: ").strip()
    site_type = int(input("Site (1=Tent $20, 2=RV Hookup $50, 3=Cabin $100): "))
    stay_nights = int(input("Number of Nights: "))
    firewood_bundles = int(input("Firewood Bundles ($8 ea): "))

    site_rates = {1: 20.00, 2: 50.00, 3: 100.00}
    site_rate = site_rates.get(site_type, 20.00)

    site_total = stay_nights * site_rate
    wood_fee = firewood_bundles * 8.00
    park_pass = 15.00
    total_bill = site_total + wood_fee + park_pass

    print("\n========================================")
    print("          CAMPGROUND RESERVATION        ")
    print("========================================")
    print(f"Camper: {camper_name}")
    print(f"Nights: {stay_nights}")
    print("----------------------------------------")
    print(f"Site Reservation Fee:   ${site_total:,.2f}")

    if firewood_bundles > 0:
        print(f"Firewood ({firewood_bundles} bundles):   ${wood_fee:,.2f}")

    print(f"State Park Entry Pass:  ${park_pass:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE DUE:      ${total_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    campsite_booking()
