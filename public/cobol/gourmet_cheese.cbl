       IDENTIFICATION DIVISION.
       PROGRAM-ID. GOURMET-CHEESE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CHEESE-ORDER.
          05 BRIE-LBS        PIC 9(2)V99 VALUE ZERO.
          05 CHEDDAR-LBS     PIC 9(2)V99 VALUE ZERO.
          05 GOUDA-LBS       PIC 9(2)V99 VALUE ZERO.
          05 CRACKER-BOXES   PIC 9(2) VALUE ZERO.

       01 PRICES.
          05 BRIE-PR        PIC 9(2)V99 VALUE 18.50.
          05 CHEDDAR-PR     PIC 9(2)V99 VALUE 12.00.
          05 GOUDA-PR       PIC 9(2)V99 VALUE 16.75.
          05 CRACKER-PR     PIC 9(2)V99 VALUE 4.50.

       01 TOTS.
          05 B-TOT          PIC 9(3)V99 VALUE ZERO.
          05 C-TOT          PIC 9(3)V99 VALUE ZERO.
          05 G-TOT          PIC 9(3)V99 VALUE ZERO.
          05 K-TOT          PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT      PIC 9(4)V99 VALUE ZERO.

       01 DISP             PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       SHOP-MAIN.
           DISPLAY "--- THE RUSTIC WHEEL CHEESE SHOP ---".
           DISPLAY "French Brie (lbs, $18.50/lb): ".
           ACCEPT BRIE-LBS.
           DISPLAY "Aged Cheddar (lbs, $12.00/lb): ".
           ACCEPT CHEDDAR-LBS.
           DISPLAY "Smoked Gouda (lbs, $16.75/lb): ".
           ACCEPT GOUDA-LBS.
           DISPLAY "Artisan Cracker Boxes ($4.50 ea): ".
           ACCEPT CRACKER-BOXES.

           COMPUTE B-TOT = BRIE-LBS * BRIE-PR.
           COMPUTE C-TOT = CHEDDAR-LBS * CHEDDAR-PR.
           COMPUTE G-TOT = GOUDA-LBS * GOUDA-PR.
           COMPUTE K-TOT = CRACKER-BOXES * CRACKER-PR.

           COMPUTE GRAND-TOT = B-TOT + C-TOT + G-TOT + K-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             SHOP RECEIPT               "
           DISPLAY "========================================"
           IF BRIE-LBS > 0
               MOVE B-TOT TO DISP
               DISPLAY "Brie (" BRIE-LBS " lbs):        " DISP
           END-IF.
           IF CHEDDAR-LBS > 0
               MOVE C-TOT TO DISP
               DISPLAY "Cheddar (" CHEDDAR-LBS " lbs):     " DISP
           END-IF.
           IF GOUDA-LBS > 0
               MOVE G-TOT TO DISP
               DISPLAY "Gouda (" GOUDA-LBS " lbs):       " DISP
           END-IF.
           IF CRACKER-BOXES > 0
               MOVE K-TOT TO DISP
               DISPLAY "Crackers (" CRACKER-BOXES " boxes):   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL SALE:          " DISP.
           DISPLAY "========================================".
           STOP RUN.
