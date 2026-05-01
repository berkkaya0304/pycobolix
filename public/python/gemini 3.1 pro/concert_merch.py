def main():
    print("--- STADIUM MERCH BOOTH ---")
    fan_name = input("Fan Name: ")
    try:
        tshirt_qty = int(input("Tour T-Shirts ($35 ea): "))
    except ValueError:
        tshirt_qty = 0
    try:
        poster_qty = int(input("Tour Posters ($15 ea): "))
    except ValueError:
        poster_qty = 0
    try:
        record_qty = int(input("Vinyl Records ($40 ea): "))
    except ValueError:
        record_qty = 0
        
    wants_signed = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper() == 'Y'

    tshirt_prc = 35.00
    poster_prc = 15.00
    record_prc = 40.00
    sign_fee = 20.00

    tshirt_tot = tshirt_qty * tshirt_prc
    poster_tot = poster_qty * poster_prc
    record_tot = record_qty * record_prc

    sub_tot = tshirt_tot + poster_tot + record_tot

    if wants_signed:
        total_due = sub_tot + sign_fee
    else:
        total_due = sub_tot

    print("\n========================================")
    print("           MERCHANDISE RECEIPT          ")
    print("========================================")
    print(f"Fan: {fan_name}")
    print("----------------------------------------")
    
    if tshirt_qty > 0:
        print(f"T-Shirts ({tshirt_qty}):        ${tshirt_tot:6.2f}")
    if poster_qty > 0:
        print(f"Posters ({poster_qty}):         ${poster_tot:6.2f}")
    if record_qty > 0:
        print(f"Vinyl Records ({record_qty}):   ${record_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:            ${sub_tot:6.2f}")
    
    if wants_signed:
        print(f"VIP Autograph Add-On:${sign_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    ${total_due:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
