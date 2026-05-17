       IDENTIFICATION DIVISION.
       PROGRAM-ID. THEME-PARK.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TICKET-INFO.
          05 GUEST-NAME      PIC X(20).
          05 ADULT-TKTS      PIC 9(2) VALUE ZERO.
          05 CHILD-TKTS      PIC 9(2) VALUE ZERO.
          
       01 UPGRADES.
          05 FAST-PASS       PIC X.
             88 WANTS-FAST   VALUE 'Y'.
          05 MEAL-PLAN       PIC X.
             88 WANTS-MEAL   VALUE 'Y'.

       01 PRICING.
          05 ADULT-FARE      PIC 9(3)V99 VALUE 85.00.
          05 CHILD-FARE      PIC 9(3)V99 VALUE 60.00.
          05 FP-COST         PIC 9(2)V99 VALUE 45.00.
          05 MP-COST         PIC 9(2)V99 VALUE 30.00.
          
       01 TOTALS.
          05 TKT-TOTAL       PIC 9(4)V99.
          05 UPGRADE-TOTAL   PIC 9(4)V99.
          05 GRAND-TOTAL     PIC 9(5)V99.
          05 HEAD-COUNT      PIC 9(3).

       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-PROGRAM.
           DISPLAY "--- ADVENTURE WORLD TICKETS ---".
           DISPLAY "Lead Guest Name: ".
           ACCEPT GUEST-NAME.
           DISPLAY "Adult Tickets ($85 each): ".
           ACCEPT ADULT-TKTS.
           DISPLAY "Child Tickets ($60 each): ".
           ACCEPT CHILD-TKTS.
           DISPLAY "Add Fast-Pass ($45/person)? (Y/N): ".
           ACCEPT FAST-PASS.
           DISPLAY "Add All-Day Dining ($30/person)? (Y/N): ".
           ACCEPT MEAL-PLAN.

           PERFORM CALCULATE-FEES.
           PERFORM PRINT-PASS.
           STOP RUN.

       CALCULATE-FEES.
           COMPUTE TKT-TOTAL = (ADULT-TKTS * ADULT-FARE) 
                             + (CHILD-TKTS * CHILD-FARE).
           COMPUTE HEAD-COUNT = ADULT-TKTS + CHILD-TKTS.
           
           MOVE ZERO TO UPGRADE-TOTAL.
           IF WANTS-FAST
               COMPUTE UPGRADE-TOTAL = UPGRADE-TOTAL 
                                     + (HEAD-COUNT * FP-COST)
           END-IF.
           
           IF WANTS-MEAL
               COMPUTE UPGRADE-TOTAL = UPGRADE-TOTAL 
                                     + (HEAD-COUNT * MP-COST)
           END-IF.

           COMPUTE GRAND-TOTAL = TKT-TOTAL + UPGRADE-TOTAL.

       PRINT-PASS.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "       ADVENTURE WORLD RECEIPT          "
           DISPLAY "========================================"
           DISPLAY "Guest: " GUEST-NAME
           DISPLAY "Headcount: " HEAD-COUNT " people"
           DISPLAY "----------------------------------------"
           IF ADULT-TKTS > 0
               MOVE ADULT-TKTS TO DISP-FMT
               DISPLAY "Adult Tickets (" ADULT-TKTS "):    " DISP-FMT
           END-IF.
           IF CHILD-TKTS > 0
               MOVE CHILD-TKTS TO DISP-FMT
               DISPLAY "Child Tickets (" CHILD-TKTS "):    " DISP-FMT
           END-IF.
           MOVE TKT-TOTAL TO DISP-FMT.
           DISPLAY "Base Ticket Total:    " DISP-FMT.
           DISPLAY "----------------------------------------"
           IF UPGRADE-TOTAL > 0
               MOVE UPGRADE-TOTAL TO DISP-FMT
               DISPLAY "Add-ons (FP/Dining):  " DISP-FMT
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOTAL TO DISP-FMT.
           DISPLAY "TOTAL PAYABLE:        " DISP-FMT.
           DISPLAY "========================================".
