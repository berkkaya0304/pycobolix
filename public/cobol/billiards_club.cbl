       IDENTIFICATION DIVISION.
       PROGRAM-ID. BILLIARDS-CLUB.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RENTAL-INFO.
          05 TABLE-NUM       PIC 9(2).
          05 HOURS-PLAYED    PIC 9(2)V9.
          05 DAY-OF-WEEK     PIC 9.
             88 WEEKDAY      VALUE 1.
             88 WEEKEND      VALUE 2.
          05 SNACKS-TAB      PIC 9(3)V99 VALUE ZERO.
          
       01 RATES-TOTS.
          05 HOURLY-RATE     PIC 9(2)V99 VALUE ZERO.
          05 TABLE-COST      PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-CHG       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-ENTRY.
           DISPLAY "--- EIGHT BALL BILLIARDS LOUNGE ---".
           DISPLAY "Table Number: ".
           ACCEPT TABLE-NUM.
           DISPLAY "Hours Played (e.g. 1.5): ".
           ACCEPT HOURS-PLAYED.
           DISPLAY "Day Rate (1=Weekday $12/h, 2=Weekend $18/h): ".
           ACCEPT DAY-OF-WEEK.
           DISPLAY "Snacks / Bar Tab Total ($): ".
           ACCEPT SNACKS-TAB.

           IF WEEKDAY
               MOVE 12.00 TO HOURLY-RATE
           ELSE
               MOVE 18.00 TO HOURLY-RATE
           END-IF.

           COMPUTE TABLE-COST = HOURS-PLAYED * HOURLY-RATE.
           COMPUTE TOTAL-CHG = TABLE-COST + SNACKS-TAB.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           TABLE TAB RECEIPT            "
           DISPLAY "========================================"
           DISPLAY "Table: " TABLE-NUM
           DISPLAY "Time:  " HOURS-PLAYED " hours"
           DISPLAY "----------------------------------------"
           MOVE HOURLY-RATE TO DISP.
           DISPLAY "Hourly Rate Applied: " DISP.
           MOVE TABLE-COST TO DISP.
           DISPLAY "Table Bill:          " DISP.
           
           IF SNACKS-TAB > 0
               MOVE SNACKS-TAB TO DISP
               DISPLAY "Lounge / Bar Tab:    " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-CHG TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
