       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAINTBALL-ARENA.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PLAYER-APP.
          05 PLAYER-NAME     PIC X(20).
          05 ADMISSION-FEE   PIC 9(2)V99 VALUE 25.00.
          05 PAINTBALL-QTY   PIC 9(4) VALUE ZERO.
          05 GUN-UPGRADE     PIC X.
             88 PRO-GUN      VALUE 'Y'.

       01 COSTS.
          05 PAINT-COST      PIC 9(3)V99 VALUE ZERO.
          05 GUN-FEE         PIC 9(2)V99 VALUE ZERO.
          05 SUB-PRICE       PIC 9(4)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-DUE       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       ARENA-START.
           DISPLAY "--- SPLAT ZONE PAINTBALL ---".
           DISPLAY "Player Name: ".
           ACCEPT PLAYER-NAME.
           DISPLAY "Paintballs to Buy (qty of 100s, $5 per 100): ".
           ACCEPT PAINTBALL-QTY.
           DISPLAY "Upgrade to Pro Marker Gun ($15)? (Y/N): ".
           ACCEPT GUN-UPGRADE.

           COMPUTE PAINT-COST = (PAINTBALL-QTY / 100) * 5.00.

           IF PRO-GUN
               MOVE 15.00 TO GUN-FEE
           END-IF.

           COMPUTE SUB-PRICE = ADMISSION-FEE + PAINT-COST + GUN-FEE.
           COMPUTE TAX-AMT = SUB-PRICE * 0.07.
           COMPUTE TOTAL-DUE = SUB-PRICE + TAX-AMT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            ARENA INVOICE               "
           DISPLAY "========================================"
           DISPLAY "Player: " PLAYER-NAME
           DISPLAY "----------------------------------------"
           MOVE ADMISSION-FEE TO DISP.
           DISPLAY "Basic Entry Fee:    " DISP.
           
           IF PAINTBALL-QTY > 0
               MOVE PAINT-COST TO DISP
               DISPLAY "Extra Paint (" PAINTBALL-QTY "): " DISP
           END-IF.
           
           IF PRO-GUN
               MOVE GUN-FEE TO DISP
               DISPLAY "Pro Marker Upgrade: " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-PRICE TO DISP.
           DISPLAY "Subtotal:           " DISP.
           MOVE TAX-AMT TO DISP.
           DISPLAY "Tax (7%):           " DISP.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-DUE TO DISP.
           DISPLAY "TOTAL BALANCE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
