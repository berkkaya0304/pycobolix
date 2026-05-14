       IDENTIFICATION DIVISION.
       PROGRAM-ID. BAKERY-SHOP.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-QTY.
          05 CUST-NAME       PIC X(20).
          05 CAKE-QTY        PIC 9(2) VALUE ZERO.
          05 BREAD-QTY       PIC 9(2) VALUE ZERO.
          05 PASTRY-QTY      PIC 9(2) VALUE ZERO.

       01 ITEM-PRICES.
          05 CAKE-PRC        PIC 9(2)V99 VALUE 25.00.
          05 BREAD-PRC       PIC 9(2)V99 VALUE 4.50.
          05 PASTRY-PRC      PIC 9(2)V99 VALUE 3.00.

       01 CALCS.
          05 CAKE-TOT        PIC 9(4)V99 VALUE ZERO.
          05 BREAD-TOT       PIC 9(3)V99 VALUE ZERO.
          05 PASTRY-TOT      PIC 9(3)V99 VALUE ZERO.
          05 SUB-TOTAL       PIC 9(4)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(3)V99 VALUE ZERO.
          05 FINAL-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP-AMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BAKERY.
           DISPLAY "--- SUNRISE BAKERY POS ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Whole Cakes ($25.00 ea): ".
           ACCEPT CAKE-QTY.
           DISPLAY "Loaves of Bread ($4.50 ea): ".
           ACCEPT BREAD-QTY.
           DISPLAY "Assorted Pastries ($3.00 ea): ".
           ACCEPT PASTRY-QTY.

           PERFORM PROCESS-ORDER.
           PERFORM PRINT-BILL.
           STOP RUN.

       PROCESS-ORDER.
           COMPUTE CAKE-TOT = CAKE-QTY * CAKE-PRC.
           COMPUTE BREAD-TOT = BREAD-QTY * BREAD-PRC.
           COMPUTE PASTRY-TOT = PASTRY-QTY * PASTRY-PRC.

           COMPUTE SUB-TOTAL = CAKE-TOT + BREAD-TOT + PASTRY-TOT.

           IF SUB-TOTAL >= 50.00
               COMPUTE DISCOUNT = SUB-TOTAL * 0.10
           END-IF.

           COMPUTE FINAL-TOT = SUB-TOTAL - DISCOUNT.

       PRINT-BILL.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "          BAKERY ORDER RECEIPT           "
           DISPLAY "========================================="
           DISPLAY "Customer: " CUST-NAME
           DISPLAY "-----------------------------------------"
           IF CAKE-QTY > 0
               MOVE CAKE-TOT TO DISP-AMT
               DISPLAY CAKE-QTY " x Cakes:         " DISP-AMT
           END-IF.
           IF BREAD-QTY > 0
               MOVE BREAD-TOT TO DISP-AMT
               DISPLAY BREAD-QTY " x Bread Loaves:  " DISP-AMT
           END-IF.
           IF PASTRY-QTY > 0
               MOVE PASTRY-TOT TO DISP-AMT
               DISPLAY PASTRY-QTY " x Pastries:      " DISP-AMT
           END-IF.
           DISPLAY "-----------------------------------------"
           MOVE SUB-TOTAL TO DISP-AMT.
           DISPLAY "Subtotal:         " DISP-AMT.
           IF DISCOUNT > 0
               MOVE DISCOUNT TO DISP-AMT
               DISPLAY "Bulk Discount:   -" DISP-AMT
           END-IF.
           DISPLAY "-----------------------------------------"
           MOVE FINAL-TOT TO DISP-AMT.
           DISPLAY "TOTAL DUE:        " DISP-AMT.
           DISPLAY "=========================================".
