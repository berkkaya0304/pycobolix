def main():
    print("--- PINE RIDGE CAMPGROUND ---")
    camper_name = input("Camper Name: ")
    site_type = input("Site (1=Tent $20, 2=RV Hookup $50, 3=Cabin $100): ").strip()
    try:
        stay_nights = int(input("Number of Nights: "))
    except ValueError:
        stay_nights = 0
    try:
        firewood_bndl = int(input("Firewood Bundles ($8 ea): "))
    except ValueError:
        firewood_bndl = 0

    if site_type == '1':
        site_rate = 20.00
    elif site_type == '2':
        site_rate = 50.00
    elif site_type == '3':
        site_rate = 100.00
    else:
        site_rate = 20.00

    site_total = stay_nights * site_rate
    wood_fee = firewood_bndl * 8.00
    park_pass = 15.00

    total_bill = site_total + wood_fee + park_pass

    print("\n========================================")
    print("          CAMPGROUND RESERVATION        ")
    print("========================================")
    print(f"Camper: {camper_name}")
    print(f"Nights: {stay_nights}")
    print("----------------------------------------")
    print(f"Site Reservation Fee:   ${site_total:6.2f}")
    
    if firewood_bndl > 0:
        print(f"Firewood ({firewood_bndl} bundles):   ${wood_fee:6.2f}")
        
    print(f"State Park Entry Pass:  ${park_pass:6.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE DUE:      ${total_bill:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
