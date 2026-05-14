def main():
    print("--- KICKS SNEAKER SHOP ---")
    print("PROMO: Buy One Get One 50% Off! (Max 10 pairs)")
    
    try:
        pair_qty = int(input("How many pairs being purchased?: "))
    except ValueError:
        pair_qty = 0

    if pair_qty > 10:
        print("Max 10 pairs per transaction!")
        pair_qty = 10
    elif pair_qty < 0:
        pair_qty = 0

    shoe_prices = []
    total_price = 0.0

    for idx in range(1, pair_qty + 1):
        try:
            price = float(input(f"Price for Pair {idx} ($): "))
        except ValueError:
            price = 0.0
        shoe_prices.append(price)
        total_price += price

    discount = 0.0
    for idx in range(1, pair_qty + 1):
        # COBOL MOD(IDX, 2) = 0 identifies even-numbered items for the BOGO discount
        if idx % 2 == 0:
            discount += shoe_prices[idx - 1] * 0.50

    final_pay = total_price - discount

    print("\n========================================")
    print("          STORE RECEIPT                 ")
    print("========================================")
    print(f"Items Bought: {pair_qty} pairs.")
    print("----------------------------------------")
    
    for idx, price in enumerate(shoe_prices, 1):
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
