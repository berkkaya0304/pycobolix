from decimal import Decimal, ROUND_HALF_UP

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    # Prices
    COMIC_PRC = Decimal("4.99")
    FIGURE_PRC = Decimal("24.99")
    BOARD_PRC = Decimal("49.99")

    print("--- GALAXY HEROES COMICS ---")
    
    try:
        comic_qty = int(input("Single Issue Comics QTY ($4.99 ea): ") or 0)
        figure_qty = int(input("Action Figures QTY ($24.99 ea): ") or 0)
        board_game_qty = int(input("Board Games QTY ($49.99 ea): ") or 0)
        sub_monthly = input("Pull-List Subscriber (10% Off)? (Y/N): ").strip().upper()
    except ValueError:
        print("Invalid input. Please enter numeric values for quantities.")
        return

    is_subscriber = (sub_monthly == 'Y')

    # Calculations
    c_tot = comic_qty * COMIC_PRC
    f_tot = figure_qty * FIGURE_PRC
    b_tot = board_game_qty * BOARD_PRC
    
    subtot = c_tot + f_tot + b_tot
    discount = Decimal("0.00")

    if is_subscriber:
        discount = (subtot * Decimal("0.10")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    final_bill = subtot - discount

    # Output
    print("\n========================================")
    print("             STORE TICKET               ")
    print("========================================")
    
    if comic_qty > 0:
        print(f"Comics ({comic_qty}):           {format_currency(c_tot)}")
    if figure_qty > 0:
        print(f"Figures ({figure_qty}):          {format_currency(f_tot)}")
    if board_game_qty > 0:
        print(f"Board Games ({board_game_qty}):      {format_currency(b_tot)}")
        
    print("----------------------------------------")
    print(f"Subtotal:            {format_currency(subtot)}")
    
    if is_subscriber:
        print(f"Subscriber Disc(10%):- {format_currency(discount)}")
        
    print("----------------------------------------")
    print(f"TOTAL BALANCE:       {format_currency(final_bill)}")
    print("========================================")

if __name__ == "__main__":
    main()
