       IDENTIFICATION DIVISION.
       PROGRAM-ID. FLIGHT-LUGGAGE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PASSENGER.
          05 FLIGHT-NUM      PIC X(6).
          05 PASSENGER-ID    PIC X(10).
          
       01 BAG-STATS.
          05 BAG-WEIGHT-KG   PIC 9(3)V99.
          05 BAG-LENGTH      PIC 9(3).
          05 BAG-WIDTH       PIC 9(3).
          05 BAG-HEIGHT      PIC 9(3).

       01 RULES.
          05 MAX-WEIGHT      PIC 9(2) VALUE 23.
          05 MAX-DIM         PIC 9(3) VALUE 158.
          
       01 CALCULATED-FEES.
          05 TOTAL-DIM       PIC 9(4).
          05 WEIGHT-OVR      PIC S9(3)V99.
          05 DIM-OVR         PIC S9(4).
          05 OVER-WT-FEE     PIC 9(3)V99 VALUE ZERO.
          05 OVER-SZ-FEE     PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-FEE       PIC 9(4)V99 VALUE ZERO.

       01 F-C                PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PROC.
           DISPLAY "--- AIRPORT LUGGAGE SCANNER ---".
           DISPLAY "Flight Number: ".
           ACCEPT FLIGHT-NUM.
           DISPLAY "Passenger ID: ".
           ACCEPT PASSENGER-ID.
           DISPLAY "Bag Weight (kg): ".
           ACCEPT BAG-WEIGHT-KG.
           DISPLAY "Bag Length (cm): ".
           ACCEPT BAG-LENGTH.
           DISPLAY "Bag Width (cm): ".
           ACCEPT BAG-WIDTH.
           DISPLAY "Bag Height (cm): ".
           ACCEPT BAG-HEIGHT.

           PERFORM CHECK-BAG.
           PERFORM PRINT-TAG.
           STOP RUN.

       CHECK-BAG.
           COMPUTE TOTAL-DIM = BAG-LENGTH + BAG-WIDTH + BAG-HEIGHT.
           COMPUTE WEIGHT-OVR = BAG-WEIGHT-KG - MAX-WEIGHT.
           COMPUTE DIM-OVR = TOTAL-DIM - MAX-DIM.

           IF WEIGHT-OVR > 0
               COMPUTE OVER-WT-FEE = WEIGHT-OVR * 15.00
           END-IF.

           IF DIM-OVR > 0
               MOVE 50.00 TO OVER-SZ-FEE
           END-IF.

           COMPUTE TOTAL-FEE = OVER-WT-FEE + OVER-SZ-FEE.

       PRINT-TAG.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "           LUGGAGE TAG & FEE           "
           DISPLAY "======================================="
           DISPLAY "Flight: " FLIGHT-NUM " | Pass ID: " PASSENGER-ID
           DISPLAY "---------------------------------------"
           DISPLAY "Bag Weight: " BAG-WEIGHT-KG " kg"
           DISPLAY "Bag Dims:   " TOTAL-DIM " cm total"
           
           IF OVER-WT-FEE > 0 OR OVER-SZ-FEE > 0
               DISPLAY "---------------------------------------"
               DISPLAY ">>> BAG EXCEEDS ALLOWANCE <<<"
               IF OVER-WT-FEE > 0
                   MOVE OVER-WT-FEE TO F-C
                   DISPLAY "Overweight Fee: " F-C
               END-IF
               IF OVER-SZ-FEE > 0
                   MOVE OVER-SZ-FEE TO F-C
                   DISPLAY "Oversized Fee:  " F-C
               END-IF
               DISPLAY "---------------------------------------"
               MOVE TOTAL-FEE TO F-C
               DISPLAY "EXCESS FEES TO PAY: " F-C
           ELSE
               DISPLAY "---------------------------------------"
               DISPLAY "Status: OK TO LOAD (No Fees)"
           END-IF.
           DISPLAY "=======================================".
