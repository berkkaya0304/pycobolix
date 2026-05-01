       IDENTIFICATION DIVISION.
       PROGRAM-ID. SHOE-STORE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CART-ITEMS.
          05 PAIR-QTY        PIC 9(2).
          
       01 ITEM-LOOP-DATA.
          05 IDX             PIC 9(2).
          05 SHOE-PRC OCCURS 10 TIMES PIC 9(3)V99.

       01 CALCS.
          05 TOTAL-PRICE     PIC 9(5)V99 VALUE ZERO.
          05 PAIRS-APPLIED   PIC 9(2) VALUE ZERO.
          05 DISCOUNT        PIC 9(4)V99 VALUE ZERO.
          05 FINAL-PAY       PIC 9(5)V99 VALUE ZERO.
          
       01 DISP               PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       CHECKOUT-START.
           DISPLAY "--- KICKS SNEAKER SHOP ---".
           DISPLAY "PROMO: Buy One Get One 50% Off! (Max 10 pairs)".
           DISPLAY "How many pairs being purchased?: ".
           ACCEPT PAIR-QTY.

           IF PAIR-QTY > 10
               DISPLAY "Max 10 pairs per transaction!"
               MOVE 10 TO PAIR-QTY
           END-IF.

           PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > PAIR-QTY
               DISPLAY "Price for Pair " IDX " ($): "
               ACCEPT SHOE-PRC(IDX)
               ADD SHOE-PRC(IDX) TO TOTAL-PRICE
           END-PERFORM.
           
           PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > PAIR-QTY
               IF FUNCTION MOD(IDX, 2) = 0
                   COMPUTE DISCOUNT = DISCOUNT + (SHOE-PRC(IDX) * 0.50)
               END-IF
           END-PERFORM.

           COMPUTE FINAL-PAY = TOTAL-PRICE - DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          STORE RECEIPT                 "
           DISPLAY "========================================"
           DISPLAY "Items Bought: " PAIR-QTY " pairs."
           DISPLAY "----------------------------------------"
           PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > PAIR-QTY
               MOVE SHOE-PRC(IDX) TO DISP
               DISPLAY "Box " IDX ":            " DISP
           END-PERFORM.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-PRICE TO DISP.
           DISPLAY "Subtotal:        " DISP.
           IF DISCOUNT > 0
               MOVE DISCOUNT TO DISP
               DISPLAY "BOGO 50% Savings:-" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE FINAL-PAY TO DISP.
           DISPLAY "TOTAL QUE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
