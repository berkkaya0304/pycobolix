       IDENTIFICATION DIVISION.
       PROGRAM-ID. GAS-STATION.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PUMP-DATA.
          05 FUEL-TYPE       PIC 9.
             88 REGULAR      VALUE 1.
             88 PLUS         VALUE 2.
             88 PREMIUM      VALUE 3.
             88 DIESEL       VALUE 4.
          05 GALLONS-PUMPED  PIC 9(3)V99.
          05 CAR-WASH        PIC X.
             88 WANTS-WASH   VALUE 'Y'.

       01 PRICING.
          05 PRICE-PER-GAL   PIC 9(2)V99 VALUE ZERO.
          05 FUEL-TOTAL      PIC 9(4)V99 VALUE ZERO.
          05 WASH-FEE        PIC 9(2)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(4)V99 VALUE ZERO.

       01 DISP-FMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-PUMP.
           DISPLAY "--- FAST FILL GAS STATION ---".
           DISPLAY "Select Fuel Grade: ".
           DISPLAY "1=Regular 87 ($3.50)".
           DISPLAY "2=Plus 89 ($3.80)".
           DISPLAY "3=Premium 93 ($4.20)".
           DISPLAY "4=Diesel ($4.50)".
           ACCEPT FUEL-TYPE.
           
           DISPLAY "Gallons Pumped: ".
           ACCEPT GALLONS-PUMPED.
           
           DISPLAY "Add Basic Car Wash for $8.00? (Y/N): ".
           ACCEPT CAR-WASH.

           PERFORM CALCULATE-SALE.
           PERFORM PRINT-RECEIPT.
           STOP RUN.

       CALCULATE-SALE.
           EVALUATE TRUE
               WHEN REGULAR
                   MOVE 3.50 TO PRICE-PER-GAL
               WHEN PLUS
                   MOVE 3.80 TO PRICE-PER-GAL
               WHEN PREMIUM
                   MOVE 4.20 TO PRICE-PER-GAL
               WHEN DIESEL
                   MOVE 4.50 TO PRICE-PER-GAL
               WHEN OTHER
                   MOVE 3.50 TO PRICE-PER-GAL
                   DISPLAY "Invalid Selection. Defaulting to Regular."
           END-EVALUATE.

           COMPUTE FUEL-TOTAL = GALLONS-PUMPED * PRICE-PER-GAL.

           IF WANTS-WASH
               MOVE 8.00 TO WASH-FEE
           END-IF.

           COMPUTE GRAND-TOTAL = FUEL-TOTAL + WASH-FEE.

       PRINT-RECEIPT.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "          FUEL PUMP RECEIPT            "
           DISPLAY "======================================="
           DISPLAY "Gallons Dispensed: " GALLONS-PUMPED
           DISPLAY "Price per Gallon:  $" PRICE-PER-GAL
           DISPLAY "---------------------------------------"
           MOVE FUEL-TOTAL TO DISP-FMT.
           DISPLAY "Fuel Charge:       " DISP-FMT.
           
           IF WANTS-WASH
               MOVE WASH-FEE TO DISP-FMT
               DISPLAY "Car Wash Add-on:   " DISP-FMT
               DISPLAY "   -> Wash Code: 49813 <-"
           END-IF.
           DISPLAY "---------------------------------------"
           MOVE GRAND-TOTAL TO DISP-FMT.
           DISPLAY "TOTAL SALE:        " DISP-FMT.
           DISPLAY "=======================================".
