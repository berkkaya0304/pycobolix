"""
Galaxy Arcade Card Kiosk
Converted from COBOL (arcade_card.cbl) to Python

Simulates an arcade card loading kiosk that calculates credits
based on funds loaded, with bonus credits for higher loads,
VIP member bonus, and new card issuance fee.
"""


def main():
    print("--- GALAXY ARCADE KIOSK ---")
    player_tag = input("Player Tag / Nickname: ")
    load_amount = float(input("Amount to load ($): "))
    is_new_card = input("Is this a new card issue ($2 fee)? (Y/N): ").strip().upper()
    vip_status = input("Are you a VIP Gold Member? (Y/N): ").strip().upper()

    base_cr = int(load_amount * 4)

    if load_amount >= 50.00:
        bonus_cr = 50
    elif load_amount >= 25.00:
        bonus_cr = 15
    else:
        bonus_cr = 0

    vip_cr = 0
    if vip_status == "Y":
        vip_cr = int(base_cr * 0.20)

    total_cr = base_cr + bonus_cr + vip_cr

    if is_new_card == "Y":
        fees_paid = load_amount + 2.00
    else:
        fees_paid = load_amount

    print()
    print("========================================")
    print("           CARD RELOAD RECIEPT          ")
    print("========================================")
    print(f"Player: {player_tag}")
    print("----------------------------------------")
    print(f"Funds Loaded:       ${load_amount:>9,.2f}")
    if is_new_card == "Y":
        print("New Card Fee:       $    2.00")
    print(f"TOTAL CHARGED:      ${fees_paid:>9,.2f}")
    print("----------------------------------------")
    print("YOUR NEW ARCADE BALANCE:")
    print(f"      {total_cr:>9,} CREDITS")
    print("========================================")


if __name__ == "__main__":
    main()
