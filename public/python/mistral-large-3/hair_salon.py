def main():
    print("--- GLAMOUR STUDIO TICKET ---")
    client_name = input("Client: ").strip()
    wants_cut = input("Haircut? (Y/N): ").strip().upper() == 'Y'
    wants_color = input("Color/Dye? (Y/N): ").strip().upper() == 'Y'
    stylist_level = int(input("Stylist Level (1=Jr, 2=Sr, 3=Master): ").strip())
    tip_pct = int(input("Tip Percentage (e.g. 15, 20): ").strip())

    level_rate = 1.00
    if stylist_level == 2:
        level_rate = 1.30
    elif stylist_level == 3:
        level_rate = 1.80

    cut_fee = 35.00 * level_rate if wants_cut else 0.00
    color_fee = 85.00 * level_rate if wants_color else 0.00
    sub_price = cut_fee + color_fee
    tip_amt = sub_price * (tip_pct / 100)
    total_due = sub_price + tip_amt

    print("\n========================================")
    print("             SALON INVOICE              ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    if wants_cut:
        print(f"Haircut Service:    ${cut_fee:,.2f}")
    if wants_color:
        print(f"Coloring Service:   ${color_fee:,.2f}")
    print("----------------------------------------")
    print(f"Services Total:     ${sub_price:,.2f}")

    if tip_amt > 0:
        print(f"Stylist Tip ({tip_pct}%):  ${tip_amt:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL CHARGED:      ${total_due:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
