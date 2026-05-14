       IDENTIFICATION DIVISION.
       PROGRAM-ID. FLOWER-SHOP.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-FORM.
          05 RECIPIENT-NAME  PIC X(25).
          05 BOUQUET-SIZE    PIC 9.
             88 SMALL-BQT    VALUE 1.
             88 MED-BQT      VALUE 2.
             88 LARGE-BQT    VALUE 3.
          05 VASE-TYPE       PIC 9.
             88 NO-VASE      VALUE 1.
             88 GLASS-VASE   VALUE 2.
             88 CRYSTAL-VASE VALUE 3.
          05 DELIVERY-ZONE   PIC 9.
             88 LOCAL-DELIV  VALUE 1.
             88 REGION-DELIV VALUE 2.

       01 COSTS.
          05 FLOWER-COST     PIC 9(3)V99 VALUE ZERO.
          05 VASE-COST       PIC 9(2)V99 VALUE ZERO.
          05 DELIV-FEE       PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-SHOP.
           DISPLAY "--- BLOSSOMS FLORIST ---".
           DISPLAY "Recipient Name: ".
           ACCEPT RECIPIENT-NAME.
           DISPLAY "Bouquet Size (1=Small $30, 2=Med $50, 3=Lrg $80): ".
           ACCEPT BOUQUET-SIZE.
           DISPLAY "Vase (1=Wrapped, 2=Glass $15, 3=Crystal $40): ".
           ACCEPT VASE-TYPE.
           DISPLAY "Delivery Zone (1=Local $10, 2=Regional $25): ".
           ACCEPT DELIVERY-ZONE.

           EVALUATE TRUE
               WHEN SMALL-BQT
                   MOVE 30.00 TO FLOWER-COST
               WHEN MED-BQT
                   MOVE 50.00 TO FLOWER-COST
               WHEN LARGE-BQT
                   MOVE 80.00 TO FLOWER-COST
               WHEN OTHER
                   MOVE 30.00 TO FLOWER-COST
           END-EVALUATE.

           EVALUATE TRUE
               WHEN NO-VASE
                   MOVE ZERO TO VASE-COST
               WHEN GLASS-VASE
                   MOVE 15.00 TO VASE-COST
               WHEN CRYSTAL-VASE
                   MOVE 40.00 TO VASE-COST
               WHEN OTHER
                   MOVE ZERO TO VASE-COST
           END-EVALUATE.

           EVALUATE TRUE
               WHEN LOCAL-DELIV
                   MOVE 10.00 TO DELIV-FEE
               WHEN REGION-DELIV
                   MOVE 25.00 TO DELIV-FEE
               WHEN OTHER
                   MOVE 10.00 TO DELIV-FEE
           END-EVALUATE.

           COMPUTE TOTAL-BILL = FLOWER-COST + VASE-COST + DELIV-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          FLORIST ORDER RECEIPT         "
           DISPLAY "========================================"
           DISPLAY "Send To: " RECIPIENT-NAME
           DISPLAY "----------------------------------------"
           MOVE FLOWER-COST TO DISP.
           DISPLAY "Arrangement:        " DISP.
           
           IF VASE-COST > 0
               MOVE VASE-COST TO DISP
               DISPLAY "Vase/Container:     " DISP
           END-IF.
           
           MOVE DELIV-FEE TO DISP.
           DISPLAY "Delivery Fee:       " DISP.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-BILL TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:   " DISP.
           DISPLAY "========================================".
           STOP RUN.
