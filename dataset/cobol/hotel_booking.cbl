       IDENTIFICATION DIVISION.
       PROGRAM-ID. HOTEL-BOOKING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RESERVATION.
          05 GUEST           PIC X(25).
          05 SEASON          PIC X.
             88 PEAK-SEASON  VALUE 'P'.
             88 OFF-PEAK     VALUE 'O'.
          05 VIEW-TYPE       PIC 9.
             88 STANDARD-VW  VALUE 1.
             88 OCEAN-VW     VALUE 2.
             88 SUITE-VW     VALUE 3.
          05 NIGHTS          PIC 9(2).

       01 RATES.
          05 BASE-RATE       PIC 9(3)V99.
          05 SEASON-MULT     PIC 9V99.
          05 NIGHTLY-RATE    PIC 9(4)V99.
          05 SUBTOTAL        PIC 9(5)V99.
          05 TAXES           PIC 9(4)V99.
          05 GRAND-TOTAL     PIC 9(6)V99.

       01 DISP-C             PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "--- SEASIDE RESORT BOOKING ---".
           DISPLAY "Guest Name: ".
           ACCEPT GUEST.
           DISPLAY "Season (P=Peak, O=Off-Peak): ".
           ACCEPT SEASON.
           DISPLAY "Room View (1=Std, 2=Ocean, 3=Suite): ".
           ACCEPT VIEW-TYPE.
           DISPLAY "Number of Nights: ".
           ACCEPT NIGHTS.

           PERFORM CALCULATE-STAY.
           PERFORM PRINT-CONF.
           STOP RUN.

       CALCULATE-STAY.
           EVALUATE TRUE
               WHEN STANDARD-VW
                   MOVE 150.00 TO BASE-RATE
               WHEN OCEAN-VW
                   MOVE 250.00 TO BASE-RATE
               WHEN SUITE-VW
                   MOVE 500.00 TO BASE-RATE
               WHEN OTHER
                   MOVE 150.00 TO BASE-RATE
           END-EVALUATE.

           IF PEAK-SEASON
               MOVE 1.50 TO SEASON-MULT
           ELSE
               MOVE 1.00 TO SEASON-MULT
           END-IF.

           COMPUTE NIGHTLY-RATE = BASE-RATE * SEASON-MULT.
           COMPUTE SUBTOTAL = NIGHTLY-RATE * NIGHTS.
           COMPUTE TAXES = SUBTOTAL * 0.125.
           COMPUTE GRAND-TOTAL = SUBTOTAL + TAXES.

       PRINT-CONF.
           DISPLAY " "
           DISPLAY "===================================="
           DISPLAY "       BOOKING CONFIRMATION         "
           DISPLAY "===================================="
           DISPLAY "Guest:  " GUEST
           DISPLAY "Nights: " NIGHTS
           DISPLAY "------------------------------------"
           MOVE NIGHTLY-RATE TO DISP-C.
           DISPLAY "Est. Nightly Rate: " DISP-C.
           MOVE SUBTOTAL TO DISP-C.
           DISPLAY "Room Subtotal:     " DISP-C.
           MOVE TAXES TO DISP-C.
           DISPLAY "Taxes (12.5%):     " DISP-C.
           DISPLAY "------------------------------------"
           MOVE GRAND-TOTAL TO DISP-C.
           DISPLAY "TOTAL STAY COST:   " DISP-C.
           DISPLAY "====================================".
