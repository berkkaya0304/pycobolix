       IDENTIFICATION DIVISION.
       PROGRAM-ID. FOOD-TRUCK.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CUSTOMER-ORDER.
          05 ORDER-NAME      PIC X(15).
          05 TACO-QTY        PIC 9(2) VALUE ZERO.
          05 BURRITO-QTY     PIC 9(2) VALUE ZERO.
          05 DRINK-QTY       PIC 9(2) VALUE ZERO.
          05 ADD-GUAC        PIC X.
             88 WANTS-GUAC   VALUE 'Y'.

       01 PRICES.
          05 TACO-COST       PIC 9(3)V99 VALUE ZERO.
          05 BURRITO-COST    PIC 9(3)V99 VALUE ZERO.
          05 DRINK-COST      PIC 9(3)V99 VALUE ZERO.
          05 GUAC-COST       PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- EL TACO LOCO TRUCK ---".
           DISPLAY "Order Name: ".
           ACCEPT ORDER-NAME.
           DISPLAY "Street Tacos ($2.50 ea): ".
           ACCEPT TACO-QTY.
           DISPLAY "Super Burritos ($8.00 ea): ".
           ACCEPT BURRITO-QTY.
           DISPLAY "Sodas / Aguas Frescas ($2.00 ea): ".
           ACCEPT DRINK-QTY.
           DISPLAY "Add side of Guac & Chips ($4.00)? (Y/N): ".
           ACCEPT ADD-GUAC.

           COMPUTE TACO-COST = TACO-QTY * 2.50.
           COMPUTE BURRITO-COST = BURRITO-QTY * 8.00.
           COMPUTE DRINK-COST = DRINK-QTY * 2.00.

           IF WANTS-GUAC
               MOVE 4.00 TO GUAC-COST
           END-IF.

           COMPUTE TOTAL-COST = TACO-COST + BURRITO-COST 
                              + DRINK-COST + GUAC-COST.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          EL TACO LOCO RECEIPT          "
           DISPLAY "========================================"
           DISPLAY "Name: " ORDER-NAME
           DISPLAY "----------------------------------------"
           IF TACO-QTY > 0
               MOVE TACO-COST TO DISP
               DISPLAY TACO-QTY "x Tacos:            " DISP
           END-IF.
           IF BURRITO-QTY > 0
               MOVE BURRITO-COST TO DISP
               DISPLAY BURRITO-QTY "x Burritos:         " DISP
           END-IF.
           IF DRINK-QTY > 0
               MOVE DRINK-COST TO DISP
               DISPLAY DRINK-QTY "x Drinks:           " DISP
           END-IF.
           IF WANTS-GUAC
               MOVE GUAC-COST TO DISP
               DISPLAY "   Side of Guac:        " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-COST TO DISP.
           DISPLAY "TOTAL ORDER:            " DISP.
           DISPLAY "========================================".
           STOP RUN.
