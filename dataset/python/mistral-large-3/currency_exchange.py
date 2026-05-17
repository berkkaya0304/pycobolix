def currency_exchange():
    print("--- GLOBAL CURRENCY EXCHANGE ---")
    cust_name = input("Customer Name: ").strip()
    currency_from = input("Source Currency (USD/EUR/GBP): ").strip().upper()
    currency_to = input("Target Currency (USD/EUR/GBP): ").strip().upper()
    amount_to_exch = float(input("Amount to Exchange: ").strip())

    exchange_rates = {
        ('USD', 'EUR'): 0.9250,
        ('USD', 'GBP'): 0.7930,
        ('EUR', 'USD'): 1.0810,
        ('GBP', 'USD'): 1.2610
    }

    conv_rate = exchange_rates.get((currency_from, currency_to), 1.0000)
    if conv_rate == 1.0000 and (currency_from, currency_to) not in exchange_rates:
        print("Exchange route not supported. Rate = 1.0")

    conv_amount = amount_to_exch * conv_rate
    comm_fee = conv_amount * 0.02
    final_payout = conv_amount - comm_fee

    def format_currency(value):
        return f"{value:,.2f}"

    print("\n=========================================")
    print("        FOREX EXCHANGE RECEIPT           ")
    print("=========================================")
    print(f"Customer:      {cust_name}")
    print(f"Exchange Path: {currency_from} to {currency_to}")
    print(f"Exchange Rate: {conv_rate:.4f}")
    print("-----------------------------------------")
    print(f"Input Amount:  {format_currency(amount_to_exch)} {currency_from}")
    print(f"Gross Converted: {format_currency(conv_amount)} {currency_to}")
    print(f"Commission (2%):-{format_currency(comm_fee)} {currency_to}")
    print("-----------------------------------------")
    print(f"FINAL PAYOUT:   {format_currency(final_payout)} {currency_to}")
    print("=========================================")

if __name__ == "__main__":
    currency_exchange()
