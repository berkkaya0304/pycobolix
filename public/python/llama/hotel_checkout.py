# HOTEL-CHECKOUT - Paradise Inn Checkout
# Converted from COBOL to Python

def main():
    RESORT_FEE = 25.00

    print("--- PARADISE INN CHECKOUT ---")
    room_number = input("Room Number: ")
    guest_name = input("Guest Name: ")
    outstanding_bal = float(input("Oustanding Room Balance ($): "))

    minibar_use = input("Minibar used? (Y/N): ").strip().upper()
    minibar_fee = 0.0
    if minibar_use == 'Y':
        minibar_fee = float(input("Total Minibar Charge ($): "))

    room_service = float(input("Total Room Service Charges ($): "))
    room_damages = float(input("Room Damages Assessed ($): "))

    sub_tot = outstanding_bal + minibar_fee + room_service + room_damages + RESORT_FEE
    tax = sub_tot * 0.11
    final_bill = sub_tot + tax

    print("")
    print("=========================================")
    print("           FINAL GUEST INVOICE           ")
    print("=========================================")
    print(f"Room: {room_number}    Guest: {guest_name}")
    print("-----------------------------------------")
    print(f"Room Stay Balance: ${outstanding_bal:,.2f}")
    print(f"Daily Resort Fee:  ${RESORT_FEE:,.2f}")
    if minibar_fee > 0:
        print(f"Minibar Charges:   ${minibar_fee:,.2f}")
    if room_service > 0:
        print(f"Room Service:      ${room_service:,.2f}")
    if room_damages > 0:
        print(f"Damage Assessment: ${room_damages:,.2f}")
    print("-----------------------------------------")
    print(f"Sub Total:         ${sub_tot:,.2f}")
    print(f"Taxes (11%):       ${tax:,.2f}")
    print("-----------------------------------------")
    print(f"FINAL AMOUNT SETTLED:${final_bill:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
