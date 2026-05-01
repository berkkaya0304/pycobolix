       IDENTIFICATION DIVISION.
       PROGRAM-ID. LUMBER-YARD.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-FORM.
          05 BUILDER-NAME    PIC X(20).
          05 WOOD-TYPE       PIC 9.
             88 PINE         VALUE 1.
             88 OAK          VALUE 2.
             88 CEDAR        VALUE 3.
          05 BOARD-FEET      PIC 9(4).
          05 DELIVERY-REQ    PIC X.
             88 WANTS-DELIV  VALUE 'Y'.

       01 COSTS.
          05 PRICE-PER-BF    PIC 9(2)V99 VALUE ZERO.
          05 WOOD-COST       PIC 9(5)V99 VALUE ZERO.
          05 DELIV-FEE       PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-ORDER     PIC 9(6)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       DESK-START.
           DISPLAY "--- TIMBER WORKS LUMBER YARD ---".
           DISPLAY "Contractor Name: ".
           ACCEPT BUILDER-NAME.
           DISPLAY "Wood (1=Pine $2/bf, 2=Oak $6/bf, 3=Cedar $4/bf): ".
           ACCEPT WOOD-TYPE.
           DISPLAY "Quantity (Board Feet): ".
           ACCEPT BOARD-FEET.
           DISPLAY "Delivery to Job Site ($75 flat)? (Y/N): ".
           ACCEPT DELIVERY-REQ.

           EVALUATE TRUE
               WHEN PINE
                   MOVE 2.00 TO PRICE-PER-BF
               WHEN OAK
                   MOVE 6.00 TO PRICE-PER-BF
               WHEN CEDAR
                   MOVE 4.00 TO PRICE-PER-BF
               WHEN OTHER
                   MOVE 2.00 TO PRICE-PER-BF
                   DISPLAY "Invalid Type. Defaulted to Pine."
           END-EVALUATE.

           COMPUTE WOOD-COST = BOARD-FEET * PRICE-PER-BF.

           IF WANTS-DELIV
               MOVE 75.00 TO DELIV-FEE
           END-IF.

           COMPUTE TOTAL-ORDER = WOOD-COST + DELIV-FEE.

           DISPLAY " "
           DISPLAY "==========================================="
           DISPLAY "            LUMBER INVOICE                 "
           DISPLAY "==========================================="
           DISPLAY "Builder: " BUILDER-NAME
           DISPLAY "Lumber:  " BOARD-FEET " board feet"
           DISPLAY "-------------------------------------------"
           MOVE PRICE-PER-BF TO DISP.
           DISPLAY "Price Per BF:     " DISP.
           MOVE WOOD-COST TO DISP.
           DISPLAY "Material Cost:    " DISP.
           
           IF WANTS-DELIV
               MOVE DELIV-FEE TO DISP
               DISPLAY "Delivery Freight: " DISP
           END-IF.
           DISPLAY "-------------------------------------------"
           MOVE TOTAL-ORDER TO DISP.
           DISPLAY "GRAND TOTAL:      " DISP.
           DISPLAY "===========================================".
           STOP RUN.
