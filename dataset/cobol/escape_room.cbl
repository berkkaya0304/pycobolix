       IDENTIFICATION DIVISION.
       PROGRAM-ID. ESCAPE-ROOM.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 BOOK-INFO.
          05 GROUP-NAME      PIC X(20).
          05 NUM-PLAYERS     PIC 9(2).
          05 DIFFICULTY      PIC 9.
             88 EASY-ROOM    VALUE 1.
             88 MED-ROOM     VALUE 2.
             88 HARD-ROOM    VALUE 3.
          05 IS-WEEKEND      PIC X.
             88 WEEKEND      VALUE 'Y'.

       01 COSTS.
          05 BASE-TICKET     PIC 9(2)V99 VALUE 25.00.
          05 DIFF-SURCHARGE  PIC 9(2)V99 VALUE ZERO.
          05 TICKET-PRICE    PIC 9(2)V99.
          05 ROOM-TOT        PIC 9(4)V99.
          05 WEEKEND-FEE     PIC 9(2)V99 VALUE ZERO.
          05 FINAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "--- ENIGMA ESCAPE ROOMS ---".
           DISPLAY "Group/Team Name: ".
           ACCEPT GROUP-NAME.
           DISPLAY "Number of Players: ".
           ACCEPT NUM-PLAYERS.
           DISPLAY "Room Difficulty (1=Easy, 2=Med, 3=Hard +$5): ".
           ACCEPT DIFFICULTY.
           DISPLAY "Is booking on Weekend (Fri-Sun)? (Y/N): ".
           ACCEPT IS-WEEKEND.

           IF HARD-ROOM
               MOVE 5.00 TO DIFF-SURCHARGE
           ELSE
               MOVE ZERO TO DIFF-SURCHARGE
           END-IF.

           COMPUTE TICKET-PRICE = BASE-TICKET + DIFF-SURCHARGE.
           COMPUTE ROOM-TOT = NUM-PLAYERS * TICKET-PRICE.

           IF WEEKEND
               MOVE 20.00 TO WEEKEND-FEE
           END-IF.

           COMPUTE FINAL-BILL = ROOM-TOT + WEEKEND-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          BOOKING CONFIRMATION          "
           DISPLAY "========================================"
           DISPLAY "Team: " GROUP-NAME " (" NUM-PLAYERS " players)"
           DISPLAY "----------------------------------------"
           MOVE TICKET-PRICE TO DISP.
           DISPLAY "Price Per Ticket:    " DISP.
           MOVE ROOM-TOT TO DISP.
           DISPLAY "Base Room Charge:    " DISP.
           
           IF WEEKEND-FEE > 0
               MOVE WEEKEND-FEE TO DISP
               DISPLAY "Weekend Premium:     " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-BILL TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
