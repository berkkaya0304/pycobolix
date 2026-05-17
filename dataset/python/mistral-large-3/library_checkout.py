class LibraryManagement:
    def __init__(self):
        self.book_details = {
            "isbn": "9781234567890",
            "title": "The Great Cobol Mystery",
            "author": "Grace Hopper",
            "available": True
        }
        self.member_id = None
        self.days_borrowed = 0

    def show_status(self):
        print(f"Title:  {self.book_details['title']}")
        print(f"ISBN:   {self.book_details['isbn']}")
        print(f"Author: {self.book_details['author']}")
        if self.book_details["available"]:
            print("Status: AVAILABLE ON SHELF")
        else:
            print("Status: BORROWED OUT")

    def borrow_book(self):
        if not self.book_details["available"]:
            print("Sorry, this book is currently unavailable.")
        else:
            self.member_id = input("Enter Member ID: ")
            self.book_details["available"] = False
            print(f"Book checked out to Member {self.member_id}")
            print("Return within 14 days to avoid fines.")

    def return_book(self):
        if self.book_details["available"]:
            print("This book is already in the library!")
        else:
            self.days_borrowed = int(input("Enter number of days it was borrowed: "))
            late_days = self.days_borrowed - 14

            if late_days > 0:
                fine_amount = late_days * 0.50
                print(f"LATE RETURN: {late_days} days.")
                print(f"Please collect fine: ${fine_amount:.2f}")
            else:
                print("Book returned on time. No fines.")

            self.book_details["available"] = True
            print("Book is now restocked to the shelf.")

    def run(self):
        print("Initializing Library Book...")

        while True:
            print()
            print("--- LIBRARY SYSTEM ---")
            print("1. View Book Status")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Exit")
            menu_opt = input("Select option: ")

            if menu_opt == "1":
                self.show_status()
            elif menu_opt == "2":
                self.borrow_book()
            elif menu_opt == "3":
                self.return_book()
            elif menu_opt == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid Option.")

if __name__ == "__main__":
    system = LibraryManagement()
    system.run()
