def main():
    print("--- KICKS SNEAKER SHOP ---")
    print("PROMO: Buy One Get One 50% Off! (Max 10 pairs)")

    while True:
        try:
            pair_qty = int(input("How many pairs being purchased?: "))
            if pair_qty > 10:
                print("Max 10 pairs per transaction!")
                pair_qty = 10
            break
        except ValueError:
            print("Please enter a valid number.")

    shoe_prices = []
    total_price = 0.0

    for idx in range(pair_qty):
        while True:
            try:
                price = float(input(f"Price for Pair {idx + 1} ($): "))
                shoe_prices.append(price)
                total_price += price
                break
            except ValueError:
                print("Please enter a valid price.")

    discount = 0.0
    for idx in range(1, pair_qty + 1):
        if idx % 2 == 0:
            discount += shoe_prices[idx - 1] * 0.50

    final_pay = total_price - discount

    print("\n========================================")
    print("          STORE RECEIPT                 ")
    print("========================================")
    print(f"Items Bought: {pair_qty} pairs.")
    print("----------------------------------------")
    for idx, price in enumerate(shoe_prices, start=1):
        print(f"Box {idx}:            ${price:,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:        ${total_price:,.2f}")
    if discount > 0:
        print(f"BOGO 50% Savings:-${discount:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL QUE:       ${final_pay:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
