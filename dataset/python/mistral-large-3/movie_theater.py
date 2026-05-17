def main_cashier():
    print("+++ SATELLITE CINEMAS BOX OFFICE +++")
    while True:
        ticket_info, concessions = get_order()
        pricing = calculate_costs(ticket_info, concessions)
        print_receipt(pricing)
        loop_ctrl = input("Next customer? (Y/N): ").strip().upper()
        if loop_ctrl != 'Y':
            break

def get_order():
    show_type = input("Show Type (M=Matinee, E=Evening, I=IMAX): ").strip().upper()
    adult_tkts = int(input("Number of Adult Tickets: "))
    child_tkts = int(input("Number of Child Tickets: "))
    popcorn_qty = int(input("Enter Large Popcorns QTY ($8 each): "))
    soda_qty = int(input("Enter Large Sodas QTY ($5 each): "))
    return {'show_type': show_type, 'adult_tkts': adult_tkts, 'child_tkts': child_tkts}, \
           {'popcorn_qty': popcorn_qty, 'soda_qty': soda_qty}

def calculate_costs(ticket_info, concessions):
    show_type = ticket_info['show_type']
    adult_tkts = ticket_info['adult_tkts']
    child_tkts = ticket_info['child_tkts']
    popcorn_qty = concessions['popcorn_qty']
    soda_qty = concessions['soda_qty']

    if show_type == 'M':
        adult_fr, child_fr = 10.00, 7.00
    elif show_type == 'E':
        adult_fr, child_fr = 14.00, 10.00
    elif show_type == 'I':
        adult_fr, child_fr = 18.00, 14.00
    else:
        adult_fr, child_fr = 14.00, 10.00
        print("Defaulted to Evening Pricing.")

    tkt_total = (adult_tkts * adult_fr) + (child_tkts * child_fr)
    snack_total = (popcorn_qty * 8.00) + (soda_qty * 5.00)
    grand_total = tkt_total + snack_total

    return {
        'adult_fr': adult_fr,
        'child_fr': child_fr,
        'tkt_total': tkt_total,
        'snack_total': snack_total,
        'grand_total': grand_total
    }

def print_receipt(pricing):
    print("\n----------------------------------------")
    print("         CINEMA RECEIPT                 ")
    print("----------------------------------------")
    print(f"Tickets Total:    ${pricing['tkt_total']:,.2f}")
    print(f"Concessions:      ${pricing['snack_total']:,.2f}")
    print("----------------------------------------")
    print(f"PLEASE PAY:       ${pricing['grand_total']:,.2f}")
    print("Enjoy the show!")
    print("----------------------------------------")

if __name__ == "__main__":
    main_cashier()
