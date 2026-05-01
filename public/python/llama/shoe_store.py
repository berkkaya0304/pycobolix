# SHOE-STORE - Kicks Sneaker Shop
# Converted from COBOL to Python

def main():
    print("--- KICKS SNEAKER SHOP ---")
    print("PROMO: Buy One Get One 50% Off! (Max 10 pairs)")
    pair_qty = int(input("How many pairs being purchased?: "))
    if pair_qty > 10:
        print("Max 10 pairs per transaction!")
        pair_qty = 10

    shoe_prices = []
    total_price = 0.0
    for i in range(1, pair_qty + 1):
        price = float(input(f"Price for Pair {i} ($): "))
        shoe_prices.append(price)
        total_price += price

    # BOGO: every 2nd pair (index 2, 4, 6...) gets 50% off
    discount = 0.0
    for i, price in enumerate(shoe_prices, start=1):
        if i % 2 == 0:
            discount += price * 0.50

    final_pay = total_price - discount

    print("")
    print("========================================")
    print("          STORE RECEIPT                 ")
    print("========================================")
    print(f"Items Bought: {pair_qty} pairs.")
    print("----------------------------------------")
    for i, price in enumerate(shoe_prices, start=1):
        print(f"Box {i}:            ${price:,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:        ${total_price:,.2f}")
    if discount > 0:
        print(f"BOGO 50% Savings:-${discount:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL QUE:       ${final_pay:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
