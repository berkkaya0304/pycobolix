class Book:
    def __init__(self):
        self.isbn = "9781234567890"
        self.title = "The Great Cobol Mystery"
        self.author = "Grace Hopper"
        self.available = True
        self.borrower_id = None

class LibrarySystem:
    def __init__(self):
        self.book = Book()
        self.late_fee_per_day = 0.50
        self.max_borrow_days = 14

    def show_status(self):
        print(f"Title:  {self.book.title}")
        print(f"ISBN:   {self.book.isbn}")
        print(f"Author: {self.book.author}")
        status = "AVAILABLE ON SHELF" if self.book.available else "BORROWED OUT"
        print(f"Status: {status}")

    def borrow_book(self):
        if not self.book.available:
            print("Sorry, this book is currently unavailable.")
            return

        try:
            member_id = int(input("Enter Member ID: "))
            if member_id <= 0:
                print("Invalid Member ID. Please enter a positive number.")
                return
            self.book.available = False
            self.book.borrower_id = member_id
            print(f"Book checked out to Member {member_id}")
            print("Return within 14 days to avoid fines.")
        except ValueError:
            print("Invalid input. Please enter a valid Member ID (numbers only).")

    def return_book(self):
        if self.book.available:
            print("This book is already in the library!")
            return

        try:
            days_borrowed = int(input("Enter number of days it was borrowed: "))
            if days_borrowed < 0:
                print("Days borrowed cannot be negative.")
                return

            late_days = days_borrowed - self.max_borrow_days
            if late_days > 0:
                fine_amount = late_days * self.late_fee_per_day
                print(f"LATE RETURN: {late_days} days.")
                print(f"Please collect fine: ${fine_amount:,.2f}")
            else:
                print("Book returned on time. No fines.")

            self.book.available = True
            self.book.borrower_id = None
            print("Book is now restocked to the shelf.")
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")

    def run(self):
        print("Initializing Library Book...")
        while True:
            print("\n--- LIBRARY SYSTEM ---")
            print("1. View Book Status")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Exit")
            
            try:
                choice = int(input("Select option: "))
            except ValueError:
                print("Invalid Option.")
                continue

            if choice == 1:
                self.show_status()
            elif choice == 2:
                self.borrow_book()
            elif choice == 3:
                self.return_book()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid Option.")

if __name__ == "__main__":
    library = LibrarySystem()
    library.run()
