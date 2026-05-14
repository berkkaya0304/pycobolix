from decimal import Decimal, ROUND_HALF_UP

def main():
    # Exchange Rates Configuration
    rates = {
        ("USD", "EUR"): Decimal("0.9250"),
        ("USD", "GBP"): Decimal("0.7930"),
        ("EUR", "USD"): Decimal("1.0810"),
        ("GBP", "USD"): Decimal("1.2610"),
    }

    print("--- GLOBAL CURRENCY EXCHANGE ---")
    cust_name = input("Customer Name: ")
    currency_from = input("Source Currency (USD/EUR/GBP): ").strip().upper()
    currency_to = input("Target Currency (USD/EUR/GBP): ").strip().upper()
    
    try:
        amount_to_exch = Decimal(input("Amount to Exchange: "))
    except Exception:
        print("Invalid amount entered.")
        return

    # Process Conversion
    conv_rate = rates.get((currency_from, currency_to))
    
    if conv_rate is None:
        print("Exchange route not supported. Rate = 1.0")
        conv_rate = Decimal("1.0000")

    conv_amount = (amount_to_exch * conv_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    comm_fee = (conv_amount * Decimal("0.02")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    final_payout = conv_amount - comm_fee

    # Print Receipt
    print("\n=========================================")
    print("        FOREX EXCHANGE RECEIPT           ")
    print("=========================================")
    print(f"Customer:      {cust_name}")
    print(f"Exchange Path: {currency_from} to {currency_to}")
    print(f"Exchange Rate: {conv_rate}")
    print("-----------------------------------------")
    print(f"Input Amount:   {amount_to_exch:,.2f} {currency_from}")
    print(f"Gross Converted: {conv_amount:,.2f} {currency_to}")
    print(f"Commission (2%):- {comm_fee:,.2f} {currency_to}")
    print("-----------------------------------------")
    print(f"FINAL PAYOUT:   {final_payout:,.2f} {currency_to}")
    print("=========================================")

if __name__ == "__main__":
    main()
