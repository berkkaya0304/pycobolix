"""
Strike Zone Bowling Alley
Converted from COBOL (bowling_alley.cbl) to Python
"""


def main():
    rate_per_game = 6.00
    shoe_fee = 4.00

    print("--- STRIKE ZONE BOWLING ---")
    party_name = input("Party Name: ")
    number_players = int(input("Number of Players: "))
    games_played = int(input("Number of Games Bowled: "))
    shoe_rentals = int(input("Number of Shoe Rentals ($4 each): "))
    league_member = input("League Member? (15% discount) (Y/N): ").strip().upper()

    total_games = number_players * games_played * rate_per_game
    total_shoes = shoe_rentals * shoe_fee
    gross_amt = total_games + total_shoes

    league_disc = gross_amt * 0.15 if league_member == "Y" else 0.0
    net_amt = gross_amt - league_disc

    print()
    print("========================================")
    print("             LANE RECEIPT               ")
    print("========================================")
    print(f"Party: {party_name}")
    print(f"Players: {number_players} | Games: {games_played}")
    print("----------------------------------------")
    print(f"Games Total:        ${total_games:>9,.2f}")
    if total_shoes > 0:
        print(f"Shoe Rentals ({shoe_rentals}):  ${total_shoes:>9,.2f}")
    if league_member == "Y":
        print(f"League Discount:   -${league_disc:>9,.2f}")
    print("----------------------------------------")
    print(f"TOTAL LANE FEE:     ${net_amt:>9,.2f}")
    print("========================================")


if __name__ == "__main__":
    main()
