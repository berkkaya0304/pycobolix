def main():
    print("--- PARADISE INN CHECKOUT ---")
    try:
        room_number = int(input("Room Number: "))
    except ValueError:
        room_number = 0
    guest_name = input("Guest Name: ")
    try:
        outstanding_bal = float(input("Oustanding Room Balance ($): "))
    except ValueError:
        outstanding_bal = 0.0
        
    minibar_use = input("Minibar used? (Y/N): ").strip().upper() == 'Y'
    minibar_fee = 0.0
    if minibar_use:
        try:
            minibar_fee = float(input("Total Minibar Charge ($): "))
        except ValueError:
            minibar_fee = 0.0

    try:
        room_service = float(input("Total Room Service Charges ($): "))
    except ValueError:
        room_service = 0.0
        
    try:
        room_damages = float(input("Room Damages Assessed ($): "))
    except ValueError:
        room_damages = 0.0

    resort_fee = 25.00
    sub_tot = outstanding_bal + minibar_fee + room_service + room_damages + resort_fee
    tax = sub_tot * 0.11
    final_bill = sub_tot + tax

    print("\n=========================================")
    print("           FINAL GUEST INVOICE           ")
    print("=========================================")
    print(f"Room: {room_number:04d}    Guest: {guest_name}")
    print("-----------------------------------------")
    print(f"Room Stay Balance: ${outstanding_bal:9.2f}")
    print(f"Daily Resort Fee:  ${resort_fee:9.2f}")
    
    if minibar_fee > 0:
        print(f"Minibar Charges:   ${minibar_fee:9.2f}")
        
    if room_service > 0:
        print(f"Room Service:      ${room_service:9.2f}")
        
    if room_damages > 0:
        print(f"Damage Assessment: ${room_damages:9.2f}")
        
    print("-----------------------------------------")
    print(f"Sub Total:         ${sub_tot:9.2f}")
    print(f"Taxes (11%):       ${tax:9.2f}")
    print("-----------------------------------------")
    print(f"FINAL AMOUNT SETTLED:${final_bill:9.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
