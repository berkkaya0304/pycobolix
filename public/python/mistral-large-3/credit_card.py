def main():
    print("--- CREDIT CARD STATEMENT GEN ---")
    card_number = input("Card Number: ").strip()
    cardholder = input("Cardholder Name: ").strip()
    prev_balance = float(input("Previous Statement Balance: "))
    payments_made = float(input("Payments Made This Cycle: "))
    new_charges = float(input("New Purchase Charges: "))

    unpaid_bal, interest_chg, new_balance, min_payment = calc_statement(
        prev_balance, payments_made, new_charges
    )

    print_statement(
        card_number, cardholder, prev_balance, payments_made,
        new_charges, interest_chg, new_balance, min_payment
    )

def calc_statement(prev_balance, payments_made, new_charges):
    apr_rate = 19.99
    unpaid_bal = prev_balance - payments_made
    interest_chg = unpaid_bal * (apr_rate / 100 / 12) if unpaid_bal > 0 else 0.0
    new_balance = unpaid_bal + new_charges + interest_chg
    min_payment = new_balance * 0.03

    if min_payment < 35.00 and new_balance >= 35.00:
        min_payment = 35.00
    elif new_balance < 35.00:
        min_payment = new_balance

    return unpaid_bal, interest_chg, new_balance, min_payment

def print_statement(card_number, cardholder, prev_balance, payments_made,
                   new_charges, interest_chg, new_balance, min_payment):
    def format_currency(value):
        return f"${value:,.2f}"

    print()
    print("=========================================")
    print("       MONTHLY ACCOUNT STATEMENT         ")
    print("=========================================")
    print(f"Card: **** **** **** {card_number[-4:]}")
    print(f"Name: {cardholder}")
    print("-----------------------------------------")
    print(f"Previous Balance:    {format_currency(prev_balance)}")
    print(f"Payments / Credits: -{format_currency(payments_made)}")
    print(f"New Purchases:      +{format_currency(new_charges)}")
    print(f"Interest Charged:   +{format_currency(interest_chg)}")
    print("-----------------------------------------")
    print(f"NEW BALANCE:         {format_currency(new_balance)}")
    print(f"MINIMUM PAYMENT DUE: {format_currency(min_payment)}")
    print("=========================================")

if __name__ == "__main__":
    main()
