       IDENTIFICATION DIVISION.
       PROGRAM-ID. MUSIC-STORE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PURCHASE-DATA.
          05 BUYER-NAME      PIC X(20).
          05 VINYL-QTY       PIC 9(2) VALUE ZERO.
          05 CD-QTY          PIC 9(2) VALUE ZERO.
          05 INSTRUMENT-COST PIC 9(4)V99 VALUE ZERO.

       01 TOTS.
          05 VINYL-TOT       PIC 9(4)V99 VALUE ZERO.
          05 CD-TOT          PIC 9(3)V99 VALUE ZERO.
          05 SUB-PRICE       PIC 9(5)V99 VALUE ZERO.
          05 MEM-DISC        PIC 9(4)V99 VALUE ZERO.
          05 FINAL-AMT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- RETRO WAVES MUSIC STORE ---".
           DISPLAY "Customer: ".
           ACCEPT BUYER-NAME.
           DISPLAY "Vinyl Records QTY ($30 ea): ".
           ACCEPT VINYL-QTY.
           DISPLAY "CDs QTY ($15 ea): ".
           ACCEPT CD-QTY.
           DISPLAY "Musical Instruments Total ($): ".
           ACCEPT INSTRUMENT-COST.

           COMPUTE VINYL-TOT = VINYL-QTY * 30.00.
           COMPUTE CD-TOT = CD-QTY * 15.00.

           COMPUTE SUB-PRICE = VINYL-TOT + CD-TOT + INSTRUMENT-COST.

           IF SUB-PRICE > 100.00
               COMPUTE MEM-DISC = SUB-PRICE * 0.10
           END-IF.

           COMPUTE FINAL-AMT = SUB-PRICE - MEM-DISC.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             STORE RECEIPT              "
           DISPLAY "========================================"
           DISPLAY "Customer: " BUYER-NAME
           DISPLAY "----------------------------------------"
           IF VINYL-QTY > 0
               MOVE VINYL-TOT TO DISP
               DISPLAY "Vinyl Records (" VINYL-QTY "): " DISP
           END-IF.
           IF CD-QTY > 0
               MOVE CD-TOT TO DISP
               DISPLAY "CDs (" CD-QTY "):           " DISP
           END-IF.
           IF INSTRUMENT-COST > 0
               MOVE INSTRUMENT-COST TO DISP
               DISPLAY "Instruments:       " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-PRICE TO DISP.
           DISPLAY "Subtotal:          " DISP.
           IF MEM-DISC > 0
               MOVE MEM-DISC TO DISP
               DISPLAY "10% Discount:     -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-AMT TO DISP.
           DISPLAY "NET PAYABLE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
