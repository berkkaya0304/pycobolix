# CONCERT-MERCH - Stadium Merch Booth
# Converted from COBOL to Python

def main():
    TSHIRT_PRC = 35.00
    POSTER_PRC = 15.00
    RECORD_PRC = 40.00
    SIGN_FEE = 20.00

    print("--- STADIUM MERCH BOOTH ---")
    fan_name = input("Fan Name: ")
    tshirt_qty = int(input("Tour T-Shirts ($35 ea): "))
    poster_qty = int(input("Tour Posters ($15 ea): "))
    record_qty = int(input("Vinyl Records ($40 ea): "))
    signed_addon = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper()

    tshirt_tot = tshirt_qty * TSHIRT_PRC
    poster_tot = poster_qty * POSTER_PRC
    record_tot = record_qty * RECORD_PRC
    sub_tot = tshirt_tot + poster_tot + record_tot

    total_due = sub_tot + SIGN_FEE if signed_addon == 'Y' else sub_tot

    print("")
    print("========================================")
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
    print(f"Subtotal:            ${sub_tot:,.2f}")
    if signed_addon == 'Y':
        print(f"VIP Autograph Add-On:${SIGN_FEE:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
