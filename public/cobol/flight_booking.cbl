       IDENTIFICATION DIVISION.
       PROGRAM-ID. FLIGHT-BOOKING.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PASSENGER-INFO.
          05 PASSENGER-NAME  PIC X(30).
          05 DESTINATION     PIC 9.
             88 DEST-NY      VALUE 1.
             88 DEST-LON     VALUE 2.
             88 DEST-TOK     VALUE 3.
          05 TICKET-CLASS    PIC X.
             88 CLASS-ECO    VALUE 'E'.
             88 CLASS-BUS    VALUE 'B'.
             88 CLASS-1ST    VALUE 'F'.
          05 LUGGAGE-COUNT   PIC 9(2).

       01 CHARGES.
          05 BASE-FARE       PIC 9(4)V99 VALUE ZERO.
          05 CLASS-SURCHARGE PIC 9(4)V99 VALUE ZERO.
          05 LUGGAGE-FEE     PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(5)V99 VALUE ZERO.
          05 TAX-AMOUNT      PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(6)V99 VALUE ZERO.

       01 FMT-VAL            PIC $ZZ,ZZ9.99.
       01 CONTINUE-PROG      PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "--- AIRLINE RESERVATION ---".
           PERFORM UNTIL CONTINUE-PROG = 'N' OR 'n'
               PERFORM GET-DETAILS
               PERFORM CALCULATE-FARE
               PERFORM PRINT-TICKET
               DISPLAY "Book another flight? (Y/N): "
               ACCEPT CONTINUE-PROG
           END-PERFORM.
           DISPLAY "System Terminated.".
           STOP RUN.

       GET-DETAILS.
           DISPLAY "Passenger Name: ".
           ACCEPT PASSENGER-NAME.
           DISPLAY "Destinations: 1=New York($300), 2=London($600), "
                   "3=Tokyo($900)".
           DISPLAY "Select Destination (1/2/3): ".
           ACCEPT DESTINATION.
           DISPLAY "Class (E=Economy, B=Business +50%, F=First +100%): "
           ACCEPT TICKET-CLASS.
           DISPLAY "Number of checked bags ($50 each): ".
           ACCEPT LUGGAGE-COUNT.

       CALCULATE-FARE.
           EVALUATE TRUE
               WHEN DEST-NY
                   MOVE 300.00 TO BASE-FARE
               WHEN DEST-LON
                   MOVE 600.00 TO BASE-FARE
               WHEN DEST-TOK
                   MOVE 900.00 TO BASE-FARE
               WHEN OTHER
                   MOVE 300.00 TO BASE-FARE
                   DISPLAY "Invalid destination, defaulted to NY."
           END-EVALUATE.

           EVALUATE TRUE
               WHEN CLASS-ECO
                   MOVE ZERO TO CLASS-SURCHARGE
               WHEN CLASS-BUS
                   COMPUTE CLASS-SURCHARGE = BASE-FARE * 0.50
               WHEN CLASS-1ST
                   COMPUTE CLASS-SURCHARGE = BASE-FARE * 1.00
               WHEN OTHER
                   MOVE ZERO TO CLASS-SURCHARGE
           END-EVALUATE.

           COMPUTE LUGGAGE-FEE = LUGGAGE-COUNT * 50.00.
           COMPUTE TOTAL-COST = BASE-FARE + CLASS-SURCHARGE + 
                                LUGGAGE-FEE.
           COMPUTE TAX-AMOUNT = TOTAL-COST * 0.10.
           COMPUTE GRAND-TOTAL = TOTAL-COST + TAX-AMOUNT.

       PRINT-TICKET.
           DISPLAY " "
           DISPLAY "=============================================".
           DISPLAY "               BOARDING PASS                 ".
           DISPLAY "=============================================".
           DISPLAY "Name: " PASSENGER-NAME.
           
           MOVE BASE-FARE TO FMT-VAL.
           DISPLAY "Base Fare:       " FMT-VAL.
           IF CLASS-SURCHARGE > 0
               MOVE CLASS-SURCHARGE TO FMT-VAL
               DISPLAY "Class Upgrade:   " FMT-VAL
           END-IF.
           IF LUGGAGE-FEE > 0
               MOVE LUGGAGE-FEE TO FMT-VAL
               DISPLAY "Baggage Fees:    " FMT-VAL
           END-IF.
           DISPLAY "---------------------------------------------".
           MOVE TAX-AMOUNT TO FMT-VAL.
           DISPLAY "Taxes (10%):     " FMT-VAL.
           MOVE GRAND-TOTAL TO FMT-VAL.
           DISPLAY "TOTAL FARE:      " FMT-VAL.
           DISPLAY "=============================================".
