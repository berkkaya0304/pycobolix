       IDENTIFICATION DIVISION.
       PROGRAM-ID. PARKING-GARAGE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TICKET-INFO.
          05 TICKET-NUM      PIC 9(6).
          05 HOURS-PARKED    PIC 9(2)V99.
          05 VALET-SERVICE   PIC X.
             88 IS-VALET     VALUE 'Y'.
          05 LOST-TICKET     PIC X.
             88 IS-LOST      VALUE 'Y'.

       01 FEES.
          05 HOURLY-RATE     PIC 9(2)V99 VALUE 4.50.
          05 DAILY-MAX       PIC 9(2)V99 VALUE 25.00.
          05 VALET-FLAT      PIC 9(2)V99 VALUE 15.00.
          05 LOST-PENALTY    PIC 9(2)V99 VALUE 40.00.
          
       01 CALCULATIONS.
          05 TIME-CHARGE     PIC 9(4)V99.
          05 EXTRA-FEE       PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-DUE       PIC 9(5)V99.

       01 DISP-AMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-GARAGE.
           DISPLAY "--- CITY CENTER PARKING GARAGE ---".
           DISPLAY "Ticket Number: ".
           ACCEPT TICKET-NUM.
           DISPLAY "Hours Parked (e.g. 3.5): ".
           ACCEPT HOURS-PARKED.
           DISPLAY "Valet Service used? (Y/N): ".
           ACCEPT VALET-SERVICE.
           DISPLAY "Is ticket lost? (Y/N): ".
           ACCEPT LOST-TICKET.

           PERFORM COMPUTE-FARE.
           PERFORM ISSUE-EXIT-PASS.
           STOP RUN.

       COMPUTE-FARE.
           IF IS-LOST
               MOVE DAILY-MAX TO TIME-CHARGE
               MOVE LOST-PENALTY TO EXTRA-FEE
           ELSE
               COMPUTE TIME-CHARGE = HOURS-PARKED * HOURLY-RATE
               IF TIME-CHARGE > DAILY-MAX
                   MOVE DAILY-MAX TO TIME-CHARGE
               END-IF
           END-IF.

           IF IS-VALET
               ADD VALET-FLAT TO EXTRA-FEE
           END-IF.

           COMPUTE TOTAL-DUE = TIME-CHARGE + EXTRA-FEE.

       ISSUE-EXIT-PASS.
           DISPLAY " "
           DISPLAY "==================================="
           DISPLAY "        PARKING EXIT TICKET        "
           DISPLAY "==================================="
           DISPLAY "Ticket #: " TICKET-NUM
           DISPLAY "Time In Garage: " HOURS-PARKED " hours"
           DISPLAY "-----------------------------------"
           MOVE TIME-CHARGE TO DISP-AMT.
           DISPLAY "Parking Fee:     " DISP-AMT.
           
           IF EXTRA-FEE > 0
               MOVE EXTRA-FEE TO DISP-AMT
               DISPLAY "Additional Fees: " DISP-AMT
           END-IF.
           DISPLAY "-----------------------------------"
           MOVE TOTAL-DUE TO DISP-AMT.
           DISPLAY "TOTAL TO PAY:    " DISP-AMT.
           DISPLAY "===================================".
