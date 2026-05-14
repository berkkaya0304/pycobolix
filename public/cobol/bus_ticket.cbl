       IDENTIFICATION DIVISION.
       PROGRAM-ID. BUS-TICKET.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TRAVEL-INFO.
          05 PASSENGER       PIC X(25).
          05 ROUTE-ID        PIC 9(2).
          05 AGE             PIC 9(3).
          05 EXTRA-BAGS      PIC 9(2) VALUE ZERO.

       01 CHARGES.
          05 BASE-FARE       PIC 9(3)V99 VALUE ZERO.
          05 BAGGAGE-FEE     PIC 9(2)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(3)V99 VALUE ZERO.
          05 FINAL-FARE      PIC 9(4)V99 VALUE ZERO.

       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "--- INTERSTATE EXPRESS TICKETING ---".
           DISPLAY "Passenger Name: ".
           ACCEPT PASSENGER.
           DISPLAY "Route (1=NY-DC $35, 2=NY-BOS $40, 3=NY-CHI $55): ".
           ACCEPT ROUTE-ID.
           DISPLAY "Passenger Age: ".
           ACCEPT AGE.
           DISPLAY "Extra Luggage (First bag free, $15 after): ".
           ACCEPT EXTRA-BAGS.

           EVALUATE ROUTE-ID
               WHEN 1
                   MOVE 35.00 TO BASE-FARE
               WHEN 2
                   MOVE 40.00 TO BASE-FARE
               WHEN 3
                   MOVE 55.00 TO BASE-FARE
               WHEN OTHER
                   MOVE 35.00 TO BASE-FARE
                   DISPLAY "Unknown Route - Default NY-DC."
           END-EVALUATE.

           IF EXTRA-BAGS > 0
               COMPUTE BAGGAGE-FEE = EXTRA-BAGS * 15.00
           END-IF.

           IF AGE >= 65
               COMPUTE DISCOUNT = BASE-FARE * 0.15
           ELSE IF AGE <= 12
               COMPUTE DISCOUNT = BASE-FARE * 0.25
           ELSE
               MOVE ZERO TO DISCOUNT
           END-IF.

           COMPUTE FINAL-FARE = BASE-FARE + BAGGAGE-FEE - DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          BOARDING PASS                 "
           DISPLAY "========================================"
           DISPLAY "Passenger: " PASSENGER " (Age: " AGE ")"
           DISPLAY "----------------------------------------"
           MOVE BASE-FARE TO DISP-FMT.
           DISPLAY "Route Base Fare:    " DISP-FMT.
           
           IF BAGGAGE-FEE > 0
               MOVE BAGGAGE-FEE TO DISP-FMT
               DISPLAY "Extra Baggage Fee:  " DISP-FMT
           END-IF.
           
           IF DISCOUNT > 0
               MOVE DISCOUNT TO DISP-FMT
               DISPLAY "Age Discount:      -" DISP-FMT
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-FARE TO DISP-FMT.
           DISPLAY "TOTAL TICKET PRICE: " DISP-FMT.
           DISPLAY "========================================".
           STOP RUN.
