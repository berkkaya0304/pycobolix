# FLOWER-SHOP - Blossoms Florist
# Converted from COBOL to Python

def main():
    print("--- BLOSSOMS FLORIST ---")
    recipient_name = input("Recipient Name: ")
    bouquet_size = int(input("Bouquet Size (1=Small $30, 2=Med $50, 3=Lrg $80): "))
    vase_type = int(input("Vase (1=Wrapped, 2=Glass $15, 3=Crystal $40): "))
    delivery_zone = int(input("Delivery Zone (1=Local $10, 2=Regional $25): "))

    if bouquet_size == 1:
        flower_cost = 30.00
    elif bouquet_size == 2:
        flower_cost = 50.00
    elif bouquet_size == 3:
        flower_cost = 80.00
    else:
        flower_cost = 30.00

    if vase_type == 1:
        vase_cost = 0.0
    elif vase_type == 2:
        vase_cost = 15.00
    elif vase_type == 3:
        vase_cost = 40.00
    else:
        vase_cost = 0.0

    deliv_fee = 25.00 if delivery_zone == 2 else 10.00

    total_bill = flower_cost + vase_cost + deliv_fee

    print("")
    print("========================================")
    print("          FLORIST ORDER RECEIPT         ")
    print("========================================")
    print(f"Send To: {recipient_name}")
    print("----------------------------------------")
    print(f"Arrangement:        ${flower_cost:,.2f}")
    if vase_cost > 0:
        print(f"Vase/Container:     ${vase_cost:,.2f}")
    print(f"Delivery Fee:       ${deliv_fee:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL AMOUNT DUE:   ${total_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
