class CurrencyExchange:
    def __init__(self):
        self.exchange_rates = {
            ('USD', 'EUR'): 0.9250,
            ('USD', 'GBP'): 0.7930,
            ('EUR', 'USD'): 1.0810,
            ('GBP', 'USD'): 1.2610
        }
        self.commission_rate = 0.02

    def get_user_input(self):
        print("--- GLOBAL CURRENCY EXCHANGE ---")
        cust_name = input("Customer Name: ").strip()
        
        while True:
            currency_from = input("Source Currency (USD/EUR/GBP): ").strip().upper()
            if currency_from in ['USD', 'EUR', 'GBP']:
                break
            print("Invalid currency. Please enter USD, EUR, or GBP.")
            
        while True:
            currency_to = input("Target Currency (USD/EUR/GBP): ").strip().upper()
            if currency_to in ['USD', 'EUR', 'GBP']:
                break
            print("Invalid currency. Please enter USD, EUR, or GBP.")
            
        while True:
            try:
                amount = float(input("Amount to Exchange: "))
                if amount > 0:
                    break
                print("Amount must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")
                
        return cust_name, currency_from, currency_to, amount

    def process_conversion(self, currency_from, currency_to, amount):
        if currency_from == currency_to:
            conv_rate = 1.0
            print("Same currency selected. No conversion needed.")
        else:
            conv_rate = self.exchange_rates.get((currency_from, currency_to), 1.0)
            if conv_rate == 1.0:
                print("Exchange route not supported. Rate = 1.0")
        
        conv_amount = amount * conv_rate
        comm_fee = conv_amount * self.commission_rate
        final_payout = conv_amount - comm_fee
        
        return conv_rate, conv_amount, comm_fee, final_payout

    def format_currency(self, amount):
        return f"{amount:,.2f}"

    def print_receipt(self, cust_name, currency_from, currency_to, amount, 
                     conv_rate, conv_amount, comm_fee, final_payout):
        print("\n" + "=" * 40)
        print("        FOREX EXCHANGE RECEIPT           ")
        print("=" * 40)
        print(f"Customer:      {cust_name}")
        print(f"Exchange Path: {currency_from} to {currency_to}")
        print(f"Exchange Rate: {conv_rate:.4f}")
        print("-" * 40)
        print(f"Input Amount:  {self.format_currency(amount)} {currency_from}")
        print(f"Gross Converted: {self.format_currency(conv_amount)} {currency_to}")
        print(f"Commission (2%):-{self.format_currency(comm_fee)} {currency_to}")
        print("-" * 40)
        print(f"FINAL PAYOUT:   {self.format_currency(final_payout)} {currency_to}")
        print("=" * 40)

    def run(self):
        cust_name, currency_from, currency_to, amount = self.get_user_input()
        conv_rate, conv_amount, comm_fee, final_payout = self.process_conversion(
            currency_from, currency_to, amount
        )
        self.print_receipt(
            cust_name, currency_from, currency_to, amount,
            conv_rate, conv_amount, comm_fee, final_payout
        )

if __name__ == "__main__":
    exchange = CurrencyExchange()
    exchange.run()
