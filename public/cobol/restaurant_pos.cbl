       IDENTIFICATION DIVISION.
       PROGRAM-ID. RESTAURANT-POS.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TABLE-INFO.
          05 TABLE-NUM       PIC 9(2).
          05 GUEST-COUNT     PIC 9(2).

       01 MENU-ITEMS OCCURS 5 TIMES.
          05 ITEM-NAME       PIC X(15).
          05 ITEM-QTY        PIC 9(2).
          05 ITEM-PRICE      PIC 9(3)V99.
          05 ITEM-SUBTOT     PIC 9(4)V99.

       01 BILLING.
          05 FOOD-TOT        PIC 9(5)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(4)V99 VALUE ZERO.
          05 TIP-AMT         PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(6)V99 VALUE ZERO.

       01 FORMATTED-FIELDS.
          05 DISP-MONEY      PIC $Z,ZZZ.99.
          05 I               PIC 9.
          05 MORE-ITEMS      PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       START-POS.
           DISPLAY "=== STARLIGHT RESTAURANT POS ===".
           DISPLAY "Table Number: ".
           ACCEPT TABLE-NUM.
           DISPLAY "Number of Guests: ".
           ACCEPT GUEST-COUNT.

           MOVE 1 TO I.
           PERFORM UNTIL MORE-ITEMS = 'N' OR I > 5
               DISPLAY "Enter Item Name: "
               ACCEPT ITEM-NAME(I)
               DISPLAY "Enter Quantity: "
               ACCEPT ITEM-QTY(I)
               DISPLAY "Enter Price per Item: "
               ACCEPT ITEM-PRICE(I)
               
               COMPUTE ITEM-SUBTOT(I) = ITEM-QTY(I) * ITEM-PRICE(I)
               ADD ITEM-SUBTOT(I) TO FOOD-TOT
               
               IF I < 5
                   DISPLAY "Add another item? (Y/N): "
                   ACCEPT MORE-ITEMS
               ELSE
                   DISPLAY "Max items reached."
                   MOVE 'N' TO MORE-ITEMS
               END-IF
               ADD 1 TO I
           END-PERFORM.

           PERFORM CALCULATE-TAX-TIP.
           PERFORM PRINT-BILL.
           STOP RUN.

       CALCULATE-TAX-TIP.
           COMPUTE TAX-AMT = FOOD-TOT * 0.0825.
           IF GUEST-COUNT >= 6
               COMPUTE TIP-AMT = FOOD-TOT * 0.18
               DISPLAY "*** Automatic Gratuity Applied (Party >= 6) ***"
           ELSE
               DISPLAY "Enter Tip Amount ($): "
               ACCEPT TIP-AMT
           END-IF.
           
           COMPUTE GRAND-TOT = FOOD-TOT + TAX-AMT + TIP-AMT.

       PRINT-BILL.
           DISPLAY " "
           DISPLAY "==========================================="
           DISPLAY "              GUEST CHECK                  "
           DISPLAY " TABLE: " TABLE-NUM "             GUESTS: " 
                   GUEST-COUNT
           DISPLAY "==========================================="
           
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
               IF ITEM-QTY(I) > 0
                   MOVE ITEM-SUBTOT(I) TO DISP-MONEY
                   DISPLAY ITEM-NAME(I) "   " ITEM-QTY(I) "   " 
                           DISP-MONEY
               END-IF
           END-PERFORM
           
           DISPLAY "-------------------------------------------"
           MOVE FOOD-TOT TO DISP-MONEY.
           DISPLAY "SUBTOTAL:         " DISP-MONEY.
           MOVE TAX-AMT TO DISP-MONEY.
           DISPLAY "TAX:              " DISP-MONEY.
           MOVE TIP-AMT TO DISP-MONEY.
           DISPLAY "GRATUITY:         " DISP-MONEY.
           DISPLAY "==========================================="
           MOVE GRAND-TOT TO DISP-MONEY.
           DISPLAY "TOTAL DUE:        " DISP-MONEY.
           DISPLAY "      Thank You For Dining With Us!        "
           DISPLAY "===========================================".
