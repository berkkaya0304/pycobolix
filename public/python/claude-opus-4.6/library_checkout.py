"""
Library Management System
Converted from COBOL (library_checkout.cbl) to Python
"""


def main():
    print("Initializing Library Book...")
    bk_isbn = "9781234567890"
    bk_title = "The Great Cobol Mystery"
    bk_author = "Grace Hopper"
    bk_avail = True

    menu_opt = 0
    while menu_opt != 4:
        print()
        print("--- LIBRARY SYSTEM ---")
        print("1. View Book Status")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        menu_opt = int(input("Select option: "))

        if menu_opt == 1:
            print(f"Title:  {bk_title}")
            print(f"ISBN:   {bk_isbn}")
            print(f"Author: {bk_author}")
            if bk_avail:
                print("Status: AVAILABLE ON SHELF")
            else:
                print("Status: BORROWED OUT")

        elif menu_opt == 2:
            if not bk_avail:
                print("Sorry, this book is currently unavailable.")
            else:
                member_id = input("Enter Member ID: ")
                bk_avail = False
                print(f"Book checked out to Member {member_id}")
                print("Return within 14 days to avoid fines.")

        elif menu_opt == 3:
            if bk_avail:
                print("This book is already in the library!")
            else:
                days_borrowed = int(input("Enter number of days it was borrowed: "))
                late_days = days_borrowed - 14
                if late_days > 0:
                    fine_amount = late_days * 0.50
                    print(f"LATE RETURN: {late_days} days.")
                    print(f"Please collect fine: ${fine_amount:>9,.2f}")
                else:
                    print("Book returned on time. No fines.")
                bk_avail = True
                print("Book is now restocked to the shelf.")

        elif menu_opt == 4:
            print("Goodbye!")

        else:
            print("Invalid Option.")


if __name__ == "__main__":
    main()
