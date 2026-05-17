def main():
    print("+++ SATELLITE CINEMAS BOX OFFICE +++")
    loop_ctrl = 'Y'

    while loop_ctrl in ('Y', 'y'):
        show_type = input("Show Type (M=Matinee, E=Evening, I=IMAX): ").strip().upper()
        try:
            adult_tkts = int(input("Number of Adult Tickets: "))
        except ValueError:
            adult_tkts = 0
        try:
            child_tkts = int(input("Number of Child Tickets: "))
        except ValueError:
            child_tkts = 0
        try:
            popcorn_qty = int(input("Enter Large Popcorns QTY ($8 each): "))
        except ValueError:
            popcorn_qty = 0
        try:
            soda_qty = int(input("Enter Large Sodas QTY ($5 each): "))
        except ValueError:
            soda_qty = 0

        if show_type == 'M':
            adult_fr = 10.00
            child_fr = 7.00
        elif show_type == 'E':
            adult_fr = 14.00
            child_fr = 10.00
        elif show_type == 'I':
            adult_fr = 18.00
            child_fr = 14.00
        else:
            adult_fr = 14.00
            child_fr = 10.00
            print("Defaulted to Evening Pricing.")

        tkt_total = (adult_tkts * adult_fr) + (child_tkts * child_fr)
        snack_total = (popcorn_qty * 8.00) + (soda_qty * 5.00)
        grand_total = tkt_total + snack_total

        print("\n----------------------------------------")
        print("         CINEMA RECEIPT                 ")
        print("----------------------------------------")
        print(f"Tickets Total:    ${tkt_total:6.2f}")
        print(f"Concessions:      ${snack_total:6.2f}")
        print("----------------------------------------")
        print(f"PLEASE PAY:       ${grand_total:6.2f}")
        print("Enjoy the show!")
        print("----------------------------------------\n")

        loop_ctrl = input("Next customer? (Y/N): ").strip()

if __name__ == "__main__":
    main()
