       IDENTIFICATION DIVISION.
       PROGRAM-ID. WINE-TASTING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TOUR-INFO.
          05 GUEST-NAME      PIC X(20).
          05 TOUR-TIER       PIC 9.
             88 BASIC-TOUR   VALUE 1.
             88 RESRV-TOUR   VALUE 2.
          05 RED-WINE-BTL    PIC 9(2) VALUE ZERO.
          05 WHT-WINE-BTL    PIC 9(2) VALUE ZERO.

       01 FEES.
          05 TOUR-FEE        PIC 9(2)V99 VALUE ZERO.
          05 RED-FEE         PIC 9(3)V99 VALUE ZERO.
          05 WHT-FEE         PIC 9(3)V99 VALUE ZERO.
          05 CASE-DISCOUNT   PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       VINEYARD-START.
           DISPLAY "--- OAK BARREL VINEYARD ---".
           DISPLAY "Guest Name: ".
           ACCEPT GUEST-NAME.
           DISPLAY "Tasting (1=Basic $25, 2=Reserve $50): ".
           ACCEPT TOUR-TIER.
           DISPLAY "Cabernet Bottles to Buy ($40 ea): ".
           ACCEPT RED-WINE-BTL.
           DISPLAY "Chardonnay Bottles to Buy ($30 ea): ".
           ACCEPT WHT-WINE-BTL.

           IF BASIC-TOUR
               MOVE 25.00 TO TOUR-FEE
           ELSE IF RESRV-TOUR
               MOVE 50.00 TO TOUR-FEE
           ELSE
               MOVE 25.00 TO TOUR-FEE
           END-IF.

           COMPUTE RED-FEE = RED-WINE-BTL * 40.00.
           COMPUTE WHT-FEE = WHT-WINE-BTL * 30.00.

           IF (RED-WINE-BTL + WHT-WINE-BTL) >= 6
               COMPUTE CASE-DISCOUNT = (RED-FEE + WHT-FEE) * 0.10
           END-IF.

           COMPUTE GRAND-TOT = TOUR-FEE + RED-FEE + WHT-FEE
                             - CASE-DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            VINEYARD RECEIPT            "
           DISPLAY "========================================"
           DISPLAY "Guest: " GUEST-NAME
           DISPLAY "----------------------------------------"
           MOVE TOUR-FEE TO DISP.
           DISPLAY "Tasting Flight Fee: " DISP.
           IF RED-WINE-BTL > 0
               MOVE RED-FEE TO DISP
               DISPLAY "Cabernet (" RED-WINE-BTL "):       " DISP
           END-IF.
           IF WHT-WINE-BTL > 0
               MOVE WHT-FEE TO DISP
               DISPLAY "Chardonnay (" WHT-WINE-BTL "):     " DISP
           END-IF.
           IF CASE-DISCOUNT > 0
               MOVE CASE-DISCOUNT TO DISP
               DISPLAY "Half-Case Disc 10%: -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:   " DISP.
           DISPLAY "========================================".
           STOP RUN.
