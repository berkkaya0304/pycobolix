       IDENTIFICATION DIVISION.
       PROGRAM-ID. WEDDING-CATERING.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 EVENT-INFO.
          05 COUPLE-NAME     PIC X(30).
          05 GUEST-COUNT     PIC 9(3).
          05 MENU-TIER       PIC 9.
             88 BUFFET       VALUE 1.
             88 PLATED-STD   VALUE 2.
             88 PLATED-PREM  VALUE 3.
          05 OPEN-BAR        PIC X.
             88 WANTS-BAR    VALUE 'Y'.

       01 QUOTES.
          05 COST-PER-HEAD   PIC 9(3)V99 VALUE ZERO.
          05 FOOD-TOT        PIC 9(5)V99 VALUE ZERO.
          05 BAR-COST        PIC 9(5)V99 VALUE ZERO.
          05 GRATUITY        PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(6)V99 VALUE ZERO.

       01 DISP               PIC $ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       QUOTE-CREATE.
           DISPLAY "--- ELEGANCE EVENT CATERING ---".
           DISPLAY "Couple's Names: ".
           ACCEPT COUPLE-NAME.
           DISPLAY "Expected Guest Count: ".
           ACCEPT GUEST-COUNT.
           DISPLAY "Menu (1=Buffet $35, 2=Standard $50, 3=Prem $85): ".
           ACCEPT MENU-TIER.
           DISPLAY "Add Full Open Bar ($30 per head)? (Y/N): ".
           ACCEPT OPEN-BAR.

           EVALUATE TRUE
               WHEN BUFFET
                   MOVE 35.00 TO COST-PER-HEAD
               WHEN PLATED-STD
                   MOVE 50.00 TO COST-PER-HEAD
               WHEN PLATED-PREM
                   MOVE 85.00 TO COST-PER-HEAD
               WHEN OTHER
                   MOVE 50.00 TO COST-PER-HEAD
           END-EVALUATE.

           COMPUTE FOOD-TOT = GUEST-COUNT * COST-PER-HEAD.

           IF WANTS-BAR
               COMPUTE BAR-COST = GUEST-COUNT * 30.00
           END-IF.

           COMPUTE GRATUITY = (FOOD-TOT + BAR-COST) * 0.20.

           COMPUTE GRAND-TOTAL = FOOD-TOT + BAR-COST + GRATUITY.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            CATERING ESTIMATE           "
           DISPLAY "========================================"
           DISPLAY "Event: The " COUPLE-NAME " Wedding"
           DISPLAY "Guests Expected: " GUEST-COUNT
           DISPLAY "----------------------------------------"
           MOVE FOOD-TOT TO DISP.
           DISPLAY "Food & Dining Cost:  " DISP.
           IF BAR-COST > 0
               MOVE BAR-COST TO DISP
               DISPLAY "Open Bar Setup:      " DISP
           END-IF.
           MOVE GRATUITY TO DISP.
           DISPLAY "Staffing/Gratuity(20%) " DISP.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOTAL TO DISP.
           DISPLAY "ESTIMATED TOTAL:     " DISP.
           DISPLAY "========================================".
           STOP RUN.
