       IDENTIFICATION DIVISION.
       PROGRAM-ID. DRONE-RENTAL.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RENTAL-INFO.
          05 CUST-NAME       PIC X(20).
          05 DRONE-MODEL     PIC 9.
             88 BASIC-CAM    VALUE 1.
             88 PRO-4K       VALUE 2.
             88 CINEMA-8K    VALUE 3.
          05 DAYS-RNT        PIC 9(2).
          05 EXTRA-BATT      PIC 9(2) VALUE ZERO.
          05 INSURE-WVT      PIC X.
             88 WANTS-INS    VALUE 'Y'.

       01 FEES.
          05 DAILY-RATE      PIC 9(3)V99 VALUE ZERO.
          05 DRONE-TOT       PIC 9(4)V99 VALUE ZERO.
          05 BATT-TOT        PIC 9(3)V99 VALUE ZERO.
          05 INSURE-TOT      PIC 9(3)V99 VALUE ZERO.
          05 GRAND-TOT       PIC 9(5)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-ENTRY.
           DISPLAY "--- AERO CAPTURE DRONE RENTALS ---".
           DISPLAY "Renter Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Drone (1=Basic $40, 2=Pro 4K $90, 3=Cinema $250): ".
           ACCEPT DRONE-MODEL.
           DISPLAY "Days to Rent: ".
           ACCEPT DAYS-RNT.
           DISPLAY "Extra Battery Packs ($10/day ea): ".
           ACCEPT EXTRA-BATT.
           DISPLAY "Add Crash Insurance ($25/day)? (Y/N): ".
           ACCEPT INSURE-WVT.

           EVALUATE TRUE
               WHEN BASIC-CAM
                   MOVE 40.00 TO DAILY-RATE
               WHEN PRO-4K
                   MOVE 90.00 TO DAILY-RATE
               WHEN CINEMA-8K
                   MOVE 250.00 TO DAILY-RATE
               WHEN OTHER
                   MOVE 40.00 TO DAILY-RATE
           END-EVALUATE.

           COMPUTE DRONE-TOT = DAILY-RATE * DAYS-RNT.
           COMPUTE BATT-TOT = (EXTRA-BATT * 10.00) * DAYS-RNT.

           IF WANTS-INS
               COMPUTE INSURE-TOT = 25.00 * DAYS-RNT
           END-IF.

           COMPUTE GRAND-TOT = DRONE-TOT + BATT-TOT + INSURE-TOT.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "          RENTAL AGREEMENT              "
           DISPLAY "========================================"
           DISPLAY "Renter: " CUST-NAME
           DISPLAY "Terms:  " DAYS-RNT " Day(s)"
           DISPLAY "----------------------------------------"
           MOVE DRONE-TOT TO DISP.
           DISPLAY "Drone Flight Time:  " DISP.
           
           IF EXTRA-BATT > 0
               MOVE BATT-TOT TO DISP
               DISPLAY "Extra Power Packs:  " DISP
           END-IF.
           
           IF WANTS-INS
               MOVE INSURE-TOT TO DISP
               DISPLAY "Crash Insurance:    " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE GRAND-TOT TO DISP.
           DISPLAY "TOTAL BALANCE:      " DISP.
           DISPLAY "========================================".
           STOP RUN.
