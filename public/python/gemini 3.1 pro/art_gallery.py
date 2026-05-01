def main():
    print("--- MODERN CANVAS GALLERY ---")
    collector_name = input("Collector Name: ")
    art_title = input("Artwork Title: ")
    try:
        art_price = float(input("Artwork Price ($): "))
    except ValueError:
        art_price = 0.0
    ship_method = input("Delivery: 1=Pickup, 2=Domestic, 3=Intl: ").strip()

    ship_fee = 0.0
    handling_fee = 0.0

    if ship_method == '1':
        pass
    elif ship_method == '2':
        ship_fee = art_price * 0.03
        handling_fee = 50.00
    elif ship_method == '3':
        ship_fee = art_price * 0.08
        handling_fee = 150.00

    grand_app = art_price + ship_fee + handling_fee

    print("\n========================================")
    print("           GALLERY INVOICE              ")
    print("========================================")
    print(f"Aquired By: {collector_name}")
    print(f"Artwork:    {art_title}")
    print("----------------------------------------")
    print(f"Base Price:          ${art_price:11.2f}")
    
    if ship_fee > 0:
        print(f"Freight Assessed:    ${ship_fee:11.2f}")
    
    if handling_fee > 0:
        print(f"Crate/Handling:      ${handling_fee:11.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL PAYABLE:       ${grand_app:11.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
