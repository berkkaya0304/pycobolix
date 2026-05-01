       IDENTIFICATION DIVISION.
       PROGRAM-ID. HAIR-SALON.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CLIENT-APP.
          05 CLIENT-NAME     PIC X(20).
          05 SV-HAIRCUT      PIC X.
             88 WANTS-CUT    VALUE 'Y'.
          05 SV-COLOR        PIC X.
             88 WANTS-COLOR  VALUE 'Y'.
          05 SV-STYLIST      PIC 9.
             88 JUNIOR       VALUE 1.
             88 SENIOR       VALUE 2.
             88 MASTER       VALUE 3.
          05 TIP-PCT         PIC 9(2) VALUE ZERO.

       01 FEES.
          05 CUT-FEE         PIC 9(3)V99 VALUE ZERO.
          05 COLOR-FEE       PIC 9(3)V99 VALUE ZERO.
          05 LEVEL-RATE      PIC 9V99 VALUE 1.00.
          05 SUB-PRICE       PIC 9(4)V99 VALUE ZERO.
          05 TIP-AMT         PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-DUE       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       REG-START.
           DISPLAY "--- GLAMOUR STUDIO TICKET ---".
           DISPLAY "Client: ".
           ACCEPT CLIENT-NAME.
           DISPLAY "Haircut? (Y/N): ".
           ACCEPT SV-HAIRCUT.
           DISPLAY "Color/Dye? (Y/N): ".
           ACCEPT SV-COLOR.
           DISPLAY "Stylist Level (1=Jr, 2=Sr, 3=Master): ".
           ACCEPT SV-STYLIST.
           DISPLAY "Tip Percentage (e.g. 15, 20): ".
           ACCEPT TIP-PCT.

           EVALUATE TRUE
               WHEN JUNIOR
                   MOVE 1.00 TO LEVEL-RATE
               WHEN SENIOR
                   MOVE 1.30 TO LEVEL-RATE
               WHEN MASTER
                   MOVE 1.80 TO LEVEL-RATE
               WHEN OTHER
                   MOVE 1.00 TO LEVEL-RATE
           END-EVALUATE.

           IF WANTS-CUT
               COMPUTE CUT-FEE = 35.00 * LEVEL-RATE
           END-IF.

           IF WANTS-COLOR
               COMPUTE COLOR-FEE = 85.00 * LEVEL-RATE
           END-IF.

           COMPUTE SUB-PRICE = CUT-FEE + COLOR-FEE.
           COMPUTE TIP-AMT = SUB-PRICE * (TIP-PCT / 100).
           COMPUTE TOTAL-DUE = SUB-PRICE + TIP-AMT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             SALON INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Client: " CLIENT-NAME
           DISPLAY "----------------------------------------"
           IF WANTS-CUT
               MOVE CUT-FEE TO DISP
               DISPLAY "Haircut Service:    " DISP
           END-IF.
           IF WANTS-COLOR
               MOVE COLOR-FEE TO DISP
               DISPLAY "Coloring Service:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-PRICE TO DISP.
           DISPLAY "Services Total:     " DISP.
           
           IF TIP-AMT > 0
               MOVE TIP-AMT TO DISP
               DISPLAY "Stylist Tip (" TIP-PCT "%):  " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-DUE TO DISP.
           DISPLAY "TOTAL CHARGED:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
