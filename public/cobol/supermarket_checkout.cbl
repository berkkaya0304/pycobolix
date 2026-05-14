       IDENTIFICATION DIVISION.
       PROGRAM-ID. SUPERMARKET.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ITEM-REC OCCURS 3 TIMES.
          05 ITEM-NAME       PIC X(15).
          05 PRICING-TYPE    PIC X.
             88 BY-UNIT      VALUE 'U'.
             88 BY-WEIGHT    VALUE 'W'.
          05 PRICE-PER       PIC 9(2)V99.
          05 QTY-OR-WEIGHT   PIC 9(2)V99.
          05 SUB-TOTAL       PIC 9(3)V99.

       01 BILLING.
          05 GROSS-TOTAL     PIC 9(4)V99 VALUE ZERO.
          05 TAX-AMOUNT      PIC 9(3)V99 VALUE ZERO.
          05 NET-TOTAL       PIC 9(4)V99 VALUE ZERO.

       01 MEM-CARD           PIC X.
       01 DISP-VAL           PIC $Z,ZZ9.99.
       01 IDX                PIC 9.

       PROCEDURE DIVISION.
       START-POS.
           DISPLAY "--- FRESH MART CHECKOUT ---".
           DISPLAY "Do you have a loyalty card? (Y/N): ".
           ACCEPT MEM-CARD.

           PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > 3
               DISPLAY "Item " IDX " Name: "
               ACCEPT ITEM-NAME(IDX)
               DISPLAY "Pricing (U=Unit, W=Weight/lbs): "
               ACCEPT PRICING-TYPE(IDX)
               DISPLAY "Price per U/W ($): "
               ACCEPT PRICE-PER(IDX)
               IF PRICING-TYPE(IDX) = 'U'
                   DISPLAY "Quantity: "
                   ACCEPT QTY-OR-WEIGHT(IDX)
               ELSE
                   DISPLAY "Weight (lbs): "
                   ACCEPT QTY-OR-WEIGHT(IDX)
               END-IF
               
               COMPUTE SUB-TOTAL(IDX) = PRICE-PER(IDX) * 
                                        QTY-OR-WEIGHT(IDX)
               ADD SUB-TOTAL(IDX) TO GROSS-TOTAL
           END-PERFORM.

           PERFORM PROCESS-BILL.
           PERFORM PRINT-RECEIPT.
           STOP RUN.

       PROCESS-BILL.
           IF MEM-CARD = 'Y' OR 'y'
               COMPUTE GROSS-TOTAL = GROSS-TOTAL * 0.95
               DISPLAY "(5% Member Discount Applied)"
           END-IF.

           COMPUTE TAX-AMOUNT = GROSS-TOTAL * 0.02.
           COMPUTE NET-TOTAL = GROSS-TOTAL + TAX-AMOUNT.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "          FRESH MART RECEIPT           "
           DISPLAY "======================================="
           
           PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > 3
               MOVE SUB-TOTAL(IDX) TO DISP-VAL
               DISPLAY ITEM-NAME(IDX) " x " QTY-OR-WEIGHT(IDX) 
                       "    " DISP-VAL
           END-PERFORM.
           
           DISPLAY "---------------------------------------"
           MOVE GROSS-TOTAL TO DISP-VAL.
           DISPLAY "Subtotal:        " DISP-VAL.
           MOVE TAX-AMOUNT TO DISP-VAL.
           DISPLAY "Tax (2%):        " DISP-VAL.
           DISPLAY "---------------------------------------"
           MOVE NET-TOTAL TO DISP-VAL.
           DISPLAY "TOTAL BALANCE:   " DISP-VAL.
           DISPLAY "=======================================".
