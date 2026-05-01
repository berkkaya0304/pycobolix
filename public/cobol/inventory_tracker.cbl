       IDENTIFICATION DIVISION.
       PROGRAM-ID. INVENTORY-TRACKER.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 INVENTORY-ITEM.
          05 ITEM-ID         PIC X(5).
          05 ITEM-DESC       PIC X(30).
          05 QTY-ON-HAND     PIC 9(4) VALUE ZERO.
          05 REORDER-LEVEL   PIC 9(4) VALUE 20.
          05 UNIT-PRICE      PIC 9(4)V99.
          
       01 TRANSACTION-DATA.
          05 TRX-QTY         PIC 9(4).
          05 ACTION-CODE     PIC X.
             88 ADD-STOCK    VALUE 'A'.
             88 RMV-STOCK    VALUE 'R'.
             88 CHK-STOCK    VALUE 'C'.
             88 QUIT-APP     VALUE 'Q'.
             
       01 DISPLAY-FORMATS.
          05 DISP-PRICE      PIC $Z,ZZ9.99.
          05 DISP-VALUE      PIC $ZZ,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-SYSTEM.
           DISPLAY "=== INVENTORY MANAGEMENT ===".
           DISPLAY "Initialize a new item tracking...".
           DISPLAY "Item ID: ".
           ACCEPT ITEM-ID.
           DISPLAY "Item Description: ".
           ACCEPT ITEM-DESC.
           DISPLAY "Unit Price: ".
           ACCEPT UNIT-PRICE.
           DISPLAY "Initial Quantity: ".
           ACCEPT QTY-ON-HAND.

           PERFORM FOREVER
               DISPLAY " "
               DISPLAY "Action (A=Add, R=Remove, C=Check, Q=Quit): "
               ACCEPT ACTION-CODE
               
               EVALUATE TRUE
                   WHEN ADD-STOCK
                       PERFORM ADD-LOGIC
                   WHEN RMV-STOCK
                       PERFORM REMOVE-LOGIC
                   WHEN CHK-STOCK
                       PERFORM STATUS-LOGIC
                   WHEN QUIT-APP
                       EXIT PERFORM
                   WHEN OTHER
                       DISPLAY "Invalid Option."
               END-EVALUATE
           END-PERFORM.

           DISPLAY "Exiting Inventory System.".
           STOP RUN.

       ADD-LOGIC.
           DISPLAY "QTY to Add: ".
           ACCEPT TRX-QTY.
           ADD TRX-QTY TO QTY-ON-HAND.
           DISPLAY "Stock updated. Current QTY: " QTY-ON-HAND.

       REMOVE-LOGIC.
           DISPLAY "QTY to Remove (Sale): ".
           ACCEPT TRX-QTY.
           IF TRX-QTY > QTY-ON-HAND
               DISPLAY "Cannot remove! Only " QTY-ON-HAND " available."
           ELSE
               SUBTRACT TRX-QTY FROM QTY-ON-HAND
               DISPLAY "Stock shipped. Current QTY: " QTY-ON-HAND
           END-IF.

       STATUS-LOGIC.
           MOVE UNIT-PRICE TO DISP-PRICE.
           COMPUTE DISP-VALUE = QTY-ON-HAND * UNIT-PRICE.
           DISPLAY "--- ITEM STATUS ---".
           DISPLAY "ID:     " ITEM-ID.
           DISPLAY "Desc:   " ITEM-DESC.
           DISPLAY "Price:  " DISP-PRICE.
           DISPLAY "Stock:  " QTY-ON-HAND.
           DISPLAY "Total Value: " DISP-VALUE.
           IF QTY-ON-HAND <= REORDER-LEVEL
               DISPLAY "*** WARNING: STOCK BELOW REORDER LEVEL ***"
           END-IF.
           DISPLAY "-------------------".
