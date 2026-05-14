       IDENTIFICATION DIVISION.
       PROGRAM-ID. VENDING-MACHINE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MACHINE-ITEMS.
          05 ITEM-CHOICE     PIC X(2).
             88 SEL-SODA     VALUE "A1".
             88 SEL-CHIPS    VALUE "A2".
             88 SEL-CANDY    VALUE "B1".
             88 SEL-WATER    VALUE "B2".

       01 TRANSACTION.
          05 ITEM-PRICE      PIC 9(2)V99 VALUE ZERO.
          05 AMOUNT-INSERTED PIC 9(2)V99 VALUE ZERO.
          05 NEW-MONEY       PIC 9(2)V99 VALUE ZERO.
          05 CHANGE-DUE      PIC 9(2)V99 VALUE ZERO.
          05 ITEM-NAME       PIC X(15) VALUE SPACES.

       01 DISP-AMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-VEND.
           DISPLAY "--- SNACK-O-MATIC VENDING ---".
           DISPLAY "A1. Soda ($1.50)".
           DISPLAY "A2. Chips ($1.25)".
           DISPLAY "B1. Candy ($2.00)".
           DISPLAY "B2. Water ($1.00)".
           DISPLAY "Enter Selection: ".
           ACCEPT ITEM-CHOICE.

           EVALUATE TRUE
               WHEN SEL-SODA
                   MOVE 1.50 TO ITEM-PRICE
                   MOVE "Soda" TO ITEM-NAME
               WHEN SEL-CHIPS
                   MOVE 1.25 TO ITEM-PRICE
                   MOVE "Chips" TO ITEM-NAME
               WHEN SEL-CANDY
                   MOVE 2.00 TO ITEM-PRICE
                   MOVE "Candy" TO ITEM-NAME
               WHEN SEL-WATER
                   MOVE 1.00 TO ITEM-PRICE
                   MOVE "Water" TO ITEM-NAME
               WHEN OTHER
                   DISPLAY "Invalid Selection."
                   STOP RUN
           END-EVALUATE.

           MOVE ITEM-PRICE TO DISP-AMT.
           DISPLAY "Selected: " ITEM-NAME "  Cost: " DISP-AMT.
           
       PAYMENT-LOOP.
           IF AMOUNT-INSERTED < ITEM-PRICE
               DISPLAY "Insert Money ($ format): "
               ACCEPT NEW-MONEY
               ADD NEW-MONEY TO AMOUNT-INSERTED
               
               MOVE AMOUNT-INSERTED TO DISP-AMT
               DISPLAY "Current Credit: " DISP-AMT
               GO TO PAYMENT-LOOP
           END-IF.

       DISPENSE.
           COMPUTE CHANGE-DUE = AMOUNT-INSERTED - ITEM-PRICE.
           DISPLAY "-----------------------------------".
           DISPLAY "Vending " ITEM-NAME "...  *CLUNK*".
           IF CHANGE-DUE > 0
               MOVE CHANGE-DUE TO DISP-AMT
               DISPLAY "Refunding Change: " DISP-AMT
           ELSE
               DISPLAY "Exact change inserted."
           END-IF.
           DISPLAY "Thank you!".
           STOP RUN.
