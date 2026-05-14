       IDENTIFICATION DIVISION.
       PROGRAM-ID. LIBRARY-MANAGEMENT.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 BOOK-DETAILS.
          05 BK-ISBN         PIC X(13).
          05 BK-TITLE        PIC X(40).
          05 BK-AUTHOR       PIC X(25).
          05 BK-AVAIL        PIC X VALUE 'Y'.
             88 IS-AVAIL     VALUE 'Y'.
             88 IS-BORROWED  VALUE 'N'.
             
       01 USER-INFO.
          05 MEMBER-ID       PIC 9(5).
          05 DAYS-BORROWED   PIC 9(3).
          
       01 CALCULATIONS.
          05 LATE-DAYS       PIC S9(3).
          05 FINE-AMOUNT     PIC 9(4)V99 VALUE ZERO.
          
       01 DISPLAY-FINE       PIC $Z,ZZ9.99.
       01 MENU-OPT           PIC 9.

       PROCEDURE DIVISION.
       MAIN-PROGRAM.
           DISPLAY "Initializing Library Book...".
           MOVE "9781234567890" TO BK-ISBN.
           MOVE "The Great Cobol Mystery" TO BK-TITLE.
           MOVE "Grace Hopper" TO BK-AUTHOR.
           MOVE 'Y' TO BK-AVAIL.
           
           PERFORM UNTIL MENU-OPT = 4
               DISPLAY " "
               DISPLAY "--- LIBRARY SYSTEM ---"
               DISPLAY "1. View Book Status"
               DISPLAY "2. Borrow Book"
               DISPLAY "3. Return Book"
               DISPLAY "4. Exit"
               DISPLAY "Select option: "
               ACCEPT MENU-OPT
               
               EVALUATE MENU-OPT
                   WHEN 1
                       PERFORM SHOW-STATUS
                   WHEN 2
                       PERFORM BORROW-BOOK
                   WHEN 3
                       PERFORM RETURN-BOOK
                   WHEN 4
                       DISPLAY "Goodbye!"
                   WHEN OTHER
                       DISPLAY "Invalid Option."
               END-EVALUATE
           END-PERFORM.
           STOP RUN.

       SHOW-STATUS.
           DISPLAY "Title:  " BK-TITLE.
           DISPLAY "ISBN:   " BK-ISBN.
           DISPLAY "Author: " BK-AUTHOR.
           IF IS-AVAIL
               DISPLAY "Status: AVAILABLE ON SHELF"
           ELSE
               DISPLAY "Status: BORROWED OUT"
           END-IF.

       BORROW-BOOK.
           IF IS-BORROWED
               DISPLAY "Sorry, this book is currently unavailable."
           ELSE
               DISPLAY "Enter Member ID: "
               ACCEPT MEMBER-ID
               MOVE 'N' TO BK-AVAIL
               DISPLAY "Book checked out to Member " MEMBER-ID
               DISPLAY "Return within 14 days to avoid fines."
           END-IF.

       RETURN-BOOK.
           IF IS-AVAIL
               DISPLAY "This book is already in the library!"
           ELSE
               DISPLAY "Enter number of days it was borrowed: "
               ACCEPT DAYS-BORROWED
               COMPUTE LATE-DAYS = DAYS-BORROWED - 14
               
               IF LATE-DAYS > 0
                   COMPUTE FINE-AMOUNT = LATE-DAYS * 0.50
                   MOVE FINE-AMOUNT TO DISPLAY-FINE
                   DISPLAY "LATE RETURN: " LATE-DAYS " days."
                   DISPLAY "Please collect fine: " DISPLAY-FINE
               ELSE
                   DISPLAY "Book returned on time. No fines."
               END-IF
               
               MOVE 'Y' TO BK-AVAIL
               DISPLAY "Book is now restocked to the shelf."
           END-IF.
