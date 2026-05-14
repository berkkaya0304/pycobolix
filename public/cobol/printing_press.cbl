       IDENTIFICATION DIVISION.
       PROGRAM-ID. PRINTING-PRESS.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PRINT-ORDER.
          05 BUSINESS-NAME   PIC X(25).
          05 FLYER-QTY       PIC 9(5) VALUE ZERO.
          05 BCARD-QTY       PIC 9(5) VALUE ZERO.
          05 COLOR-INK       PIC X.
             88 FULL-COLOR   VALUE 'Y'.
          05 RUSH-PRINT      PIC X.
             88 IS-RUSH      VALUE 'Y'.

       01 RATES-TOTS.
          05 FLYER-RT        PIC 9V999 VALUE 0.05.
          05 BCARD-RT        PIC 9V999 VALUE 0.02.
          05 FLYER-TOT       PIC 9(4)V99 VALUE ZERO.
          05 BCARD-TOT       PIC 9(4)V99 VALUE ZERO.
          05 COLOR-FEE       PIC 9(4)V99 VALUE ZERO.
          05 RUSH-FEE        PIC 9(3)V99 VALUE ZERO.
          05 SUB-TOT         PIC 9(5)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       START-PRESS.
           DISPLAY "--- INKWELL PRINTING SERVICES ---".
           DISPLAY "Business Name: ".
           ACCEPT BUSINESS-NAME.
           DISPLAY "Flyers QTY ($0.05 B&W): ".
           ACCEPT FLYER-QTY.
           DISPLAY "Business Cards QTY ($0.02 B&W): ".
           ACCEPT BCARD-QTY.
           DISPLAY "Upgrade to Full Color (+50% base)? (Y/N): ".
           ACCEPT COLOR-INK.
           DISPLAY "Rush 24Hr Turnaround (+$25 flat)? (Y/N): ".
           ACCEPT RUSH-PRINT.

           COMPUTE FLYER-TOT = FLYER-QTY * FLYER-RT.
           COMPUTE BCARD-TOT = BCARD-QTY * BCARD-RT.

           COMPUTE SUB-TOT = FLYER-TOT + BCARD-TOT.

           IF FULL-COLOR
               COMPUTE COLOR-FEE = SUB-TOT * 0.50
           END-IF.

           IF IS-RUSH
               MOVE 25.00 TO RUSH-FEE
           END-IF.

           COMPUTE GRAND-TOT = SUB-TOT + COLOR-FEE + RUSH-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             PRINT INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Account: " BUSINESS-NAME
           DISPLAY "----------------------------------------"
           IF FLYER-QTY > 0
               MOVE FLYER-TOT TO DISP
               DISPLAY "Flyers (x" FLYER-QTY "):  " DISP
           END-IF.
           IF BCARD-QTY > 0
               MOVE BCARD-TOT TO DISP
               DISPLAY "Biz Cards (x" BCARD-QTY "):" DISP
           END-IF.
           
           IF FULL-COLOR
               MOVE COLOR-FEE TO DISP
               DISPLAY "Color Ink (+50%):  " DISP
           END-IF.
           
           IF IS-RUSH
               MOVE RUSH-FEE TO DISP
               DISPLAY "Rush Handling:     " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL ORDER COST:  " DISP.
           DISPLAY "========================================".
           STOP RUN.
