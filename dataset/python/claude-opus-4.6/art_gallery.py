"""
Modern Canvas Art Gallery Invoice
Converted from COBOL (art_gallery.cbl) to Python

Generates a gallery invoice for art purchases with shipping
and handling fees based on delivery method.
"""


def main():
    print("--- MODERN CANVAS GALLERY ---")
    collector_name = input("Collector Name: ")
    art_title = input("Artwork Title: ")
    art_price = float(input("Artwork Price ($): "))
    ship_method = int(input("Delivery: 1=Pickup, 2=Domestic, 3=Intl: "))

    ship_fee = 0.0
    handling_fee = 0.0

    if ship_method == 1:  # Pickup
        ship_fee = 0.0
        handling_fee = 0.0
    elif ship_method == 2:  # Domestic
        ship_fee = art_price * 0.03
        handling_fee = 50.00
    elif ship_method == 3:  # International
        ship_fee = art_price * 0.08
        handling_fee = 150.00
    else:
        ship_fee = 0.0

    grand_total = art_price + ship_fee + handling_fee

    print()
    print("========================================")
    print("           GALLERY INVOICE              ")
    print("========================================")
    print(f"Aquired By: {collector_name}")
    print(f"Artwork:    {art_title}")
    print("----------------------------------------")
    print(f"Base Price:          ${art_price:>12,.2f}")

    if ship_fee > 0:
        print(f"Freight Assessed:    ${ship_fee:>12,.2f}")

    if handling_fee > 0:
        print(f"Crate/Handling:      ${handling_fee:>12,.2f}")

    print("----------------------------------------")
    print(f"TOTAL PAYABLE:       ${grand_total:>12,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
