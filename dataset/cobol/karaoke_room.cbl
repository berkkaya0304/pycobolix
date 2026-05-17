       IDENTIFICATION DIVISION.
       PROGRAM-ID. KARAOKE-ROOM.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 EVENT-RES.
          05 GUEST-NAME      PIC X(20).
          05 ROOM-SIZE       PIC 9.
             88 SMALL-ROOM   VALUE 1.
             88 LARGE-ROOM   VALUE 2.
             88 PARTY-SUITE  VALUE 3.
          05 RENT-HOURS      PIC 9(2).
          05 FOOD-DRINK-TAB  PIC 9(3)V99 VALUE ZERO.

       01 COSTS.
          05 HOURLY-RATE     PIC 9(3)V99 VALUE ZERO.
          05 ROOM-TOT        PIC 9(4)V99 VALUE ZERO.
          05 SERV-CHG        PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BOOKING.
           DISPLAY "--- NEON NIGHTS KARAOKE ---".
           DISPLAY "Host Name: ".
           ACCEPT GUEST-NAME.
           DISPLAY "Room (1=Small $30/hr, 2=Large $60/h, 3=Suite $100): ".
           ACCEPT ROOM-SIZE.
           DISPLAY "Time Reserved (Hours): ".
           ACCEPT RENT-HOURS.
           DISPLAY "Food & Drink Tab Total ($): ".
           ACCEPT FOOD-DRINK-TAB.

           EVALUATE TRUE
               WHEN SMALL-ROOM
                   MOVE 30.00 TO HOURLY-RATE
               WHEN LARGE-ROOM
                   MOVE 60.00 TO HOURLY-RATE
               WHEN PARTY-SUITE
                   MOVE 100.00 TO HOURLY-RATE
               WHEN OTHER
                   MOVE 30.00 TO HOURLY-RATE
           END-EVALUATE.

           COMPUTE ROOM-TOT = HOURLY-RATE * RENT-HOURS.

           COMPUTE SERV-CHG = FOOD-DRINK-TAB * 0.18.

           COMPUTE GRAND-TOT = ROOM-TOT + FOOD-DRINK-TAB + SERV-CHG.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          KARAOKE ROOM INVOICE          "
           DISPLAY "========================================"
           DISPLAY "Host: " GUEST-NAME
           DISPLAY "----------------------------------------"
           MOVE ROOM-TOT TO DISP.
           DISPLAY "Room Rental (" RENT-HOURS "h):      " DISP.
           
           IF FOOD-DRINK-TAB > 0
               MOVE FOOD-DRINK-TAB TO DISP
               DISPLAY "Food & Drink Tab:      " DISP
               MOVE SERV-CHG TO DISP
               DISPLAY "Auto Gratuity (18%):   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
