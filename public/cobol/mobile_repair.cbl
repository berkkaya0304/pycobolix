       IDENTIFICATION DIVISION.
       PROGRAM-ID. MOBILE-REPAIR.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 DEVICE-INFO.
          05 CUSTOMER        PIC X(20).
          05 PHONE-MODEL     PIC X(15).
          05 SCREEN-FIX      PIC X.
             88 FIX-SCREEN   VALUE 'Y'.
          05 BATTERY-FIX     PIC X.
             88 FIX-BATTERY  VALUE 'Y'.
          05 WATER-DAMAGE    PIC X.
             88 DIAGNOSE     VALUE 'Y'.

       01 FEES.
          05 SCREEN-FEE      PIC 9(3)V99 VALUE ZERO.
          05 BATT-FEE        PIC 9(2)V99 VALUE ZERO.
          05 DIAG-FEE        PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-COST      PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-REPAIR.
           DISPLAY "--- CELL DOCTOR REPAIRS ---".
           DISPLAY "Customer: ".
           ACCEPT CUSTOMER.
           DISPLAY "Phone Model: ".
           ACCEPT PHONE-MODEL.
           DISPLAY "OLED Screen Replacement ($180)? (Y/N): ".
           ACCEPT SCREEN-FIX.
           DISPLAY "Battery Replacement ($65)? (Y/N): ".
           ACCEPT BATTERY-FIX.
           DISPLAY "Water Damage Diagnostics ($40)? (Y/N): ".
           ACCEPT WATER-DAMAGE.

           IF FIX-SCREEN
               MOVE 180.00 TO SCREEN-FEE
           END-IF.
           IF FIX-BATTERY
               MOVE 65.00 TO BATT-FEE
           END-IF.
           IF DIAGNOSE
               MOVE 40.00 TO DIAG-FEE
           END-IF.

           COMPUTE TOTAL-COST = SCREEN-FEE + BATT-FEE + DIAG-FEE.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "            REPAIR TICKET               "
           DISPLAY "========================================"
           DISPLAY "Customer: " CUSTOMER
           DISPLAY "Device:   " PHONE-MODEL
           DISPLAY "----------------------------------------"
           IF FIX-SCREEN
               MOVE SCREEN-FEE TO DISP
               DISPLAY "Screen Replacement: " DISP
           END-IF.
           IF FIX-BATTERY
               MOVE BATT-FEE TO DISP
               DISPLAY "Battery Install:    " DISP
           END-IF.
           IF DIAGNOSE
               MOVE DIAG-FEE TO DISP
               DISPLAY "Water Diagnostic:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-COST TO DISP.
           DISPLAY "TOTAL BALANCE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
