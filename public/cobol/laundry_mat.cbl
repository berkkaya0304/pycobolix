       IDENTIFICATION DIVISION.
       PROGRAM-ID. LAUNDRY-MAT.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 LAUNDRY-LOAD.
          05 WASH-LOADS      PIC 9(2).
          05 WASH-TEMP       PIC 9.
             88 COLD-WASH    VALUE 1.
             88 WARM-WASH    VALUE 2.
             88 HOT-WASH     VALUE 3.
          05 DRYER-MINS      PIC 9(3).
          05 BUY-SOAP        PIC 9(2) VALUE ZERO.

       01 FEES.
          05 WASH-RATE       PIC 9V99 VALUE 0.00.
          05 WASH-TOT        PIC 9(3)V99 VALUE ZERO.
          05 DRYER-TOT       PIC 9(3)V99 VALUE ZERO.
          05 SOAP-TOT        PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-MAT.
           DISPLAY "--- SUDS & BUBBLES COIN LAUNDRY ---".
           DISPLAY "Number of Washing Machines Needed: ".
           ACCEPT WASH-LOADS.
           DISPLAY "Wash Temp (1=Cold $3, 2=Warm $3.50, 3=Hot $4): ".
           ACCEPT WASH-TEMP.
           DISPLAY "Total Dryer Minutes ($0.25 per 5 mins): ".
           ACCEPT DRYER-MINS.
           DISPLAY "Detergent Pods to Purchase ($1.50 ea): ".
           ACCEPT BUY-SOAP.

           EVALUATE TRUE
               WHEN COLD-WASH
                   MOVE 3.00 TO WASH-RATE
               WHEN WARM-WASH
                   MOVE 3.50 TO WASH-RATE
               WHEN HOT-WASH
                   MOVE 4.00 TO WASH-RATE
               WHEN OTHER
                   MOVE 3.00 TO WASH-RATE
           END-EVALUATE.

           COMPUTE WASH-TOT = WASH-LOADS * WASH-RATE.

           COMPUTE DRYER-TOT = (DRYER-MINS / 5) * 0.25.

           COMPUTE SOAP-TOT = BUY-SOAP * 1.50.

           COMPUTE GRAND-TOT = WASH-TOT + DRYER-TOT + SOAP-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           LAUNDRY KIOSK TICKET         "
           DISPLAY "========================================"
           IF WASH-LOADS > 0
               MOVE WASH-TOT TO DISP
               DISPLAY "Washers (" WASH-LOADS "):           " DISP
           END-IF.
           
           IF DRYER-MINS > 0
               MOVE DRYER-TOT TO DISP
               DISPLAY "Dryer Time (" DRYER-MINS "m):        " DISP
           END-IF.
           
           IF BUY-SOAP > 0
               MOVE SOAP-TOT TO DISP
               DISPLAY "Detergent Pods (" BUY-SOAP "):      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL INSERT COINS:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
