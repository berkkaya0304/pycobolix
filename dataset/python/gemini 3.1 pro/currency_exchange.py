def main():
    print("--- GLOBAL CURRENCY EXCHANGE ---")
    cust_name = input("Customer Name: ")
    currency_from = input("Source Currency (USD/EUR/GBP): ").strip().upper()
    currency_to = input("Target Currency (USD/EUR/GBP): ").strip().upper()
    try:
        amount_to_exch = float(input("Amount to Exchange: "))
    except ValueError:
        amount_to_exch = 0.0

    rate_usd_eur = 0.9250
    rate_usd_gbp = 0.7930
    rate_eur_usd = 1.0810
    rate_gbp_usd = 1.2610

    if currency_from == "USD" and currency_to == "EUR":
        conv_rate = rate_usd_eur
    elif currency_from == "USD" and currency_to == "GBP":
        conv_rate = rate_usd_gbp
    elif currency_from == "EUR" and currency_to == "USD":
        conv_rate = rate_eur_usd
    elif currency_from == "GBP" and currency_to == "USD":
        conv_rate = rate_gbp_usd
    else:
        print("Exchange route not supported. Rate = 1.0")
        conv_rate = 1.0000

    conv_amount = amount_to_exch * conv_rate
    comm_fee = conv_amount * 0.02
    final_payout = conv_amount - comm_fee

    print("\n=========================================")
    print("        FOREX EXCHANGE RECEIPT           ")
    print("=========================================")
    print(f"Customer:      {cust_name}")
    print(f"Exchange Path: {currency_from} to {currency_to}")
    print(f"Exchange Rate: {conv_rate:.4f}")
    print("-----------------------------------------")
    print(f"Input Amount:  {amount_to_exch:11.2f} {currency_from}")
    print(f"Gross Converted: {conv_amount:10.2f} {currency_to}")
    print(f"Commission (2%):-{comm_fee:10.2f} {currency_to}")
    print("-----------------------------------------")
    print(f"FINAL PAYOUT:   {final_payout:11.2f} {currency_to}")
    print("=========================================")

if __name__ == "__main__":
    main()
