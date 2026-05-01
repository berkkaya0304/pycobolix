# COMIC-BOOK-STORE - Galaxy Heroes Comics
# Converted from COBOL to Python

def main():
    COMIC_PRC = 4.99
    FIGURE_PRC = 24.99
    BOARD_PRC = 49.99

    print("--- GALAXY HEROES COMICS ---")
    comic_qty = int(input("Single Issue Comics QTY ($4.99 ea): "))
    figure_qty = int(input("Action Figures QTY ($24.99 ea): "))
    board_game_qty = int(input("Board Games QTY ($49.99 ea): "))
    sub_monthly = input("Pull-List Subscriber (10% Off)? (Y/N): ").strip().upper()

    c_tot = comic_qty * COMIC_PRC
    f_tot = figure_qty * FIGURE_PRC
    b_tot = board_game_qty * BOARD_PRC
    subtot = c_tot + f_tot + b_tot

    discount = subtot * 0.10 if sub_monthly == 'Y' else 0.0
    final_bill = subtot - discount

    print("")
    print("========================================")
    print("             STORE TICKET               ")
    print("========================================")
    if comic_qty > 0:
        print(f"Comics ({comic_qty}):           ${c_tot:,.2f}")
    if figure_qty > 0:
        print(f"Figures ({figure_qty}):          ${f_tot:,.2f}")
    if board_game_qty > 0:
        print(f"Board Games ({board_game_qty}):      ${b_tot:,.2f}")
    print("----------------------------------------")
    print(f"Subtotal:            ${subtot:,.2f}")
    if sub_monthly == 'Y':
        print(f"Subscriber Disc(10%):-${discount:,.2f}")
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       ${final_bill:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
