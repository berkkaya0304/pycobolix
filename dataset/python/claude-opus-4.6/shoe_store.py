"""
Kicks Sneaker Shop - Shoe Store
Converted from COBOL (shoe_store.cbl) to Python
"""


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

    discount = sum(shoe_prices[i] * 0.50 for i in range(len(shoe_prices)) if (i + 1) % 2 == 0)
    final_pay = total_price - discount

    print()
    print("========================================")
    print("          STORE RECEIPT                 ")
    print("========================================")
    print(f"Items Bought: {pair_qty} pairs.")
    print("----------------------------------------")
    for i, price in enumerate(shoe_prices, 1):
        print(f"Box {i}:            ${price:>9,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:        ${total_price:>9,.2f}")
    if discount > 0:
        print(f"BOGO 50% Savings:-${discount:>8,.2f}")
    print("----------------------------------------")
    print(f"TOTAL QUE:       ${final_pay:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
