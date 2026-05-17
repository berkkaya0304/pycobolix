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

    shoe_prc = [0.0] * pair_qty
    total_price = 0.0

    for idx in range(pair_qty):
        try:
            price = float(input(f"Price for Pair {idx + 1} ($): "))
        except ValueError:
            price = 0.0
        shoe_prc[idx] = price
        total_price += price

    discount = 0.0
    for idx in range(pair_qty):
        if (idx + 1) % 2 == 0:
            discount += (shoe_prc[idx] * 0.50)

    final_pay = total_price - discount

    print("\n========================================")
    print("          STORE RECEIPT                 ")
    print("========================================")
    print(f"Items Bought: {pair_qty:02d} pairs.")
    print("----------------------------------------")
    
    for idx in range(pair_qty):
        print(f"Box {idx + 1:02d}:            ${shoe_prc[idx]:7.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:        ${total_price:7.2f}")
    
    if discount > 0:
        print(f"BOGO 50% Savings:-${discount:7.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL QUE:       ${final_pay:7.2f}") # Kept typo QUE from COBOL to match original
    print("========================================")

if __name__ == "__main__":
    main()
