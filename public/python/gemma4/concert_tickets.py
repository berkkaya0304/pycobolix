def main():
    # Constants
    GA_PRICE = 75.00
    VIP_PRICE = 250.00
    PARKING_FEE = 40.00
    SERVICE_FEE_RATE = 0.08

    print("*** SUMMER FESTIVAL BOX OFFICE ***")
    
    buyer_name = input("Ticket Buyer Name: ")
    try:
        gen_adm_qty = int(input("Quantity of General Admission ($75): ") or 0)
        vip_qty = int(input("Quantity of VIP Passes ($250): ") or 0)
    except ValueError:
        gen_adm_qty = 0
        vip_qty = 0
        
    parking_pass = input("Add VIP Parking Pass ($40)? (Y/N): ").upper()
    wants_parking = (parking_pass == 'Y')

    # Process Transaction
    ga_total = gen_adm_qty * GA_PRICE
    vip_total = vip_qty * VIP_PRICE
    
    grand_sum = ga_total + vip_total
    
    if wants_parking:
        grand_sum += PARKING_FEE

    processing_fee = grand_sum * SERVICE_FEE_RATE
    grand_sum += processing_fee

    # Display Invoice
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
        print(f"1x Parking Pass: ${PARKING_FEE:,.2f}")
        
    print("--------------------------------------")
    print(f"Service Fees(8%):${processing_fee:,.2f}")
    print(f"TOTAL DUE:       ${grand_sum:,.2f}")
    print("**************************************")

if __name__ == "__main__":
    main()
