def main():
    print("--- RETRO WAVES MUSIC STORE ---")
    buyer_name = input("Customer: ")
    
    vinyl_qty = int(input("Vinyl Records QTY ($30 ea): "))
    cd_qty = int(input("CDs QTY ($15 ea): "))
    instrument_cost = float(input("Musical Instruments Total ($): "))

    vinyl_tot = vinyl_qty * 30.00
    cd_tot = cd_qty * 15.00
    sub_price = vinyl_tot + cd_tot + instrument_cost

    mem_disc = 0.0
    if sub_price > 100.00:
        mem_disc = sub_price * 0.10

    final_amt = sub_price - mem_disc

    print("\n========================================")
    print("             STORE RECEIPT              ")
    print("========================================")
    print(f"Customer: {buyer_name}")
    print("----------------------------------------")
    
    if vinyl_qty > 0:
        print(f"Vinyl Records ({vinyl_qty}): ${vinyl_tot:,.2f}")
    if cd_qty > 0:
        print(f"CDs ({cd_qty}):           ${cd_tot:,.2f}")
    if instrument_cost > 0:
        print(f"Instruments:       ${instrument_cost:,.2f}")
    
    print("----------------------------------------")
    print(f"Subtotal:          ${sub_price:,.2f}")
    
    if mem_disc > 0:
        print(f"10% Discount:     -${mem_disc:,.2f}")
    
    print("----------------------------------------")
    print(f"NET PAYABLE:       ${final_amt:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
