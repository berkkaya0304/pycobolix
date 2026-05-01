       IDENTIFICATION DIVISION.
       PROGRAM-ID. PIZZA-ORDER.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-DATA.
          05 CUST-NAME       PIC X(20).
          05 PIZZA-SIZE      PIC X.
             88 SIZE-S       VALUE 'S'.
             88 SIZE-M       VALUE 'M'.
             88 SIZE-L       VALUE 'L'.
          05 CRUST-TYPE      PIC 9.
             88 THIN-CRUST   VALUE 1.
             88 THICK-CRUST  VALUE 2.
             88 STUFFED      VALUE 3.
          05 TOPPING-QTY     PIC 9(2) VALUE ZERO.

       01 PRICING.
          05 BASE-PRICE      PIC 9(2)V99 VALUE ZERO.
          05 CRUST-FEE       PIC 9(2)V99 VALUE ZERO.
          05 TOPPING-FEE     PIC 9(2)V99 VALUE ZERO.
          05 SUB-TOTAL       PIC 9(3)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(2)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(4)V99 VALUE ZERO.

       01 FMT-PRC            PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-ORDER.
           DISPLAY "--- MARIO'S PIZZERIA ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Size (S=Small $10, M=Medium $14, L=Large $18): ".
           ACCEPT PIZZA-SIZE.
           DISPLAY "Crust (1=Thin, 2=Thick, 3=Stuffed +$3): ".
           ACCEPT CRUST-TYPE.
           DISPLAY "Number of Extra Toppings ($1.50 ea): ".
           ACCEPT TOPPING-QTY.

           PERFORM CALCULATE-ORDER.
           PERFORM PRINT-RECEIPT.
           STOP RUN.

       CALCULATE-ORDER.
           EVALUATE TRUE
               WHEN SIZE-S
                   MOVE 10.00 TO BASE-PRICE
               WHEN SIZE-M
                   MOVE 14.00 TO BASE-PRICE
               WHEN SIZE-L
                   MOVE 18.00 TO BASE-PRICE
               WHEN OTHER
                   MOVE 10.00 TO BASE-PRICE
                   DISPLAY "Invalid Size, Default to Small."
           END-EVALUATE.

           IF STUFFED
               MOVE 3.00 TO CRUST-FEE
           ELSE
               MOVE ZERO TO CRUST-FEE
           END-IF.

           COMPUTE TOPPING-FEE = TOPPING-QTY * 1.50.
           
           COMPUTE SUB-TOTAL = BASE-PRICE + CRUST-FEE + TOPPING-FEE.
           COMPUTE TAX-AMT = SUB-TOTAL * 0.08.
           COMPUTE GRAND-TOTAL = SUB-TOTAL + TAX-AMT.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          PIZZA ORDER RECEIPT           "
           DISPLAY "========================================"
           DISPLAY "Order for: " CUST-NAME
           DISPLAY "----------------------------------------"
           MOVE BASE-PRICE TO FMT-PRC.
           DISPLAY "Base Pizza:       " FMT-PRC.
           IF CRUST-FEE > 0
               MOVE CRUST-FEE TO FMT-PRC
               DISPLAY "Stuffed Crust:    " FMT-PRC
           END-IF.
           IF TOPPING-FEE > 0
               MOVE TOPPING-FEE TO FMT-PRC
               DISPLAY "Toppings (" TOPPING-QTY "):    " FMT-PRC
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE SUB-TOTAL TO FMT-PRC.
           DISPLAY "Subtotal:         " FMT-PRC.
           MOVE TAX-AMT TO FMT-PRC.
           DISPLAY "Tax (8%):         " FMT-PRC.
           DISPLAY "========================================"
           MOVE GRAND-TOTAL TO FMT-PRC.
           DISPLAY "TOTAL AMOUNT DUE: " FMT-PRC.
           DISPLAY "========================================".
