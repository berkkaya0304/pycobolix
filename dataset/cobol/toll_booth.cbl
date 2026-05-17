       IDENTIFICATION DIVISION.
       PROGRAM-ID. TOLL-BOOTH.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 VEHICLE-DATA.
          05 LICENSE-PLATE   PIC X(10).
          05 AXLES           PIC 9(2) VALUE 2.
          05 HAS-EZPASS      PIC X.
             88 EZ-PASS-YES  VALUE 'Y'.

       01 TOLL-CALC.
          05 BASE-TOLL       PIC 9(2)V99 VALUE 2.50.
          05 AXLE-CHARGE     PIC 9(2)V99 VALUE ZERO.
          05 GROSS-TOLL      PIC 9(3)V99 VALUE ZERO.
          05 DISCOUNT        PIC 9(2)V99 VALUE ZERO.
          05 NET-TOLL        PIC 9(3)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-TOLL.
           DISPLAY "--- TURNPIKE TOLL AUTHORITY ---".
           DISPLAY "License Plate: ".
           ACCEPT LICENSE-PLATE.
           DISPLAY "Number of Axles (e.g. 2 for car, 4+ for truck): ".
           ACCEPT AXLES.
           DISPLAY "EZ-Pass Transponder Detected? (Y/N): ".
           ACCEPT HAS-EZPASS.

           IF AXLES > 2
               COMPUTE AXLE-CHARGE = (AXLES - 2) * 2.00
           END-IF.

           COMPUTE GROSS-TOLL = BASE-TOLL + AXLE-CHARGE.

           IF EZ-PASS-YES
               COMPUTE DISCOUNT = GROSS-TOLL * 0.20
           END-IF.

           COMPUTE NET-TOLL = GROSS-TOLL - DISCOUNT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "           TOLL RECEIPT                 "
           DISPLAY "========================================"
           DISPLAY "Plate: " LICENSE-PLATE "   Axles: " AXLES
           DISPLAY "----------------------------------------"
           MOVE BASE-TOLL TO DISP.
           DISPLAY "Base Vehicle Toll:  " DISP.
           
           IF AXLE-CHARGE > 0
               MOVE AXLE-CHARGE TO DISP
               DISPLAY "Extra Axle Charge:  " DISP
           END-IF.
           
           IF EZ-PASS-YES
               MOVE DISCOUNT TO DISP
               DISPLAY "EZ-Pass Discount:  -" DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE NET-TOLL TO DISP.
           DISPLAY "TOTAL TOLL FARE:    " DISP.
           DISPLAY "========================================".
           STOP RUN.
