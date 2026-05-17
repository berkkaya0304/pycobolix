def main():
    print("--- PARADISE INN CHECKOUT ---")
    room_number = input("Room Number: ")
    guest_name = input("Guest Name: ")
    
    try:
        outstanding_bal = float(input("Outstanding Room Balance ($): "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    minibar_used = input("Minibar used? (Y/N): ").strip().upper() == 'Y'
    minibar_fee = 0.0
    if minibar_used:
        try:
            minibar_fee = float(input("Total Minibar Charge ($): "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

    try:
        room_service = float(input("Total Room Service Charges ($): "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    try:
        room_damages = float(input("Room Damages Assessed ($): "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    resort_fee = 25.00
    subtotal = outstanding_bal + minibar_fee + room_service + room_damages + resort_fee
    tax = subtotal * 0.11
    final_bill = subtotal + tax

    print("\n=========================================")
    print("           FINAL GUEST INVOICE           ")
    print("=========================================")
    print(f"Room: {room_number}    Guest: {guest_name}")
    print("-----------------------------------------")
    print(f"Room Stay Balance: ${outstanding_bal:,.2f}")
    print(f"Daily Resort Fee:  ${resort_fee:,.2f}")
    
    if minibar_fee > 0:
        print(f"Minibar Charges:   ${minibar_fee:,.2f}")
    
    if room_service > 0:
        print(f"Room Service:      ${room_service:,.2f}")
    
    if room_damages > 0:
        print(f"Damage Assessment: ${room_damages:,.2f}")
    
    print("-----------------------------------------")
    print(f"Sub Total:         ${subtotal:,.2f}")
    print(f"Taxes (11%):       ${tax:,.2f}")
    print("-----------------------------------------")
    print(f"FINAL AMOUNT SETTLED: ${final_bill:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
