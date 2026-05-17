def main():
    print("--- RETRO WAVES MUSIC STORE ---")
    buyer_name = input("Customer: ")
    try:
        vinyl_qty = int(input("Vinyl Records QTY ($30 ea): "))
    except ValueError:
        vinyl_qty = 0
    try:
        cd_qty = int(input("CDs QTY ($15 ea): "))
    except ValueError:
        cd_qty = 0
    try:
        instrument_cost = float(input("Musical Instruments Total ($): "))
    except ValueError:
        instrument_cost = 0.0

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
        print(f"Vinyl Records ({vinyl_qty:02d}): ${vinyl_tot:8.2f}")
    if cd_qty > 0:
        print(f"CDs ({cd_qty:02d}):           ${cd_tot:8.2f}")
    if instrument_cost > 0:
        print(f"Instruments:       ${instrument_cost:8.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:          ${sub_price:8.2f}")
    
    if mem_disc > 0:
        print(f"10% Discount:     -${mem_disc:8.2f}")
        
    print("----------------------------------------")
    print(f"NET PAYABLE:       ${final_amt:8.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
