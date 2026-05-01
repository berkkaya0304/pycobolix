       IDENTIFICATION DIVISION.
       PROGRAM-ID. COFFEE-SHOP.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-INPUTS.
          05 CUSTOMER-NAME   PIC X(20).
          05 DRINK-SIZE      PIC X.
             88 SMALL-SZ     VALUE 'S'.
             88 MEDIUM-SZ    VALUE 'M'.
             88 LARGE-SZ     VALUE 'L'.
          05 MILK-TYPE       PIC 9.
             88 WHOLE-MILK   VALUE 1.
             88 SKIM-MILK    VALUE 2.
             88 OAT-MILK     VALUE 3.
             88 ALMOND-MILK  VALUE 4.
          05 SYRUP-PUMPS     PIC 9(2) VALUE ZERO.

       01 PRICING.
          05 BASE-PRICE      PIC 9(2)V99 VALUE ZERO.
          05 MILK-SURCHARGE  PIC 9(2)V99 VALUE ZERO.
          05 SYRUP-FEE       PIC 9(2)V99 VALUE ZERO.
          05 DRINK-TOTAL     PIC 9(3)V99 VALUE ZERO.
          
       01 FORMAT-PRICE       PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- MORNING BREW CAFE ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUSTOMER-NAME.
           DISPLAY "Size (S/M/L): ".
           ACCEPT DRINK-SIZE.
           DISPLAY "Milk (1=Whole, 2=Skim, 3=Oat, 4=Almond): ".
           ACCEPT MILK-TYPE.
           DISPLAY "Syrup Pumps ($0.50 each): ".
           ACCEPT SYRUP-PUMPS.

           PERFORM CALCULATE-ORDER.
           PERFORM PRINT-RECEIPT.
           STOP RUN.

       CALCULATE-ORDER.
           EVALUATE TRUE
               WHEN SMALL-SZ
                   MOVE 3.50 TO BASE-PRICE
               WHEN MEDIUM-SZ
                   MOVE 4.50 TO BASE-PRICE
               WHEN LARGE-SZ
                   MOVE 5.50 TO BASE-PRICE
               WHEN OTHER
                   MOVE 3.50 TO BASE-PRICE
                   DISPLAY "Invalid size, defaulted to Small."
           END-EVALUATE.

           EVALUATE TRUE
               WHEN OAT-MILK
               WHEN ALMOND-MILK
                   MOVE 1.00 TO MILK-SURCHARGE
               WHEN OTHER
                   MOVE ZERO TO MILK-SURCHARGE
           END-EVALUATE.

           COMPUTE SYRUP-FEE = SYRUP-PUMPS * 0.50.
           COMPUTE DRINK-TOTAL = BASE-PRICE + MILK-SURCHARGE + SYRUP-FEE.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "=================================="
           DISPLAY "         CAFE RECEIPT             "
           DISPLAY "=================================="
           DISPLAY "Order for: " CUSTOMER-NAME
           DISPLAY "----------------------------------"
           MOVE BASE-PRICE TO FORMAT-PRICE.
           DISPLAY "Drink Base Price:  " FORMAT-PRICE.
           IF MILK-SURCHARGE > 0
               MOVE MILK-SURCHARGE TO FORMAT-PRICE
               DISPLAY "Premium Milk:      " FORMAT-PRICE
           END-IF.
           IF SYRUP-FEE > 0
               MOVE SYRUP-FEE TO FORMAT-PRICE
               DISPLAY "Syrup (" SYRUP-PUMPS ") pumps:   " FORMAT-PRICE
           END-IF.
           DISPLAY "----------------------------------"
           MOVE DRINK-TOTAL TO FORMAT-PRICE.
           DISPLAY "TOTAL AMOUNT DUE:  " FORMAT-PRICE.
           DISPLAY "==================================".
