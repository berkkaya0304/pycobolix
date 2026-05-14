       IDENTIFICATION DIVISION.
       PROGRAM-ID. ORDER-PROCESSING.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-HEADER.
          05 ORD-NUMBER      PIC 9(6).
          05 CUST-NAME       PIC X(30).
          05 ORD-DATE        PIC X(10).
          
       01 L-ITEMS OCCURS 3 TIMES.
          05 PRD-NAME        PIC X(15).
          05 PRD-QTY         PIC 9(3).
          05 PRD-PRICE       PIC 9(4)V99.
          05 PRD-SUBTOT      PIC 9(5)V99.

       01 TOTALS.
          05 GRAND-SUBTOT    PIC 9(6)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(6)V99 VALUE ZERO.
          05 SHIPPING        PIC 9(4)V99 VALUE 15.00.
          05 FINAL-TOTAL     PIC 9(7)V99 VALUE ZERO.

       01 FORMATTED-OUTPUTS.
          05 FMT-SUB         PIC $Z,ZZZ,ZZ9.99.
          05 FMT-TAX         PIC $Z,ZZZ,ZZ9.99.
          05 FMT-SHIP        PIC $Z,ZZZ,ZZ9.99.
          05 FMT-FIN         PIC $ZZ,ZZZ,ZZ9.99.
          05 I               PIC 9.

       PROCEDURE DIVISION.
       START-PROC.
           DISPLAY "*** ONLINE ORDER SYSTEM ***".
           DISPLAY "Order Number: ".
           ACCEPT ORD-NUMBER.
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Date (YYYY-MM-DD): ".
           ACCEPT ORD-DATE.

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 3
               DISPLAY "--- Enter Item " I " ---"
               DISPLAY "Product Name: "
               ACCEPT PRD-NAME(I)
               DISPLAY "Quantity: "
               ACCEPT PRD-QTY(I)
               DISPLAY "Unit Price: "
               ACCEPT PRD-PRICE(I)
               
               COMPUTE PRD-SUBTOT(I) = PRD-QTY(I) * PRD-PRICE(I)
               ADD PRD-SUBTOT(I) TO GRAND-SUBTOT
           END-PERFORM.

           PERFORM CALCULATE-TOTALS.
           PERFORM PRINT-INVOICE.
           STOP RUN.

       CALCULATE-TOTALS.
           COMPUTE TAX-AMT = GRAND-SUBTOT * 0.08.
           IF GRAND-SUBTOT > 500
               MOVE ZERO TO SHIPPING
           END-IF.
           COMPUTE FINAL-TOTAL = GRAND-SUBTOT + TAX-AMT + SHIPPING.

       PRINT-INVOICE.
           DISPLAY " ".
           DISPLAY "=============================================".
           DISPLAY "  INVOICE #" ORD-NUMBER "    DATE: " ORD-DATE.
           DISPLAY "  BILL TO: " CUST-NAME.
           DISPLAY "---------------------------------------------".
           DISPLAY "ITEM            QTY         PRICE       SUBTOTAL".
           DISPLAY "---------------------------------------------".
           
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 3
               MOVE PRD-SUBTOT(I) TO FMT-SUB
               DISPLAY PRD-NAME(I) "     " PRD-QTY(I) 
                       "          " PRD-PRICE(I) "     " FMT-SUB
           END-PERFORM.
           
           DISPLAY "---------------------------------------------".
           MOVE GRAND-SUBTOT TO FMT-SUB.
           MOVE TAX-AMT TO FMT-TAX.
           MOVE SHIPPING TO FMT-SHIP.
           MOVE FINAL-TOTAL TO FMT-FIN.
           DISPLAY "  Goods Total:   " FMT-SUB.
           DISPLAY "  Tax (8%):      " FMT-TAX.
           DISPLAY "  Shipping:      " FMT-SHIP.
           DISPLAY "=============================================".
           DISPLAY "  FINAL PAYABLE: " FMT-FIN.
           DISPLAY "=============================================".
