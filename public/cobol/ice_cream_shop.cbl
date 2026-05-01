       IDENTIFICATION DIVISION.
       PROGRAM-ID. ICE-CREAM.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ORDER-FORM.
          05 CUST-NAME       PIC X(15).
          05 SCOOPS          PIC 9(2).
          05 CONE-BOWL       PIC X.
             88 WAFFLE-CONE  VALUE 'W'.
             88 CUP-BOWL     VALUE 'C'.
          05 TOPPING-QTY     PIC 9(2).

       01 PRICES.
          05 SCOOP-PRC       PIC 9V99 VALUE 2.50.
          05 WAFFLE-PRC      PIC 9V99 VALUE 1.50.
          05 TOPPING-PRC     PIC 9V99 VALUE 0.75.

       01 CALCS.
          05 ICE-CREAM-FEE   PIC 9(3)V99 VALUE ZERO.
          05 CONE-FEE        PIC 9(2)V99 VALUE ZERO.
          05 TOP-FEE         PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-ORDER     PIC 9(3)V99 VALUE ZERO.

       01 DISP               PIC $ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-APP.
           DISPLAY "--- SWEET SCOOPS ICE CREAM ---".
           DISPLAY "Name for Order: ".
           ACCEPT CUST-NAME.
           DISPLAY "Number of Scoops ($2.50 ea): ".
           ACCEPT SCOOPS.
           DISPLAY "Vessel (W=Waffle Cone $1.50, C=Cup $0): ".
           ACCEPT CONE-BOWL.
           DISPLAY "Number of Toppings ($0.75 ea): ".
           ACCEPT TOPPING-QTY.

           COMPUTE ICE-CREAM-FEE = SCOOPS * SCOOP-PRC.

           IF WAFFLE-CONE
               MOVE WAFFLE-PRC TO CONE-FEE
           END-IF.

           COMPUTE TOP-FEE = TOPPING-QTY * TOPPING-PRC.

           COMPUTE TOTAL-ORDER = ICE-CREAM-FEE + CONE-FEE + TOP-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             ORDER TICKET               "
           DISPLAY "========================================"
           DISPLAY "Name: " CUST-NAME
           DISPLAY "----------------------------------------"
           MOVE ICE-CREAM-FEE TO DISP.
           DISPLAY "Ice Cream (" SCOOPS " scoops): " DISP.
           
           IF WAFFLE-CONE
               MOVE CONE-FEE TO DISP
               DISPLAY "Waffle Cone:           " DISP
           END-IF.
           
           IF TOPPING-QTY > 0
               MOVE TOP-FEE TO DISP
               DISPLAY "Toppings (" TOPPING-QTY "):          " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-ORDER TO DISP.
           DISPLAY "TOTAL DUE:             " DISP.
           DISPLAY "========================================".
           STOP RUN.
