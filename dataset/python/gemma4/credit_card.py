from decimal import Decimal, ROUND_HALF_UP

def format_currency(value):
    return f"${value:,.2f}"

def main():
    print("--- CREDIT CARD STATEMENT GEN ---")
    
    card_number = input("Card Number: ")
    cardholder = input("Cardholder Name: ")
    
    try:
        prev_balance = Decimal(input("Previous Statement Balance: "))
        payments_made = Decimal(input("Payments Made This Cycle: "))
        new_charges = Decimal(input("New Purchase Charges: "))
    except ValueError:
        print("Invalid numeric input.")
        return

    # Constants
    apr_rate = Decimal("19.99")
    
    # Calculations
    unpaid_bal = prev_balance - payments_made
    
    interest_chg = Decimal("0.00")
    if unpaid_bal > 0:
        # Monthly interest = (APR / 100 / 12)
        interest_chg = unpaid_bal * (apr_rate / 100 / 12)
    
    new_balance = unpaid_bal + new_charges + interest_chg
    
    min_payment = new_balance * Decimal("0.03")
    if min_payment < Decimal("35.00") and new_balance >= Decimal("35.00"):
        min_payment = Decimal("35.00")
    elif new_balance < Decimal("35.00"):
        min_payment = new_balance

    # Print Statement
    print("\n=========================================")
    print("       MONTHLY ACCOUNT STATEMENT         ")
    print("=========================================")
    
    # Mask card number to show only last 4 digits
    masked_card = f"**** **** **** {card_number[-4:] if len(card_number) >= 4 else card_number}"
    print(f"Card: {masked_card}")
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
