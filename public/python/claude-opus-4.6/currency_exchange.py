"""
Global Currency Exchange
Converted from COBOL (currency_exchange.cbl) to Python
"""


def main():
    # Exchange rates
    rates = {
        ("USD", "EUR"): 0.9250,
        ("USD", "GBP"): 0.7930,
        ("EUR", "USD"): 1.0810,
        ("GBP", "USD"): 1.2610,
    }

    print("--- GLOBAL CURRENCY EXCHANGE ---")
    cust_name = input("Customer Name: ")
    currency_from = input("Source Currency (USD/EUR/GBP): ").strip().upper()
    currency_to = input("Target Currency (USD/EUR/GBP): ").strip().upper()
    amount_to_exch = float(input("Amount to Exchange: "))

    conv_rate = rates.get((currency_from, currency_to), None)
    if conv_rate is None:
        print("Exchange route not supported. Rate = 1.0")
        conv_rate = 1.0000

    conv_amount = amount_to_exch * conv_rate
    comm_fee = conv_amount * 0.02
    final_payout = conv_amount - comm_fee

    print()
    print("=========================================")
    print("        FOREX EXCHANGE RECEIPT           ")
    print("=========================================")
    print(f"Customer:      {cust_name}")
    print(f"Exchange Path: {currency_from} to {currency_to}")
    print(f"Exchange Rate: {conv_rate:.4f}")
    print("-----------------------------------------")
    print(f"Input Amount:  {amount_to_exch:>12,.2f} {currency_from}")
    print(f"Gross Converted: {conv_amount:>10,.2f} {currency_to}")
    print(f"Commission (2%):-{comm_fee:>10,.2f} {currency_to}")
    print("-----------------------------------------")
    print(f"FINAL PAYOUT:   {final_payout:>10,.2f} {currency_to}")
    print("=========================================")


if __name__ == "__main__":
    main()
