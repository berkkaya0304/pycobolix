       IDENTIFICATION DIVISION.
       PROGRAM-ID. INTERNET-CAFE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 USAGE-DATA.
          05 PC-NUMBER       PIC 9(2).
          05 HOURS-USED      PIC 9(2)V9.
          05 PAGES-PRINTED   PIC 9(3) VALUE ZERO.
          05 SNACKS-BOUGHT   PIC 9(2) VALUE ZERO.

       01 RATES.
          05 HOURLY-RATE     PIC 9(1)V99 VALUE 4.50.
          05 PRINT-RATE      PIC 9(1)V99 VALUE 0.15.
          05 SNACK-PRICE     PIC 9(1)V99 VALUE 2.00.

       01 CALCS.
          05 PC-COST         PIC 9(3)V99 VALUE ZERO.
          05 PRINT-COST      PIC 9(3)V99 VALUE ZERO.
          05 SNACK-COST      PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-CAFE.
           DISPLAY "--- CYBER NET CAFE BILLING ---".
           DISPLAY "PC Station Number: ".
           ACCEPT PC-NUMBER.
           DISPLAY "Hours Logged (e.g., 2.5): ".
           ACCEPT HOURS-USED.
           DISPLAY "Pages Printed (Black & White): ".
           ACCEPT PAGES-PRINTED.
           DISPLAY "Number of Snacks/Drinks: ".
           ACCEPT SNACKS-BOUGHT.

           COMPUTE PC-COST = HOURS-USED * HOURLY-RATE.
           COMPUTE PRINT-COST = PAGES-PRINTED * PRINT-RATE.
           COMPUTE SNACK-COST = SNACKS-BOUGHT * SNACK-PRICE.

           COMPUTE TOTAL-BILL = PC-COST + PRINT-COST + SNACK-COST.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           CAFE INVOICE                 "
           DISPLAY "========================================"
           DISPLAY "Station: PC-" PC-NUMBER
           DISPLAY "----------------------------------------"
           MOVE PC-COST TO DISP.
           DISPLAY "Internet Time (" HOURS-USED " hrs): " DISP.
           
           IF PAGES-PRINTED > 0
               MOVE PRINT-COST TO DISP
               DISPLAY "Printing (" PAGES-PRINTED " pgs):   " DISP
           END-IF.
           
           IF SNACKS-BOUGHT > 0
               MOVE SNACK-COST TO DISP
               DISPLAY "Snacks & Drinks:      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-BILL TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
