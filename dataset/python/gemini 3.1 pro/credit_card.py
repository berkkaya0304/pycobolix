def main():
    print("--- CREDIT CARD STATEMENT GEN ---")
    card_number = input("Card Number: ")
    cardholder = input("Cardholder Name: ")
    try:
        prev_balance = float(input("Previous Statement Balance: "))
    except ValueError:
        prev_balance = 0.0
    try:
        payments_made = float(input("Payments Made This Cycle: "))
    except ValueError:
        payments_made = 0.0
    try:
        new_charges = float(input("New Purchase Charges: "))
    except ValueError:
        new_charges = 0.0

    apr_rate = 19.99
    unpaid_bal = prev_balance - payments_made

    interest_chg = 0.0
    if unpaid_bal > 0:
        interest_chg = unpaid_bal * (apr_rate / 100 / 12)

    new_balance = unpaid_bal + new_charges + interest_chg

    min_payment = new_balance * 0.03
    if min_payment < 35.00 and new_balance >= 35.00:
        min_payment = 35.00
    elif new_balance < 35.00:
        min_payment = new_balance

    masked_card = card_number[-4:] if len(card_number) >= 4 else "0000"

    print("\n=========================================")
    print("       MONTHLY ACCOUNT STATEMENT         ")
    print("=========================================")
    print(f"Card: **** **** **** {masked_card}")
    print(f"Name: {cardholder}")
    print("-----------------------------------------")
    print(f"Previous Balance:    ${prev_balance:9.2f}")
    print(f"Payments / Credits: -${payments_made:9.2f}")
    print(f"New Purchases:      +${new_charges:9.2f}")
    print(f"Interest Charged:   +${interest_chg:9.2f}")
    print("-----------------------------------------")
    print(f"NEW BALANCE:         ${new_balance:9.2f}")
    print(f"MINIMUM PAYMENT DUE: ${min_payment:9.2f}")
    print("=========================================")

if __name__ == "__main__":
    main()
