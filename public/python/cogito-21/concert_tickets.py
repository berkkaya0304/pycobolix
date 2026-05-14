def main():
    print("*** SUMMER FESTIVAL BOX OFFICE ***")
    buyer_name = input("Ticket Buyer Name: ")
    
    try:
        ga_qty = int(input("Quantity of General Admission ($75): "))
        vip_qty = int(input("Quantity of VIP Passes ($250): "))
        parking = input("Add VIP Parking Pass ($40)? (Y/N): ").strip().upper()
        
        wants_parking = parking == 'Y'
        
        ga_price = 75.00
        vip_price = 250.00
        parking_fee = 40.00 if wants_parking else 0.00
        
        ga_total = ga_qty * ga_price
        vip_total = vip_qty * vip_price
        
        subtotal = ga_total + vip_total
        grand_sum = subtotal + parking_fee
        processing_fee = grand_sum * 0.08
        grand_total = grand_sum + processing_fee
        
        print("\n" + "*" * 38)
        print("        FESTIVAL TICKET INVOICE       ")
        print("*" * 38)
        print(f"Purchaser: {buyer_name}")
        print("-" * 38)
        
        if ga_qty > 0:
            print(f"{ga_qty}x General Adm:   ${ga_total:,.2f}")
        if vip_qty > 0:
            print(f"{vip_qty}x VIP Pass:      ${vip_total:,.2f}")
        if wants_parking:
            print(f"1x Parking Pass:  ${parking_fee:,.2f}")
            
        print("-" * 38)
        print(f"Service Fees(8%): ${processing_fee:,.2f}")
        print(f"TOTAL DUE:       ${grand_total:,.2f}")
        print("*" * 38)
        
    except ValueError:
        print("Error: Please enter valid numeric values for ticket quantities.")

if __name__ == "__main__":
    main()
