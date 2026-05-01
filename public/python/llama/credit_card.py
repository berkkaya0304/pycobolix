# CREDIT-CARD - Credit Card Statement Generator
# Converted from COBOL to Python

def main():
    APR_RATE = 19.99

    print("--- CREDIT CARD STATEMENT GEN ---")
    card_number = input("Card Number: ")
    cardholder = input("Cardholder Name: ")
    prev_balance = float(input("Previous Statement Balance: "))
    payments_made = float(input("Payments Made This Cycle: "))
    new_charges = float(input("New Purchase Charges: "))

    unpaid_bal = prev_balance - payments_made
    interest_chg = unpaid_bal * (APR_RATE / 100 / 12) if unpaid_bal > 0 else 0.0
    new_balance = unpaid_bal + new_charges + interest_chg

    min_payment = new_balance * 0.03
    if min_payment < 35.00 and new_balance >= 35.00:
        min_payment = 35.00
    elif new_balance < 35.00:
        min_payment = new_balance

    last_four = card_number[-4:] if len(card_number) >= 4 else card_number
    print("")
    print("=========================================")
    print("       MONTHLY ACCOUNT STATEMENT         ")
    print("=========================================")
    print(f"Card: **** **** **** {last_four}")
    print(f"Name: {cardholder}")
    print("-----------------------------------------")
    print(f"Previous Balance:    ${prev_balance:,.2f}")
    print(f"Payments / Credits: -${payments_made:,.2f}")
    print(f"New Purchases:      +${new_charges:,.2f}")
    print(f"Interest Charged:   +${interest_chg:,.2f}")
    print("-----------------------------------------")
    print(f"NEW BALANCE:         ${new_balance:,.2f}")
    print(f"MINIMUM PAYMENT DUE: ${min_payment:,.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
