def art_gallery():
    print("--- MODERN CANVAS GALLERY ---")
    collector_name = input("Collector Name: ").strip()
    art_title = input("Artwork Title: ").strip()
    art_price = float(input("Artwork Price ($): "))
    print("Delivery: 1=Pickup, 2=Domestic, 3=Intl: ", end="")
    ship_method = int(input())

    ship_fee = 0.0
    handling_fee = 0.0

    if ship_method == 1:
        ship_fee = 0.0
        handling_fee = 0.0
    elif ship_method == 2:
        ship_fee = art_price * 0.03
        handling_fee = 50.00
    elif ship_method == 3:
        ship_fee = art_price * 0.08
        handling_fee = 150.00

    grand_total = art_price + ship_fee + handling_fee

    print("")
    print("=" * 40)
    print("           GALLERY INVOICE              ")
    print("=" * 40)
    print(f"Aquired By: {collector_name}")
    print(f"Artwork:    {art_title}")
    print("-" * 40)
    print(f"Base Price:          ${art_price:,.2f}")

    if ship_fee > 0:
        print(f"Freight Assessed:    ${ship_fee:,.2f}")

    if handling_fee > 0:
        print(f"Crate/Handling:      ${handling_fee:,.2f}")

    print("-" * 40)
    print(f"TOTAL PAYABLE:       ${grand_total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    art_gallery()
