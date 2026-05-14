def arcade_card():
    print("--- GALAXY ARCADE KIOSK ---")
    player_tag = input("Player Tag / Nickname: ")
    load_amount = float(input("Amount to load ($): "))
    is_new_card = input("Is this a new card issue ($2 fee)? (Y/N): ").upper()
    vip_status = input("Are you a VIP Gold Member? (Y/N): ").upper()

    base_cr = int(load_amount * 4)
    
    if load_amount >= 50.00:
        bonus_cr = 50
    elif load_amount >= 25.00:
        bonus_cr = 15
    else:
        bonus_cr = 0

    vip_cr = int(base_cr * 0.20) if vip_status == 'Y' else 0
    total_cr = base_cr + bonus_cr + vip_cr

    fees_paid = load_amount + 2.00 if is_new_card == 'Y' else load_amount

    print("\n" + "=" * 40)
    print("           CARD RELOAD RECEIPT          ")
    print("=" * 40)
    print(f"Player: {player_tag}")
    print("-" * 40)
    print(f"Funds Loaded:       ${load_amount:8.2f}")
    if is_new_card == 'Y':
        print("New Card Fee:       $    2.00")
    print(f"TOTAL CHARGED:      ${fees_paid:8.2f}")
    print("-" * 40)
    print("YOUR NEW ARCADE BALANCE:")
    print(f"      {total_cr:,} CREDITS")
    print("=" * 40)

if __name__ == "__main__":
    arcade_card()
