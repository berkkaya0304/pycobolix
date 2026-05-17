       IDENTIFICATION DIVISION.
       PROGRAM-ID. TAILOR-SHOP.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-TICKET.
          05 CUST-NAME       PIC X(25).
          05 HEMMING-QTY     PIC 9(2) VALUE ZERO.
          05 ZIPPER-QTY      PIC 9(2) VALUE ZERO.
          05 SUIT-FIT-QTY    PIC 9(2) VALUE ZERO.
          05 RUSH-ORDER      PIC X.
             88 IS-RUSH      VALUE 'Y'.

       01 COSTS.
          05 HEM-RATE        PIC 9(2)V99 VALUE 15.00.
          05 ZIP-RATE        PIC 9(2)V99 VALUE 25.00.
          05 SUIT-RATE       PIC 9(3)V99 VALUE 120.00.

          05 HEM-TOT         PIC 9(4)V99 VALUE ZERO.
          05 ZIP-TOT         PIC 9(4)V99 VALUE ZERO.
          05 SUIT-TOT        PIC 9(4)V99 VALUE ZERO.
          
          05 SUB-TOTAL       PIC 9(5)V99 VALUE ZERO.
          05 RUSH-FEE        PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       TAILOR-START.
           DISPLAY "--- FINE STITCHES ALTERATIONS ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Pants/Skirts Hemming QTY ($15 ea): ".
           ACCEPT HEMMING-QTY.
           DISPLAY "Zipper Replacements QTY ($25 ea): ".
           ACCEPT ZIPPER-QTY.
           DISPLAY "Full Suit Tailoring QTY ($120 ea): ".
           ACCEPT SUIT-FIT-QTY.
           DISPLAY "Rush Order (Next Day +30%)? (Y/N): ".
           ACCEPT RUSH-ORDER.

           COMPUTE HEM-TOT = HEMMING-QTY * HEM-RATE.
           COMPUTE ZIP-TOT = ZIPPER-QTY * ZIP-RATE.
           COMPUTE SUIT-TOT = SUIT-FIT-QTY * SUIT-RATE.

           COMPUTE SUB-TOTAL = HEM-TOT + ZIP-TOT + SUIT-TOT.

           IF IS-RUSH
               COMPUTE RUSH-FEE = SUB-TOTAL * 0.30
           END-IF.

           COMPUTE GRAND-TOT = SUB-TOTAL + RUSH-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          ALTERATION TICKET             "
           DISPLAY "========================================"
           DISPLAY "Name: " CUST-NAME
           DISPLAY "----------------------------------------"
           IF HEMMING-QTY > 0
               MOVE HEM-TOT TO DISP
               DISPLAY HEMMING-QTY "x Hemming:          " DISP
           END-IF.
           IF ZIPPER-QTY > 0
               MOVE ZIP-TOT TO DISP
               DISPLAY ZIPPER-QTY "x Zipper Fix:       " DISP
           END-IF.
           IF SUIT-FIT-QTY > 0
               MOVE SUIT-TOT TO DISP
               DISPLAY SUIT-FIT-QTY "x Suit Tailoring:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-TOTAL TO DISP.
           DISPLAY "Subtotal:           " DISP.
           
           IF IS-RUSH
               MOVE RUSH-FEE TO DISP
               DISPLAY "Rush Charge (30%):  " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL BALANCE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
