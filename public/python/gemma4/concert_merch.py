def main():
    # Prices
    TSHIRT_PRC = 35.00
    POSTER_PRC = 15.00
    RECORD_PRC = 40.00
    SIGN_FEE = 20.00

    print("--- STADIUM MERCH BOOTH ---")
    
    fan_name = input("Fan Name: ")
    
    try:
        tshirt_qty = int(input("Tour T-Shirts ($35 ea): ") or 0)
        poster_qty = int(input("Tour Posters ($15 ea): ") or 0)
        record_qty = int(input("Vinyl Records ($40 ea): ") or 0)
    except ValueError:
        tshirt_qty = poster_qty = record_qty = 0

    signed_addon = input("Add Band VIP Autograph ($20 flat)? (Y/N): ").strip().upper()
    wants_signed = (signed_addon == 'Y')

    # Calculations
    tshirt_tot = tshirt_qty * TSHIRT_PRC
    poster_tot = poster_qty * POSTER_PRC
    record_tot = record_qty * RECORD_PRC
    
    sub_tot = tshirt_tot + poster_tot + record_tot
    total_due = sub_tot + (SIGN_FEE if wants_signed else 0)

    # Formatting helper for the COBOL $Z,ZZ9.99 style
    def format_currency(amount):
        return f"${amount:,.2f}"

    print("\n========================================")
    print("           MERCHANDISE RECEIPT          ")
    print("========================================")
    print(f"Fan: {fan_name}")
    print("----------------------------------------")
    
    if tshirt_qty > 0:
        print(f"T-Shirts ({tshirt_qty}):        {format_currency(tshirt_tot)}")
    
    if poster_qty > 0:
        print(f"Posters ({poster_qty}):         {format_currency(poster_tot)}")
        
    if record_qty > 0:
        print(f"Vinyl Records ({record_qty}):   {format_currency(record_tot)}")
        
    print("----------------------------------------")
    print(f"Subtotal:            {format_currency(sub_tot)}")
    
    if wants_signed:
        print(f"VIP Autograph Add-On: {format_currency(SIGN_FEE)}")
        
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:    {format_currency(total_due)}")
    print("========================================")

if __name__ == "__main__":
    main()
