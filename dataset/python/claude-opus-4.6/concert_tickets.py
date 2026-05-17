"""
Summer Festival Box Office - Concert Tickets
Converted from COBOL (concert_tickets.cbl) to Python
"""


def main():
    ga_price = 75.00
    vip_price = 250.00
    parking_fee = 40.00

    print("*** SUMMER FESTIVAL BOX OFFICE ***")
    buyer_name = input("Ticket Buyer Name: ")
    gen_adm_qty = int(input("Quantity of General Admission ($75): "))
    vip_qty = int(input("Quantity of VIP Passes ($250): "))
    parking_pass = input("Add VIP Parking Pass ($40)? (Y/N): ").strip().upper()

    ga_total = gen_adm_qty * ga_price
    vip_total = vip_qty * vip_price

    grand_sum = ga_total + vip_total

    if parking_pass == "Y":
        grand_sum += parking_fee

    processing_fee = grand_sum * 0.08
    grand_sum += processing_fee

    print()
    print("**************************************")
    print("        FESTIVAL TICKET INVOICE       ")
    print("**************************************")
    print(f"Purchaser: {buyer_name}")
    print("--------------------------------------")
    if gen_adm_qty > 0:
        print(f"{gen_adm_qty}x General Adm:   ${ga_total:>9,.2f}")
    if vip_qty > 0:
        print(f"{vip_qty}x VIP Pass:      ${vip_total:>9,.2f}")
    if parking_pass == "Y":
        print(f"1x Parking Pass: ${parking_fee:>9,.2f}")
    print("--------------------------------------")
    print(f"Service Fees(8%):${processing_fee:>9,.2f}")
    print(f"TOTAL DUE:       ${grand_sum:>9,.2f}")
    print("**************************************")


if __name__ == "__main__":
    main()
