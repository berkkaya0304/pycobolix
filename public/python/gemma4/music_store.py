from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print("--- RETRO WAVES MUSIC STORE ---")
    
    buyer_name = input("Customer: ")
    
    try:
        vinyl_qty = int(input("Vinyl Records QTY ($30 ea): ") or 0)
        cd_qty = int(input("CDs QTY ($15 ea): ") or 0)
        instrument_cost = Decimal(input("Musical Instruments Total ($): ") or "0.00")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    vinyl_tot = Decimal(vinyl_qty) * Decimal("30.00")
    cd_tot = Decimal(cd_qty) * Decimal("15.00")
    
    sub_price = vinyl_tot + cd_tot + instrument_cost
    
    mem_disc = Decimal("0.00")
    if sub_price > Decimal("100.00"):
        mem_disc = (sub_price * Decimal("0.10")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        
    final_amt = sub_price - mem_disc

    print("\n========================================")
    print("             STORE RECEIPT              ")
    print("========================================")
    print(f"Customer: {buyer_name}")
    print("----------------------------------------")
    
    if vinyl_qty > 0:
        print(f"Vinyl Records ({vinyl_qty}): {format_currency(vinyl_tot)}")
        
    if cd_qty > 0:
        print(f"CDs ({cd_qty}):           {format_currency(cd_tot)}")
        
    if instrument_cost > 0:
        print(f"Instruments:       {format_currency(instrument_cost)}")
        
    print("----------------------------------------")
    print(f"Subtotal:          {format_currency(sub_price)}")
    
    if mem_disc > 0:
        print(f"10% Discount:     -{format_currency(mem_disc)}")
        
    print("----------------------------------------")
    print(f"NET PAYABLE:       {format_currency(final_amt)}")
    print("========================================")

if __name__ == "__main__":
    main()
