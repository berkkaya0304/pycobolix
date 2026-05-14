def main():
    print("--- GLAMOUR STUDIO TICKET ---")
    
    client_name = input("Client: ")
    sv_haircut = input("Haircut? (Y/N): ").upper()
    sv_color = input("Color/Dye? (Y/N): ").upper()
    
    try:
        sv_stylist = int(input("Stylist Level (1=Jr, 2=Sr, 3=Master): "))
    except ValueError:
        sv_stylist = 1
        
    try:
        tip_pct = int(input("Tip Percentage (e.g. 15, 20): "))
    except ValueError:
        tip_pct = 0

    # Determine Level Rate
    if sv_stylist == 1:
        level_rate = 1.00
    elif sv_stylist == 2:
        level_rate = 1.30
    elif sv_stylist == 3:
        level_rate = 1.80
    else:
        level_rate = 1.00

    # Calculate Fees
    cut_fee = 0.0
    if sv_haircut == 'Y':
        cut_fee = 35.00 * level_rate

    color_fee = 0.0
    if sv_color == 'Y':
        color_fee = 85.00 * level_rate

    sub_price = cut_fee + color_fee
    tip_amt = sub_price * (tip_pct / 100)
    total_due = sub_price + tip_amt

    # Invoice Display
    print("\n========================================")
    print("             SALON INVOICE              ")
    print("========================================")
    print(f"Client: {client_name}")
    print("----------------------------------------")
    
    if sv_haircut == 'Y':
        print(f"Haircut Service:    ${cut_fee:,.2f}")
    
    if sv_color == 'Y':
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
