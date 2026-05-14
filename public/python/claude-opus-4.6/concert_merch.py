"""
Stadium Merch Booth - Concert Merchandise
Converted from COBOL (concert_merch.cbl) to Python
"""


def main():
    tshirt_prc = 35.00
    poster_prc = 15.00
    record_prc = 40.00
    sign_fee = 20.00

    print("--- STADIUM MERCH BOOTH ---")
    fan_name = input("Fan Name: ")
    tshirt_qty = int(input("Tour T-Shirts ($35 ea): "))
    poster_qty = int(input("Tour Posters ($15 ea): "))
    record_qty = int(input("Vinyl Records ($40 ea): "))
    signed_addon = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper()

    tshirt_tot = tshirt_qty * tshirt_prc
    poster_tot = poster_qty * poster_prc
    record_tot = record_qty * record_prc
    sub_tot = tshirt_tot + poster_tot + record_tot

    total_due = sub_tot + sign_fee if signed_addon == "Y" else sub_tot

    print()
    print("========================================")
    print("           MERCHANDISE RECEIPT          ")
    print("========================================")
    print(f"Fan: {fan_name}")
    print("----------------------------------------")
    if tshirt_qty > 0:
        print(f"T-Shirts ({tshirt_qty}):        ${tshirt_tot:>9,.2f}")
    if poster_qty > 0:
        print(f"Posters ({poster_qty}):         ${poster_tot:>9,.2f}")
    if record_qty > 0:
        print(f"Vinyl Records ({record_qty}):   ${record_tot:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:            ${sub_tot:>9,.2f}")
    if signed_addon == "Y":
        print(f"VIP Autograph Add-On:${sign_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_due:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
