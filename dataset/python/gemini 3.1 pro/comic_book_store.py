def main():
    print("--- GALAXY HEROES COMICS ---")
    try:
        comic_qty = int(input("Single Issue Comics QTY ($4.99 ea): "))
    except ValueError:
        comic_qty = 0
    try:
        figure_qty = int(input("Action Figures QTY ($24.99 ea): "))
    except ValueError:
        figure_qty = 0
    try:
        board_game_qty = int(input("Board Games QTY ($49.99 ea): "))
    except ValueError:
        board_game_qty = 0
    
    sub_monthly = input("Pull-List Subscriber (10% Off)? (Y/N): ").strip().upper() == 'Y'

    comic_prc = 4.99
    figure_prc = 24.99
    board_prc = 49.99

    c_tot = comic_qty * comic_prc
    f_tot = figure_qty * figure_prc
    b_tot = board_game_qty * board_prc

    subtot = c_tot + f_tot + b_tot

    discount = subtot * 0.10 if sub_monthly else 0.0

    final_bill = subtot - discount

    print("\n========================================")
    print("             STORE TICKET               ")
    print("========================================")
    
    if comic_qty > 0:
        print(f"Comics ({comic_qty}):           ${c_tot:6.2f}")
    if figure_qty > 0:
        print(f"Figures ({figure_qty}):          ${f_tot:6.2f}")
    if board_game_qty > 0:
        print(f"Board Games ({board_game_qty}):      ${b_tot:6.2f}")
        
    print("----------------------------------------")
    print(f"Subtotal:            ${subtot:6.2f}")
    
    if sub_monthly:
        print(f"Subscriber Disc(10%):-${discount:6.2f}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${final_bill:6.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
