def main():
    print("--- STRIKE ZONE BOWLING ---")
    party_name = input("Party Name: ").strip()
    number_players = int(input("Number of Players: "))
    games_played = int(input("Number of Games Bowled: "))
    shoe_rentals = int(input("Number of Shoe Rentals ($4 each): "))
    league_member = input("League Member? (15% discount) (Y/N): ").strip().upper()

    RATE_PER_GAME = 6.00
    SHOE_FEE = 4.00

    total_games = number_players * games_played * RATE_PER_GAME
    total_shoes = shoe_rentals * SHOE_FEE
    gross_amt = total_games + total_shoes

    league_disc = 0.0
    if league_member == 'Y':
        league_disc = gross_amt * 0.15

    net_amt = gross_amt - league_disc

    print("\n" + "="*40)
    print("             LANE RECEIPT               ")
    print("="*40)
    print(f"Party: {party_name}")
    print(f"Players: {number_players} | Games: {games_played}")
    print("-"*40)
    print(f"Games Total:        ${total_games:,.2f}")
    
    if total_shoes > 0:
        print(f"Shoe Rentals ({shoe_rentals}):  ${total_shoes:,.2f}")
    
    if league_member == 'Y':
        print(f"League Discount:   -${league_disc:,.2f}")
    
    print("-"*40)
    print(f"TOTAL LANE FEE:     ${net_amt:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
