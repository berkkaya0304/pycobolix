       IDENTIFICATION DIVISION.
       PROGRAM-ID. TAXI-FARE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RIDE-DATA.
          05 PASSENGER-NAME  PIC X(20).
          05 DISTANCE-MILES  PIC 9(3)V9.
          05 WAIT-MINUTES    PIC 9(3) VALUE ZERO.
          05 NIGHT-SURCHARGE PIC X.
             88 IS-NIGHT     VALUE 'Y'.

       01 RATES-FEES.
          05 BASE-DROP       PIC 9(2)V99 VALUE 3.50.
          05 MILE-RATE       PIC 9(2)V99 VALUE 2.75.
          05 WAIT-RATE       PIC 9(2)V99 VALUE 0.50.
          05 NIGHT-FEE       PIC 9(2)V99 VALUE 2.00.

       01 CALCS.
          05 DISTANCE-FEE    PIC 9(4)V99 VALUE ZERO.
          05 TIME-FEE        PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-FARE      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-METER.
           DISPLAY "--- CITY CAB METER ---".
           DISPLAY "Passenger Name: ".
           ACCEPT PASSENGER-NAME.
           DISPLAY "Distance Traveled (Miles): ".
           ACCEPT DISTANCE-MILES.
           DISPLAY "Traffic/Wait Time (Minutes): ".
           ACCEPT WAIT-MINUTES.
           DISPLAY "Is it between 8PM and 6AM? (Y/N): ".
           ACCEPT NIGHT-SURCHARGE.

           COMPUTE DISTANCE-FEE = DISTANCE-MILES * MILE-RATE.
           COMPUTE TIME-FEE = WAIT-MINUTES * WAIT-RATE.

           COMPUTE TOTAL-FARE = BASE-DROP + DISTANCE-FEE + TIME-FEE.

           IF IS-NIGHT
               ADD NIGHT-FEE TO TOTAL-FARE
           END-IF.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             TAXI RECEIPT               "
           DISPLAY "========================================"
           DISPLAY "Passenger: " PASSENGER-NAME
           DISPLAY "Distance:  " DISTANCE-MILES " mi"
           DISPLAY "----------------------------------------"
           MOVE BASE-DROP TO DISP.
           DISPLAY "Initial Drop:       " DISP.
           MOVE DISTANCE-FEE TO DISP.
           DISPLAY "Mileage Fare:       " DISP.
           
           IF TIME-FEE > 0
               MOVE TIME-FEE TO DISP
               DISPLAY "Wait/Idle Time:     " DISP
           END-IF.
           
           IF IS-NIGHT
               MOVE NIGHT-FEE TO DISP
               DISPLAY "Night Surcharge:    " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-FARE TO DISP.
           DISPLAY "TOTAL FARE DUE:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
