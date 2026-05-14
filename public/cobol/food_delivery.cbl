       IDENTIFICATION DIVISION.
       PROGRAM-ID. FOOD-DELIVERY.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 APP-ORDER.
          05 ORDER-NUM       PIC 9(6).
          05 FOOD-SUBTOTAL   PIC 9(3)V99.
          05 MILES-AWAY      PIC 9(2)V9.
          05 ADD-TIP-PCT     PIC 9(2).

       01 APP-FEES.
          05 DELIVERY-FEE    PIC 9(2)V99 VALUE ZERO.
          05 SERVICE-FEE     PIC 9(2)V99 VALUE ZERO.
          05 TAX-AMT         PIC 9(2)V99 VALUE ZERO.
          05 DRIVER-TIP      PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-ORDER.
           DISPLAY "--- QUICK DASH FOOD DELIVERY ---".
           DISPLAY "Order Number: ".
           ACCEPT ORDER-NUM.
           DISPLAY "Restaurant Food Subtotal ($): ".
           ACCEPT FOOD-SUBTOTAL.
           DISPLAY "Distance from Restaurant (Miles): ".
           ACCEPT MILES-AWAY.
           DISPLAY "Tip Percentage for Driver (e.g. 15, 20): ".
           ACCEPT ADD-TIP-PCT.

           COMPUTE DELIVERY-FEE = 2.00 + (MILES-AWAY * 1.50).

           COMPUTE SERVICE-FEE = FOOD-SUBTOTAL * 0.15.

           COMPUTE TAX-AMT = FOOD-SUBTOTAL * 0.08.

           COMPUTE DRIVER-TIP = FOOD-SUBTOTAL * (ADD-TIP-PCT / 100).

           COMPUTE GRAND-TOT = FOOD-SUBTOTAL + DELIVERY-FEE + 
                               SERVICE-FEE + TAX-AMT + DRIVER-TIP.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           DELIVERY INVOICE             "
           DISPLAY "========================================"
           DISPLAY "Order ID: #" ORDER-NUM
           DISPLAY "----------------------------------------"
           MOVE FOOD-SUBTOTAL TO DISP.
           DISPLAY "Food Subtotal:      " DISP.
           MOVE DELIVERY-FEE TO DISP.
           DISPLAY "Delivery Distance:  " DISP.
           MOVE SERVICE-FEE TO DISP.
           DISPLAY "App Service Fee:    " DISP.
           MOVE TAX-AMT TO DISP.
           DISPLAY "Local Taxes:        " DISP.
           MOVE DRIVER-TIP TO DISP.
           DISPLAY "Driver Tip:         " DISP.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL CHARGE:       " DISP.
           DISPLAY "========================================".
           STOP RUN.
