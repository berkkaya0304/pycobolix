"""
Satellite Cinemas Box Office - Movie Theater
Converted from COBOL (movie_theater.cbl) to Python
"""


def main():
    print("+++ SATELLITE CINEMAS BOX OFFICE +++")
    loop_ctrl = "Y"

    while loop_ctrl.upper() == "Y":
        show_type = input("Show Type (M=Matinee, E=Evening, I=IMAX): ").strip().upper()
        adult_tkts = int(input("Number of Adult Tickets: "))
        child_tkts = int(input("Number of Child Tickets: "))
        popcorn_qty = int(input("Enter Large Popcorns QTY ($8 each): "))
        soda_qty = int(input("Enter Large Sodas QTY ($5 each): "))

        if show_type == "M":
            adult_fr, child_fr = 10.00, 7.00
        elif show_type == "I":
            adult_fr, child_fr = 18.00, 14.00
        else:
            adult_fr, child_fr = 14.00, 10.00

        tkt_total = (adult_tkts * adult_fr) + (child_tkts * child_fr)
        snack_total = (popcorn_qty * 8.00) + (soda_qty * 5.00)
        grand_total = tkt_total + snack_total

        print()
        print("----------------------------------------")
        print("         CINEMA RECEIPT                 ")
        print("----------------------------------------")
        print(f"Tickets Total:    ${tkt_total:>9,.2f}")
        print(f"Concessions:      ${snack_total:>9,.2f}")
        print("----------------------------------------")
        print(f"PLEASE PAY:       ${grand_total:>9,.2f}")
        print("Enjoy the show!")
        print("----------------------------------------")

        loop_ctrl = input("Next customer? (Y/N): ").strip().upper()


if __name__ == "__main__":
    main()
