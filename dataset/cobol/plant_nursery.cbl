       IDENTIFICATION DIVISION.
       PROGRAM-ID. PLANT-NURSERY.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NURSERY-CART.
          05 SUC-QTY         PIC 9(2) VALUE ZERO.
          05 FERN-QTY        PIC 9(2) VALUE ZERO.
          05 TREE-QTY        PIC 9(2) VALUE ZERO.
          05 POT-QTY         PIC 9(2) VALUE ZERO.
          05 SOIL-BAGS       PIC 9(2) VALUE ZERO.

       01 PRICES.
          05 SUC-PRC         PIC 9(2)V99 VALUE 5.50.
          05 FERN-PRC        PIC 9(2)V99 VALUE 15.00.
          05 TREE-PRC        PIC 9(2)V99 VALUE 45.00.
          05 POT-PRC         PIC 9(2)V99 VALUE 8.50.
          05 SOIL-PRC        PIC 9(2)V99 VALUE 12.00.

       01 CALCS.
          05 S-TOT           PIC 9(3)V99 VALUE ZERO.
          05 F-TOT           PIC 9(3)V99 VALUE ZERO.
          05 T-TOT           PIC 9(3)V99 VALUE ZERO.
          05 P-TOT           PIC 9(3)V99 VALUE ZERO.
          05 D-TOT           PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-NURSERY.
           DISPLAY "--- BOTANICA PLANT NURSERY ---".
           DISPLAY "Mini Succulents QTY ($5.50 ea): ".
           ACCEPT SUC-QTY.
           DISPLAY "Ferns & Hanging Plants QTY ($15.00 ea): ".
           ACCEPT FERN-QTY.
           DISPLAY "Small Info Trees QTY ($45.00 ea): ".
           ACCEPT TREE-QTY.
           DISPLAY "Ceramic Pots ($8.50 ea): ".
           ACCEPT POT-QTY.
           DISPLAY "Bags of Potting Soil ($12.00 ea): ".
           ACCEPT SOIL-BAGS.

           COMPUTE S-TOT = SUC-QTY * SUC-PRC.
           COMPUTE F-TOT = FERN-QTY * FERN-PRC.
           COMPUTE T-TOT = TREE-QTY * TREE-PRC.
           COMPUTE P-TOT = POT-QTY * POT-PRC.
           COMPUTE D-TOT = SOIL-BAGS * SOIL-PRC.

           COMPUTE GRAND-TOT = S-TOT + F-TOT + T-TOT + P-TOT + D-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            GARDEN RECEIPT              "
           DISPLAY "========================================"
           IF SUC-QTY > 0
               MOVE S-TOT TO DISP
               DISPLAY "Succulents (" SUC-QTY "):        " DISP
           END-IF.
           IF FERN-QTY > 0
               MOVE F-TOT TO DISP
               DISPLAY "Ferns (" FERN-QTY "):             " DISP
           END-IF.
           IF TREE-QTY > 0
               MOVE T-TOT TO DISP
               DISPLAY "Trees (" TREE-QTY "):             " DISP
           END-IF.
           IF POT-QTY > 0
               MOVE P-TOT TO DISP
               DISPLAY "Ceramic Pots (" POT-QTY "):      " DISP
           END-IF.
           IF SOIL-BAGS > 0
               MOVE D-TOT TO DISP
               DISPLAY "Potting Soil (" SOIL-BAGS "):      " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
