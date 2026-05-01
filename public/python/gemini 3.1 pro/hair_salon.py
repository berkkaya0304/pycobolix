def main():
    print("--- GLAMOUR STUDIO TICKET ---")
    client_name = input("Client: ")
    sv_haircut = input("Haircut? (Y/N): ").strip().upper() == 'Y'
    sv_color = input("Color/Dye? (Y/N): ").strip().upper() == 'Y'
    sv_stylist = input("Stylist Level (1=Jr, 2=Sr, 3=Master): ").strip()
    try:
        tip_pct = int(input("Tip Percentage (e.g. 15, 20): "))
    except ValueError:
        tip_pct = 0

    if sv_stylist == '1':
        level_rate = 1.00
    elif sv_stylist == '2':
        level_rate = 1.30
    elif sv_stylist == '3':
        level_rate = 1.80
    else:
        level_rate = 1.00

    cut_fee = 35.00 * level_rate if sv_haircut else 0.0
    color_fee = 85.00 * level_rate if sv_color else 0.0

    sub_price = cut_fee + color_fee
    tip_amt = sub_price * (tip_pct / 100.0)
    total_due = sub_price + tip_amt

    print("\n========================================")
    print("             SALON INVOICE              ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    
    if sv_haircut:
        print(f"Haircut Service:    ${cut_fee:6.2f}")
    if sv_color:
        print(f"Coloring Service:   ${color_fee:6.2f}")
        
    print("----------------------------------------")
    print(f"Services Total:     ${sub_price:6.2f}")
    
    if tip_amt > 0:
        print(f"Stylist Tip ({tip_pct:02d}%):  ${tip_amt:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL CHARGED:      ${total_due:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
