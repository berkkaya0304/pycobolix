from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- PARADISE INN CHECKOUT ---")
    
    room_number = input("Room Number: ")
    guest_name = input("Guest Name: ")
    
    try:
        outstanding_bal = Decimal(input("Oustanding Room Balance ($): ") or "0")
    except:
        outstanding_bal = Decimal("0")

    minibar_use = input("Minibar used? (Y/N): ").strip().upper()
    minibar_fee = Decimal("0")
    if minibar_use == 'Y':
        try:
            minibar_fee = Decimal(input("Total Minibar Charge ($): ") or "0")
        except:
            minibar_fee = Decimal("0")

    try:
        room_service = Decimal(input("Total Room Service Charges ($): ") or "0")
    except:
        room_service = Decimal("0")
        
    try:
        room_damages = Decimal(input("Room Damages Assessed ($): ") or "0")
    except:
        room_damages = Decimal("0")

    resort_fee = Decimal("25.00")
    
    # Calculations
    sub_tot = outstanding_bal + minibar_fee + room_service + room_damages + resort_fee
    tax = (sub_tot * Decimal("0.11")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    final_bill = sub_tot + tax

    # Receipt Generation
    print("\n=========================================")
    print("           FINAL GUEST INVOICE           ")
    print("=========================================")
    print(f"Room: {room_number:<5}    Guest: {guest_name}")
    print("-----------------------------------------")
    print(f"Room Stay Balance: {format_currency(outstanding_bal):>15}")
    print(f"Daily Resort Fee:  {format_currency(resort_fee):>15}")
    
    if minibar_fee > 0:
        print(f"Minibar Charges:   {format_currency(minibar_fee):>15}")
        
    if room_service > 0:
        print(f"Room Service:      {format_currency(room_service):>15}")
        
    if room_damages > 0:
        print(f"Damage Assessment: {format_currency(room_damages):>15}")
        
    print("-----------------------------------------")
    print(f"Sub Total:         {format_currency(sub_tot):>15}")
    print(f"Taxes (11%):       {format_currency(tax):>15}")
    print("-----------------------------------------")
    print(f"FINAL AMOUNT SETTLED:{format_currency(final_bill):>15}")
    print("=========================================")

if __name__ == "__main__":
    main()
