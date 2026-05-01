def main():
    print("--- GALAXY ARCADE KIOSK ---")
    player_tag = input("Player Tag / Nickname: ")
    try:
        load_amount = float(input("Amount to load ($): "))
    except ValueError:
        load_amount = 0.0
    is_new_card = input("Is this a new card issue ($2 fee)? (Y/N): ").strip().upper() == 'Y'
    vip_status = input("Are you a VIP Gold Member? (Y/N): ").strip().upper() == 'Y'

    base_cr = load_amount * 4
    bonus_cr = 0
    if load_amount >= 50.00:
        bonus_cr = 50
    elif load_amount >= 25.00:
        bonus_cr = 15

    vip_cr = base_cr * 0.20 if vip_status else 0
    total_cr = base_cr + bonus_cr + vip_cr

    fees_paid = load_amount + 2.00 if is_new_card else load_amount

    print("\n========================================")
    print("           CARD RELOAD RECIEPT          ")
    print("========================================")
    print(f"Player: {player_tag}")
    print("----------------------------------------")
    print(f"Funds Loaded:       ${load_amount:9.2f}")
    if is_new_card:
        print("New Card Fee:       $     2.00")
    print(f"TOTAL CHARGED:      ${fees_paid:9.2f}")
    print("----------------------------------------")
    print("YOUR NEW ARCADE BALANCE:")
    print(f"      {int(total_cr):6d} CREDITS")
    print("========================================")

if __name__ == "__main__":
    main()
