import decimal

def main():
    print("--- GALAXY ARCADE KIOSK ---")
    
    player_tag = input("Player Tag / Nickname: ")
    
    try:
        load_amount = decimal.Decimal(input("Amount to load ($): "))
    except decimal.InvalidOperation:
        load_amount = decimal.Decimal("0.00")

    is_new_card = input("Is this a new card issue ($2 fee)? (Y/N): ").upper() == 'Y'
    is_vip = input("Are you a VIP Gold Member? (Y/N): ").upper() == 'Y'

    # Calculate base credits
    base_cr = int(load_amount * 4)

    # Calculate bonus credits
    if load_amount >= 50.00:
        bonus_cr = 50
    elif load_amount >= 25.00:
        bonus_cr = 15
    else:
        bonus_cr = 0

    # Calculate VIP credits
    vip_cr = 0
    if is_vip:
        vip_cr = int(base_cr * 0.20)

    total_cr = base_cr + bonus_cr + vip_cr

    # Calculate total fees paid
    if is_new_card:
        fees_paid = load_amount + decimal.Decimal("2.00")
    else:
        fees_paid = load_amount

    # Display Receipt
    print("\n========================================")
    print("           CARD RELOAD RECIEPT          ")
    print("========================================")
    print(f"Player: {player_tag}")
    print("----------------------------------------")
    print(f"Funds Loaded:       ${load_amount:,.2f}")
    
    if is_new_card:
        print("New Card Fee:       $    2.00")
        
    print(f"TOTAL CHARGED:      ${fees_paid:,.2f}")
    print("----------------------------------------")
    print("YOUR NEW ARCADE BALANCE:")
    print(f"      {total_cr:,} CREDITS")
    print("========================================")

if __name__ == "__main__":
    main()
