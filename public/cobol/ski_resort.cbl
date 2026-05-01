       IDENTIFICATION DIVISION.
       PROGRAM-ID. SKI-RESORT.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SKIER-DATA.
          05 SKIER-NAME      PIC X(20).
          05 PASS-TYPE       PIC 9.
             88 HALF-DAY     VALUE 1.
             88 FULL-DAY     VALUE 2.
             88 MULTI-DAY    VALUE 3.
          05 RENT-GEAR       PIC X.
             88 WANTS-RENTAL VALUE 'Y'.
          05 RENT-HELMET     PIC X.
             88 WANTS-HELMET VALUE 'Y'.

       01 FEE-TOTS.
          05 LIFT-TICKET     PIC 9(3)V99 VALUE ZERO.
          05 GEAR-FEE        PIC 9(3)V99 VALUE ZERO.
          05 HELMET-FEE      PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-PASS.
           DISPLAY "--- SNOW PEAK RESORT ---".
           DISPLAY "Skier Name: ".
           ACCEPT SKIER-NAME.
           DISPLAY "Pass (1=Half Day $60, 2=Full $95, 3=3-Day $250): ".
           ACCEPT PASS-TYPE.
           DISPLAY "Rent Skis/Snowboard ($45)? (Y/N): ".
           ACCEPT RENT-GEAR.
           DISPLAY "Rent Safety Helmet ($15)? (Y/N): ".
           ACCEPT RENT-HELMET.

           EVALUATE TRUE
               WHEN HALF-DAY
                   MOVE 60.00 TO LIFT-TICKET
               WHEN FULL-DAY
                   MOVE 95.00 TO LIFT-TICKET
               WHEN MULTI-DAY
                   MOVE 250.00 TO LIFT-TICKET
               WHEN OTHER
                   MOVE 95.00 TO LIFT-TICKET
           END-EVALUATE.

           IF WANTS-RENTAL
               MOVE 45.00 TO GEAR-FEE
           END-IF.

           IF WANTS-HELMET
               MOVE 15.00 TO HELMET-FEE
           END-IF.

           COMPUTE TOTAL-COST = LIFT-TICKET + GEAR-FEE + HELMET-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           LIFT PASS ISSUED             "
           DISPLAY "========================================"
           DISPLAY "Skier: " SKIER-NAME
           DISPLAY "----------------------------------------"
           MOVE LIFT-TICKET TO DISP.
           DISPLAY "Lift Ticket Access:  " DISP.
           IF GEAR-FEE > 0
               MOVE GEAR-FEE TO DISP
               DISPLAY "Equipment Rental:    " DISP
           END-IF.
           IF HELMET-FEE > 0
               MOVE HELMET-FEE TO DISP
               DISPLAY "Helmet Rental:       " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-COST TO DISP.
           DISPLAY "TOTAL PAID:          " DISP.
           DISPLAY "  >>> SEE YOU ON THE SLOPES! <<<        "
           DISPLAY "========================================".
           STOP RUN.
