       IDENTIFICATION DIVISION.
       PROGRAM-ID. VEHICLE-SERVICE.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 VEHICLE-INFO.
          05 LICENSE-PLATE   PIC X(10).
          05 MILEAGE         PIC 9(6).
          05 LABOR-HOURS     PIC 9(2)V9.

       01 SERVICE-FLAGS.
          05 OIL-CHANGE      PIC X.
          05 TIRE-ROTATE     PIC X.
          05 INSPECTION      PIC X.

       01 COSTS.
          05 LABOR-COST      PIC 9(4)V99 VALUE ZERO.
          05 PARTS-COST      PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-ESTIMATE  PIC 9(5)V99 VALUE ZERO.

       01 PRINT-FMT          PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-GARAGE.
           DISPLAY "--- FAST LANE AUTO REPAIR ---".
           DISPLAY "Vehicle License Plate: ".
           ACCEPT LICENSE-PLATE.
           DISPLAY "Current Mileage: ".
           ACCEPT MILEAGE.

           DISPLAY "Oil Change ($45)? (Y/N): ".
           ACCEPT OIL-CHANGE.
           DISPLAY "Tire Rotation ($25)? (Y/N): ".
           ACCEPT TIRE-ROTATE.
           DISPLAY "State Inspection ($35)? (Y/N): ".
           ACCEPT INSPECTION.
           DISPLAY "Estimated Labor Hours ($80/hr): ".
           ACCEPT LABOR-HOURS.

           PERFORM CALC-ESTIMATE.
           PERFORM PRINT-INVOICE.
           STOP RUN.

       CALC-ESTIMATE.
           COMPUTE LABOR-COST = LABOR-HOURS * 80.00.
           MOVE ZERO TO PARTS-COST.
           
           IF OIL-CHANGE = 'Y' OR 'y'
               ADD 45.00 TO PARTS-COST
           END-IF.
           
           IF TIRE-ROTATE = 'Y' OR 'y'
               ADD 25.00 TO PARTS-COST
           END-IF.
           
           IF INSPECTION = 'Y' OR 'y'
               ADD 35.00 TO PARTS-COST
           END-IF.
           
           COMPUTE TOTAL-ESTIMATE = LABOR-COST + PARTS-COST.

       PRINT-INVOICE.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          SERVICE INVOICE               "
           DISPLAY "========================================"
           DISPLAY "License: " LICENSE-PLATE " | Mileage: " MILEAGE
           DISPLAY "----------------------------------------"
           IF OIL-CHANGE = 'Y' OR 'y'
               DISPLAY " - Oil & Filter Replacement: $45.00"
           END-IF
           IF TIRE-ROTATE = 'Y' OR 'y'
               DISPLAY " - Tire Rotation:            $25.00"
           END-IF
           IF INSPECTION = 'Y' OR 'y'
               DISPLAY " - State Safety Inspection:  $35.00"
           END-IF
           DISPLAY "----------------------------------------"
           MOVE PARTS-COST TO PRINT-FMT.
           DISPLAY "Total Parts/Services: " PRINT-FMT.
           MOVE LABOR-COST TO PRINT-FMT.
           DISPLAY "Labor Cost:           " PRINT-FMT.
           DISPLAY "========================================"
           MOVE TOTAL-ESTIMATE TO PRINT-FMT.
           DISPLAY "FINAL ESTIMATE:       " PRINT-FMT.
           DISPLAY "========================================".
