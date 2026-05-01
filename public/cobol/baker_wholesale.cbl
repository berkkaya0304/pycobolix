       IDENTIFICATION DIVISION.
       PROGRAM-ID. BAKER-WHOLESALE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-DATA.
          05 BAKERY-NAME     PIC X(25).
          05 FLOUR-SACKS     PIC 9(3) VALUE ZERO.
          05 SUGAR-SACKS     PIC 9(3) VALUE ZERO.
          05 YEAST-BLOCKS    PIC 9(3) VALUE ZERO.
          05 DELIVERY        PIC X.
             88 WANTS-DELIV  VALUE 'Y'.

       01 PRICES.
          05 FLOUR-PRC       PIC 9(2)V99 VALUE 22.50.
          05 SUGAR-PRC       PIC 9(2)V99 VALUE 28.00.
          05 YEAST-PRC       PIC 9(2)V99 VALUE 15.00.

       01 TOTS.
          05 F-TOT           PIC 9(4)V99 VALUE ZERO.
          05 S-TOT           PIC 9(4)V99 VALUE ZERO.
          05 Y-TOT           PIC 9(4)V99 VALUE ZERO.
          05 FREIGHT-FEE     PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(6)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-ORDER.
           DISPLAY "--- GRAIN & MILL WHOLESALE ---".
           DISPLAY "Bakery Name: ".
           ACCEPT BAKERY-NAME.
           DISPLAY "Flour Sacks (50lb, $22.50 ea): ".
           ACCEPT FLOUR-SACKS.
           DISPLAY "Sugar Sacks (50lb, $28.00 ea): ".
           ACCEPT SUGAR-SACKS.
           DISPLAY "Yeast Blocks (5lb, $15.00 ea): ".
           ACCEPT YEAST-BLOCKS.
           DISPLAY "Require Freight Delivery ($150 flat)? (Y/N): ".
           ACCEPT DELIVERY.

           COMPUTE F-TOT = FLOUR-SACKS * FLOUR-PRC.
           COMPUTE S-TOT = SUGAR-SACKS * SUGAR-PRC.
           COMPUTE Y-TOT = YEAST-BLOCKS * YEAST-PRC.

           IF WANTS-DELIV
               MOVE 150.00 TO FREIGHT-FEE
           END-IF.

           COMPUTE GRAND-TOT = F-TOT + S-TOT + Y-TOT + FREIGHT-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           WHOLESALE INVOICE            "
           DISPLAY "========================================"
           DISPLAY "Buyer: " BAKERY-NAME
           DISPLAY "----------------------------------------"
           IF FLOUR-SACKS > 0
               MOVE F-TOT TO DISP
               DISPLAY "Flour (x" FLOUR-SACKS "):      " DISP
           END-IF.
           IF SUGAR-SACKS > 0
               MOVE S-TOT TO DISP
               DISPLAY "Sugar (x" SUGAR-SACKS "):      " DISP
           END-IF.
           IF YEAST-BLOCKS > 0
               MOVE Y-TOT TO DISP
               DISPLAY "Yeast (x" YEAST-BLOCKS "):      " DISP
           END-IF.
           IF WANTS-DELIV
               MOVE FREIGHT-FEE TO DISP
               DISPLAY "LTL Freight:    " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL DUE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
