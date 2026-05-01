       IDENTIFICATION DIVISION.
       PROGRAM-ID. TOWING-SERVICE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 DISPATCH-LOG.
          05 DRIVER-NAME     PIC X(20).
          05 VEH-TYPE        PIC 9.
             88 STD-CAR      VALUE 1.
             88 HEAVY-TRUCK  VALUE 2.
             88 MOTORCYCLE   VALUE 3.
          05 TOW-MILES       PIC 9(3)V9.
          05 WINTCH-OUT      PIC X.
             88 NEED-WINTCH  VALUE 'Y'.

       01 COSTS.
          05 HOOK-FEE        PIC 9(3)V99 VALUE ZERO.
          05 MILE-RATE       PIC 9V99 VALUE ZERO.
          05 MILE-TOT        PIC 9(3)V99 VALUE ZERO.
          05 WINTCH-FEE      PIC 9(2)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-TOW.
           DISPLAY "--- HIGHWAY HERO TOWING ---".
           DISPLAY "Motorist: ".
           ACCEPT DRIVER-NAME.
           DISPLAY "Vehicle (1=Car, 2=Heavy Truck, 3=Motorcycle): ".
           ACCEPT VEH-TYPE.
           DISPLAY "Total Towing Miles: ".
           ACCEPT TOW-MILES.
           DISPLAY "Did vehicle require ditch/snow winch-out? (Y/N): ".
           ACCEPT WINTCH-OUT.

           EVALUATE TRUE
               WHEN STD-CAR
                   MOVE 75.00 TO HOOK-FEE
                   MOVE 3.50 TO MILE-RATE
               WHEN HEAVY-TRUCK
                   MOVE 125.00 TO HOOK-FEE
                   MOVE 5.00 TO MILE-RATE
               WHEN MOTORCYCLE
                   MOVE 60.00 TO HOOK-FEE
                   MOVE 3.00 TO MILE-RATE
               WHEN OTHER
                   MOVE 75.00 TO HOOK-FEE
                   MOVE 3.50 TO MILE-RATE
           END-EVALUATE.

           COMPUTE MILE-TOT = TOW-MILES * MILE-RATE.

           IF NEED-WINTCH
               MOVE 50.00 TO WINTCH-FEE
           END-IF.

           COMPUTE GRAND-TOT = HOOK-FEE + MILE-TOT + WINTCH-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          TOW SERVICE SUMMARY           "
           DISPLAY "========================================"
           DISPLAY "Motorist: " DRIVER-NAME
           DISPLAY "----------------------------------------"
           MOVE HOOK-FEE TO DISP.
           DISPLAY "Base Hookup Fee:     " DISP.
           MOVE MILE-TOT TO DISP.
           DISPLAY "Mileage (" TOW-MILES "m):     " DISP.
           
           IF NEED-WINTCH
               MOVE WINTCH-FEE TO DISP
               DISPLAY "Winch-Out Surcharge: " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL TOW BILL:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
