"""
Pine Ridge Campground Booking
Converted from COBOL (campsite_booking.cbl) to Python
"""


def main():
    print("--- PINE RIDGE CAMPGROUND ---")
    camper_name = input("Camper Name: ")
    site_type = int(input("Site (1=Tent $20, 2=RV Hookup $50, 3=Cabin $100): "))
    stay_nights = int(input("Number of Nights: "))
    firewood_bndl = int(input("Firewood Bundles ($8 ea): "))

    if site_type == 1:
        site_rate = 20.00
    elif site_type == 2:
        site_rate = 50.00
    elif site_type == 3:
        site_rate = 100.00
    else:
        site_rate = 20.00

    site_total = stay_nights * site_rate
    wood_fee = firewood_bndl * 8.00
    park_pass = 15.00
    total_bill = site_total + wood_fee + park_pass

    print()
    print("========================================")
    print("          CAMPGROUND RESERVATION        ")
    print("========================================")
    print(f"Camper: {camper_name}")
    print(f"Nights: {stay_nights}")
    print("----------------------------------------")
    print(f"Site Reservation Fee:   ${site_total:>9,.2f}")
    if firewood_bndl > 0:
        print(f"Firewood ({firewood_bndl} bundles):   ${wood_fee:>9,.2f}")
    print(f"State Park Entry Pass:  ${park_pass:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE DUE:      ${total_bill:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
