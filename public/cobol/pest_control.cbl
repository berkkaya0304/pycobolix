       IDENTIFICATION DIVISION.
       PROGRAM-ID. PEST-CONTROL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SERVICE-ORDER.
          05 CLIENT-NAME     PIC X(20).
          05 SQ-FOOTAGE      PIC 9(5).
          05 PEST-TYPE       PIC 9.
             88 INSECTS      VALUE 1.
             88 RODENTS      VALUE 2.
             88 TERMITES     VALUE 3.
          05 SUB-MONTHLY     PIC X.
             88 MONTHLY-PLAN VALUE 'Y'.

       01 COSTS.
          05 BASE-SQFT       PIC 9V999 VALUE 0.05.
          05 AREA-CHARGE     PIC 9(4)V99 VALUE ZERO.
          05 PEST-SURCHG     PIC 9(3)V99 VALUE ZERO.
          05 GROSS-AMT       PIC 9(4)V99 VALUE ZERO.
          05 SUB-DISCOUNT    PIC 9(3)V99 VALUE ZERO.
          05 FINAL-DUE       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-CONTROL.
           DISPLAY "--- BUG BUSTERS EXTERMINATING ---".
           DISPLAY "Property Owner: ".
           ACCEPT CLIENT-NAME.
           DISPLAY "Square Footage of Property: ".
           ACCEPT SQ-FOOTAGE.
           DISPLAY "Pest (1=Insects, 2=Rodent +$50, 3=Termite +$200):".
           ACCEPT PEST-TYPE.
           DISPLAY "Enroll in Monthly Plan (20% Off)? (Y/N): ".
           ACCEPT SUB-MONTHLY.

           COMPUTE AREA-CHARGE = SQ-FOOTAGE * BASE-SQFT.

           EVALUATE TRUE
               WHEN INSECTS
                   MOVE ZERO TO PEST-SURCHG
               WHEN RODENTS
                   MOVE 50.00 TO PEST-SURCHG
               WHEN TERMITES
                   MOVE 200.00 TO PEST-SURCHG
               WHEN OTHER
                   MOVE ZERO TO PEST-SURCHG
           END-EVALUATE.

           COMPUTE GROSS-AMT = AREA-CHARGE + PEST-SURCHG.

           IF MONTHLY-PLAN
               COMPUTE SUB-DISCOUNT = GROSS-AMT * 0.20
           END-IF.

           COMPUTE FINAL-DUE = GROSS-AMT - SUB-DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           SERVICE INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Property: " CLIENT-NAME " (" SQ-FOOTAGE " sqft)"
           DISPLAY "----------------------------------------"
           MOVE AREA-CHARGE TO DISP.
           DISPLAY "Property Area Charge:" DISP.
           IF PEST-SURCHG > 0
               MOVE PEST-SURCHG TO DISP
               DISPLAY "Target Pest Surcharge: " DISP
           END-IF.
           IF MONTHLY-PLAN
               MOVE SUB-DISCOUNT TO DISP
               DISPLAY "Service Plan Disc:  -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-DUE TO DISP.
           DISPLAY "TOTAL TREATMENT:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
