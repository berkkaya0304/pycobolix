       IDENTIFICATION DIVISION.
       PROGRAM-ID. SURF-SHOP.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SURF-CART.
          05 SURFER-NAME     PIC X(20).
          05 BOARD-RENTALS   PIC 9(2) VALUE ZERO.
          05 WETSUITS        PIC 9(2) VALUE ZERO.
          05 HOURS-RENT      PIC 9(2) VALUE 1.
          05 LESSON-ADD      PIC X.
             88 WANTS-LESSON VALUE 'Y'.

       01 COSTS.
          05 BOARD-RT        PIC 9(2)V99 VALUE 15.00.
          05 SUIT-RT         PIC 9(2)V99 VALUE 10.00.
          05 LESSON-FEE      PIC 9(2)V99 VALUE 45.00.
          
          05 B-TOT           PIC 9(4)V99 VALUE ZERO.
          05 S-TOT           PIC 9(4)V99 VALUE ZERO.
          05 L-TOT           PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-SHACK.
           DISPLAY "--- BIG KAHUNA SURF SHACK ---".
           DISPLAY "Name: ".
           ACCEPT SURFER-NAME.
           DISPLAY "Surfboards to Rent ($15/hr): ".
           ACCEPT BOARD-RENTALS.
           DISPLAY "Wetsuits to Rent ($10/hr): ".
           ACCEPT WETSUITS.
           DISPLAY "Rental Duration (Hours): ".
           ACCEPT HOURS-RENT.
           DISPLAY "Add 1-Hour Beginner Lesson ($45)? (Y/N): ".
           ACCEPT LESSON-ADD.

           COMPUTE B-TOT = (BOARD-RENTALS * BOARD-RT) * HOURS-RENT.
           COMPUTE S-TOT = (WETSUITS * SUIT-RT) * HOURS-RENT.

           IF WANTS-LESSON
               MOVE LESSON-FEE TO L-TOT
           END-IF.

           COMPUTE GRAND-TOT = B-TOT + S-TOT + L-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             SURF RENTALS               "
           DISPLAY "========================================"
           DISPLAY "Cowabunga, " SURFER-NAME "!"
           DISPLAY "Renting for " HOURS-RENT " hours."
           DISPLAY "----------------------------------------"
           IF BOARD-RENTALS > 0
               MOVE B-TOT TO DISP
               DISPLAY "Surfboards (" BOARD-RENTALS "):       " DISP
           END-IF.
           IF WETSUITS > 0
               MOVE S-TOT TO DISP
               DISPLAY "Wetsuits (" WETSUITS "):         " DISP
           END-IF.
           IF WANTS-LESSON
               MOVE L-TOT TO DISP
               DISPLAY "Beginner Lesson:      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL WAVES COST:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
