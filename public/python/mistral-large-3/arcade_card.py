def arcade_card():
    print("--- GALAXY ARCADE KIOSK ---")
    player_tag = input("Player Tag / Nickname: ").strip()
    load_amount = float(input("Amount to load ($): "))
    is_new_card = input("Is this a new card issue ($2 fee)? (Y/N): ").strip().upper() == 'Y'
    vip_status = input("Are you a VIP Gold Member? (Y/N): ").strip().upper() == 'Y'

    base_cr = int(load_amount * 4)
    bonus_cr = 50 if load_amount >= 50.00 else 15 if load_amount >= 25.00 else 0
    vip_cr = int(base_cr * 0.20) if vip_status else 0
    total_cr = base_cr + bonus_cr + vip_cr
    fees_paid = load_amount + 2.00 if is_new_card else load_amount

    print("\n========================================")
    print("           CARD RELOAD RECEIPT          ")
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
    arcade_card()
