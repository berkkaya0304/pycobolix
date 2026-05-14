class MovieTheater:
    def __init__(self):
        self.adult_tickets = 0
        self.child_tickets = 0
        self.show_type = ''
        self.popcorn_qty = 0
        self.soda_qty = 0
        self.adult_price = 0.0
        self.child_price = 0.0
        self.ticket_total = 0.0
        self.snack_total = 0.0
        self.grand_total = 0.0

    def get_order(self):
        print("Show Type (M=Matinee, E=Evening, I=IMAX): ")
        self.show_type = input().strip().upper()
        print("Number of Adult Tickets: ")
        self.adult_tickets = int(input())
        print("Number of Child Tickets: ")
        self.child_tickets = int(input())
        print("Enter Large Popcorns QTY ($8 each): ")
        self.popcorn_qty = int(input())
        print("Enter Large Sodas QTY ($5 each): ")
        self.soda_qty = int(input())

    def calculate_costs(self):
        if self.show_type == 'M':
            self.adult_price = 10.00
            self.child_price = 7.00
        elif self.show_type == 'E':
            self.adult_price = 14.00
            self.child_price = 10.00
        elif self.show_type == 'I':
            self.adult_price = 18.00
            self.child_price = 14.00
        else:
            self.adult_price = 14.00
            self.child_price = 10.00
            print("Defaulted to Evening Pricing.")

        self.ticket_total = (self.adult_tickets * self.adult_price) + (self.child_tickets * self.child_price)
        self.snack_total = (self.popcorn_qty * 8.00) + (self.soda_qty * 5.00)
        self.grand_total = self.ticket_total + self.snack_total

    def print_receipt(self):
        print("\n----------------------------------------")
        print("         CINEMA RECEIPT                 ")
        print("----------------------------------------")
        print(f"Tickets Total:    ${self.ticket_total:,.2f}")
        print(f"Concessions:      ${self.snack_total:,.2f}")
        print("----------------------------------------")
        print(f"PLEASE PAY:       ${self.grand_total:,.2f}")
        print("Enjoy the show!")
        print("----------------------------------------")

def main():
    print("+++ SATELLITE CINEMAS BOX OFFICE +++")
    theater = MovieTheater()
    
    while True:
        theater.get_order()
        theater.calculate_costs()
        theater.print_receipt()
        
        print("Next customer? (Y/N): ")
        if input().strip().upper() != 'Y':
            break

if __name__ == "__main__":
    main()
