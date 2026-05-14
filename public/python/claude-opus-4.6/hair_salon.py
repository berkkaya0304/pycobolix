"""
Glamour Studio - Hair Salon
Converted from COBOL (hair_salon.cbl) to Python
"""


def main():
    print("--- GLAMOUR STUDIO TICKET ---")
    client_name = input("Client: ")
    sv_haircut = input("Haircut? (Y/N): ").strip().upper()
    sv_color = input("Color/Dye? (Y/N): ").strip().upper()
    sv_stylist = int(input("Stylist Level (1=Jr, 2=Sr, 3=Master): "))
    tip_pct = int(input("Tip Percentage (e.g. 15, 20): "))

    if sv_stylist == 1:
        level_rate = 1.00
    elif sv_stylist == 2:
        level_rate = 1.30
    elif sv_stylist == 3:
        level_rate = 1.80
    else:
        level_rate = 1.00

    cut_fee = 35.00 * level_rate if sv_haircut == "Y" else 0.0
    color_fee = 85.00 * level_rate if sv_color == "Y" else 0.0

    sub_price = cut_fee + color_fee
    tip_amt = sub_price * (tip_pct / 100)
    total_due = sub_price + tip_amt

    print()
    print("========================================")
    print("             SALON INVOICE              ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    if sv_haircut == "Y":
        print(f"Haircut Service:    ${cut_fee:>9,.2f}")
    if sv_color == "Y":
        print(f"Coloring Service:   ${color_fee:>9,.2f}")
    print("----------------------------------------")
    print(f"Services Total:     ${sub_price:>9,.2f}")
    if tip_amt > 0:
        print(f"Stylist Tip ({tip_pct}%):  ${tip_amt:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL CHARGED:      ${total_due:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
