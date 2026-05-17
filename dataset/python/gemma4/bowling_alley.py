def main():
    # Constants
    RATE_PER_GAME = 6.00
    SHOE_FEE = 4.00
    LEAGUE_DISCOUNT_RATE = 0.15

    print("--- STRIKE ZONE BOWLING ---")
    
    party_name = input("Party Name: ")
    try:
        number_players = int(input("Number of Players: "))
        games_played = int(input("Number of Games Bowled: "))
        shoe_rentals = int(input("Number of Shoe Rentals ($4 each): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for players, games, and rentals.")
        return

    league_member_input = input("League Member? (15% discount) (Y/N): ").strip().upper()
    is_league = league_member_input == 'Y'

    # Calculations
    total_games_cost = number_players * games_played * RATE_PER_GAME
    total_shoes_cost = shoe_rentals * SHOE_FEE
    gross_amount = total_games_cost + total_shoes_cost
    
    league_discount = 0.0
    if is_league:
        league_discount = gross_amount * LEAGUE_DISCOUNT_RATE
    
    net_amount = gross_amount - league_discount

    # Formatting helper to mimic PIC $Z,ZZ9.99
    def format_currency(amount):
        return f"${amount:,.2f}"

    # Output Receipt
    print("\n========================================")
    print("             LANE RECEIPT               ")
    print("========================================")
    print(f"Party: {party_name}")
    print(f"Players: {number_players} | Games: {games_played}")
    print("----------------------------------------")
    print(f"Games Total:        {format_currency(total_games_cost)}")
    
    if total_shoes_cost > 0:
        print(f"Shoe Rentals ({shoe_rentals}):  {format_currency(total_shoes_cost)}")
    
    if is_league:
        print(f"League Discount:   -{format_currency(league_discount)}")
        
    print("----------------------------------------")
    print(f"TOTAL LANE FEE:     {format_currency(net_amount)}")
    print("========================================")

if __name__ == "__main__":
    main()
