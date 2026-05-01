       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEA-HOUSE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-FORM.
          05 PATRON-NAME       PIC X(15).
          05 GREEN-TEA-QTY     PIC 9(2) VALUE ZERO.
          05 BLACK-TEA-QTY     PIC 9(2) VALUE ZERO.
          05 HERBAL-TEA-QTY    PIC 9(2) VALUE ZERO.
          05 PASTRY-QTY        PIC 9(2) VALUE ZERO.

       01 ITEM-RATES.
          05 GREEN-RT          PIC 9(2)V99 VALUE 4.00.
          05 BLACK-RT          PIC 9(2)V99 VALUE 3.50.
          05 HERBAL-RT         PIC 9(2)V99 VALUE 4.50.
          05 PASTRY-RT         PIC 9(2)V99 VALUE 5.00.

       01 ITEM-TOTS.
          05 G-TOT             PIC 9(3)V99 VALUE ZERO.
          05 B-TOT             PIC 9(3)V99 VALUE ZERO.
          05 H-TOT             PIC 9(3)V99 VALUE ZERO.
          05 P-TOT             PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT         PIC 9(4)V99 VALUE ZERO.

       01 DISP                PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       TEA-MAIN.
           DISPLAY "--- ZEN LEAF TEA HOUSE ---".
           DISPLAY "Name: ".
           ACCEPT PATRON-NAME.
           DISPLAY "Matcha/Green Tea QTY ($4.00): ".
           ACCEPT GREEN-TEA-QTY.
           DISPLAY "Earl Grey/Black Tea QTY ($3.50): ".
           ACCEPT BLACK-TEA-QTY.
           DISPLAY "Chamomile/Herbal QTY ($4.50): ".
           ACCEPT HERBAL-TEA-QTY.
           DISPLAY "Assorted Pastries ($5.00): ".
           ACCEPT PASTRY-QTY.

           COMPUTE G-TOT = GREEN-TEA-QTY * GREEN-RT.
           COMPUTE B-TOT = BLACK-TEA-QTY * BLACK-RT.
           COMPUTE H-TOT = HERBAL-TEA-QTY * HERBAL-RT.
           COMPUTE P-TOT = PASTRY-QTY * PASTRY-RT.

           COMPUTE GRAND-TOT = G-TOT + B-TOT + H-TOT + P-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             TEA INVOICE                "
           DISPLAY "========================================"
           DISPLAY "Patron: " PATRON-NAME
           DISPLAY "----------------------------------------"
           IF GREEN-TEA-QTY > 0
               MOVE G-TOT TO DISP
               DISPLAY GREEN-TEA-QTY "x Green Teas:       " DISP
           END-IF.
           IF BLACK-TEA-QTY > 0
               MOVE B-TOT TO DISP
               DISPLAY BLACK-TEA-QTY "x Black Teas:       " DISP
           END-IF.
           IF HERBAL-TEA-QTY > 0
               MOVE H-TOT TO DISP
               DISPLAY HERBAL-TEA-QTY "x Herbal Teas:      " DISP
           END-IF.
           IF PASTRY-QTY > 0
               MOVE P-TOT TO DISP
               DISPLAY PASTRY-QTY "x Fresh Pastries:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL BALANCE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
