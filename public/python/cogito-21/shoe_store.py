def main():
    print("--- KICKS SNEAKER SHOP ---")
    print("PROMO: Buy One Get One 50% Off! (Max 10 pairs)")
    
    try:
        pair_qty = int(input("How many pairs being purchased?: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if pair_qty > 10:
        print("Max 10 pairs per transaction!")
        pair_qty = 10

    shoe_prices = []
    total_price = 0.0

    for i in range(pair_qty):
        while True:
            try:
                price = float(input(f"Price for Pair {i+1} ($): "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                shoe_prices.append(price)
                total_price += price
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")

    discount = 0.0
    for i in range(1, pair_qty, 2):
        discount += shoe_prices[i] * 0.5

    final_pay = total_price - discount

    print("\n" + "="*40)
    print("          STORE RECEIPT                 ")
    print("="*40)
    print(f"Items Bought: {pair_qty} pairs.")
    print("-"*40)
    
    for i, price in enumerate(shoe_prices, 1):
        print(f"Box {i}:            ${price:,.2f}")
    
    print("-"*40)
    print(f"Subtotal:        ${total_price:,.2f}")
    
    if discount > 0:
        print(f"BOGO 50% Savings:-${discount:,.2f}")
    
    print("-"*40)
    print(f"TOTAL DUE:       ${final_pay:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
