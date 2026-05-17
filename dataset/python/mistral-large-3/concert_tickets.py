def main():
    print("*** SUMMER FESTIVAL BOX OFFICE ***")

    buyer_name = input("Ticket Buyer Name: ")
    gen_adm_qty = int(input("Quantity of General Admission ($75): "))
    vip_qty = int(input("Quantity of VIP Passes ($250): "))
    wants_parking = input("Add VIP Parking Pass ($40)? (Y/N): ").upper() == 'Y'

    ga_price = 75.00
    vip_price = 250.00
    parking_fee = 40.00

    ga_total = gen_adm_qty * ga_price
    vip_total = vip_qty * vip_price
    grand_sum = ga_total + vip_total

    if wants_parking:
        grand_sum += parking_fee

    processing_fee = grand_sum * 0.08
    grand_sum += processing_fee

    print("\n**************************************")
    print("        FESTIVAL TICKET INVOICE       ")
    print("**************************************")
    print(f"Purchaser: {buyer_name}")
    print("--------------------------------------")

    if gen_adm_qty > 0:
        print(f"{gen_adm_qty}x General Adm:   ${ga_total:,.2f}")

    if vip_qty > 0:
        print(f"{vip_qty}x VIP Pass:      ${vip_total:,.2f}")

    if wants_parking:
        print(f"1x Parking Pass: ${parking_fee:,.2f}")

    print("--------------------------------------")
    print(f"Service Fees(8%): ${processing_fee:,.2f}")
    print(f"TOTAL DUE:       ${grand_sum:,.2f}")
    print("**************************************")

if __name__ == "__main__":
    main()
