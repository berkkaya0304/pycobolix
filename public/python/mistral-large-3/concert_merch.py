def concert_merch():
    print("--- STADIUM MERCH BOOTH ---")

    fan_name = input("Fan Name: ").strip()
    tshirt_qty = int(input("Tour T-Shirts ($35 ea): "))
    poster_qty = int(input("Tour Posters ($15 ea): "))
    record_qty = int(input("Vinyl Records ($40 ea): "))
    signed_addon = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper()

    prices = {
        'tshirt': 35.00,
        'poster': 15.00,
        'record': 40.00,
        'sign_fee': 20.00
    }

    tshirt_tot = tshirt_qty * prices['tshirt']
    poster_tot = poster_qty * prices['poster']
    record_tot = record_qty * prices['record']
    subtotal = tshirt_tot + poster_tot + record_tot

    total_due = subtotal + prices['sign_fee'] if signed_addon == 'Y' else subtotal

    print("\n========================================")
    print("           MERCHANDISE RECEIPT          ")
    print("========================================")
    print(f"Fan: {fan_name}")
    print("----------------------------------------")

    if tshirt_qty > 0:
        print(f"T-Shirts ({tshirt_qty}):        ${tshirt_tot:,.2f}")
    if poster_qty > 0:
        print(f"Posters ({poster_qty}):         ${poster_tot:,.2f}")
    if record_qty > 0:
        print(f"Vinyl Records ({record_qty}):   ${record_tot:,.2f}")

    print("----------------------------------------")
    print(f"Subtotal:            ${subtotal:,.2f}")

    if signed_addon == 'Y':
        print(f"VIP Autograph Add-On: ${prices['sign_fee']:,.2f}")

    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    concert_merch()
