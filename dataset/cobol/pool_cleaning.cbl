       IDENTIFICATION DIVISION.
       PROGRAM-ID. POOL-CLEANING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ROUTE-JOB.
          05 HOMEOWNER       PIC X(20).
          05 POOL-TYPE       PIC 9.
             88 ABOVE-GROUND VALUE 1.
             88 IN-GROUND    VALUE 2.
          05 SALT-WATER      PIC X.
             88 IS-SALT      VALUE 'Y'.
          05 FILTER-CLEAN    PIC X.
             88 WANTS-FILTER VALUE 'Y'.

       01 FEES.
          05 BASE-CLEAN      PIC 9(2)V99 VALUE ZERO.
          05 CHEM-CHARGE     PIC 9(2)V99 VALUE 20.00.
          05 FILTER-CHG      PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(3)V99 VALUE ZERO.

       01 DISP               PIC $ZZ9.99.

       PROCEDURE DIVISION.
       APP-MAIN.
           DISPLAY "--- CRYSTAL CLEAR POOL SERVICE ---".
           DISPLAY "Client: ".
           ACCEPT HOMEOWNER.
           DISPLAY "Pool (1=Above Ground $50, 2=In Ground $80): ".
           ACCEPT POOL-TYPE.
           DISPLAY "Is it a Salt Water Pool (lower chem fee)? (Y/N): ".
           ACCEPT SALT-WATER.
           DISPLAY "Add Filter Dismantle & Scrub ($45)? (Y/N): ".
           ACCEPT FILTER-CLEAN.

           EVALUATE TRUE
               WHEN ABOVE-GROUND
                   MOVE 50.00 TO BASE-CLEAN
               WHEN IN-GROUND
                   MOVE 80.00 TO BASE-CLEAN
               WHEN OTHER
                   MOVE 50.00 TO BASE-CLEAN
           END-EVALUATE.

           IF IS-SALT
               MOVE 10.00 TO CHEM-CHARGE
           ELSE
               MOVE 20.00 TO CHEM-CHARGE
           END-IF.

           IF WANTS-FILTER
               MOVE 45.00 TO FILTER-CHG
           END-IF.

           COMPUTE TOTAL-BILL = BASE-CLEAN + CHEM-CHARGE + FILTER-CHG.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          POOL SERVICE RECIEPT          "
           DISPLAY "========================================"
           DISPLAY "Home: " HOMEOWNER
           DISPLAY "----------------------------------------"
           MOVE BASE-CLEAN TO DISP.
           DISPLAY "Base Cleaning:       " DISP.
           MOVE CHEM-CHARGE TO DISP.
           DISPLAY "Chemicals Balancing: " DISP.
           
           IF WANTS-FILTER
               MOVE FILTER-CHG TO DISP
               DISPLAY "Filter Deep Clean:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-BILL TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
