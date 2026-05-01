       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAR-MECHANIC.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SERVICE-ORDER.
          05 CUSTOMER-NAME   PIC X(20).
          05 VEHICLE-INFO    PIC X(15).
          05 OIL-CHANGE      PIC X.
             88 WANTS-OIL    VALUE 'Y'.
          05 TIRE-ROTATION   PIC X.
             88 WANTS-TIRE   VALUE 'Y'.
          05 BRAKE-PADS      PIC 9.
             88 FRONT-ONLY   VALUE 1.
             88 REAR-ONLY    VALUE 2.
             88 ALL-FOUR     VALUE 3.
             88 NO-BRAKES    VALUE 0.

       01 COSTS.
          05 OIL-FEE         PIC 9(2)V99 VALUE ZERO.
          05 TIRE-FEE        PIC 9(2)V99 VALUE ZERO.
          05 BRAKE-FEE       PIC 9(3)V99 VALUE ZERO.
          05 SHOP-SUPPLIES   PIC 9(2)V99 VALUE 15.00.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-SHOP.
           DISPLAY "--- GREASE MONKEY AUTO SHOP ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUSTOMER-NAME.
           DISPLAY "Vehicle Make/Model: ".
           ACCEPT VEHICLE-INFO.
           DISPLAY "Synthetic Oil Change ($65)? (Y/N): ".
           ACCEPT OIL-CHANGE.
           DISPLAY "Tire Rotation & Balance ($40)? (Y/N): ".
           ACCEPT TIRE-ROTATION.
           DISPLAY "Brakes (1=Front $150, 2=Rear $150, 3=All $280,"
           DISPLAY " 0=None): ".
           ACCEPT BRAKE-PADS.

           IF WANTS-OIL
               MOVE 65.00 TO OIL-FEE
           END-IF.

           IF WANTS-TIRE
               MOVE 40.00 TO TIRE-FEE
           END-IF.

           EVALUATE TRUE
               WHEN FRONT-ONLY
                   MOVE 150.00 TO BRAKE-FEE
               WHEN REAR-ONLY
                   MOVE 150.00 TO BRAKE-FEE
               WHEN ALL-FOUR
                   MOVE 280.00 TO BRAKE-FEE
               WHEN OTHER
                   MOVE ZERO TO BRAKE-FEE
           END-EVALUATE.

           COMPUTE GRAND-TOT = OIL-FEE + TIRE-FEE + BRAKE-FEE 
                             + SHOP-SUPPLIES.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            REPAIR INVOICE              "
           DISPLAY "========================================"
           DISPLAY "Customer: " CUSTOMER-NAME
           DISPLAY "Vehicle:  " VEHICLE-INFO
           DISPLAY "----------------------------------------"
           IF WANTS-OIL
               MOVE OIL-FEE TO DISP
               DISPLAY "Lube/Oil Change:    " DISP
           END-IF.
           IF WANTS-TIRE
               MOVE TIRE-FEE TO DISP
               DISPLAY "Tire Rotation:      " DISP
           END-IF.
           IF BRAKE-FEE > 0
               MOVE BRAKE-FEE TO DISP
               DISPLAY "Brake Pad Service:  " DISP
           END-IF.
           MOVE SHOP-SUPPLIES TO DISP.
           DISPLAY "Shop/Disposal Fee:  " DISP.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "GRAND TOTAL:        " DISP.
           DISPLAY "========================================".
           STOP RUN.
