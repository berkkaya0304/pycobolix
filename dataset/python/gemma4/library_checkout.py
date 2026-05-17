import sys

class LibraryBook:
    def __init__(self):
        self.isbn = "9781234567890"
        self.title = "The Great Cobol Mystery"
        self.author = "Grace Hopper"
        self.is_available = True

    def show_status(self):
        print(f"Title:  {self.title}")
        print(f"ISBN:   {self.isbn}")
        print(f"Author: {self.author}")
        status = "AVAILABLE ON SHELF" if self.is_available else "BORROWED OUT"
        print(f"Status: {status}")

    def borrow_book(self):
        if not self.is_available:
            print("Sorry, this book is currently unavailable.")
        else:
            try:
                member_id = input("Enter Member ID: ")
                self.is_available = False
                print(f"Book checked out to Member {member_id}")
                print("Return within 14 days to avoid fines.")
            except EOFError:
                sys.exit(0)

    def return_book(self):
        if self.is_available:
            print("This book is already in the library!")
        else:
            try:
                days_borrowed = int(input("Enter number of days it was borrowed: "))
                late_days = days_borrowed - 14
                
                if late_days > 0:
                    fine_amount = late_days * 0.50
                    print(f"LATE RETURN: {late_days} days.")
                    print(f"Please collect fine: ${fine_amount:,.2f}")
                else:
                    print("Book returned on time. No fines.")
                
                self.is_available = True
                print("Book is now restocked to the shelf.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for days.")
            except EOFError:
                sys.exit(0)

def main():
    print("Initializing Library Book...")
    book = LibraryBook()
    
    while True:
        print("\n--- LIBRARY SYSTEM ---")
        print("1. View Book Status")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        try:
            option = input("Select option: ")
            
            if option == '1':
                book.show_status()
            elif option == '2':
                book.borrow_book()
            elif option == '3':
                book.return_book()
            elif option == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid Option.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
