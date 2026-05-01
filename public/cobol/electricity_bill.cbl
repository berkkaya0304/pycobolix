       IDENTIFICATION DIVISION.
       PROGRAM-ID. ELECTRIC-BILL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 METER-READINGS.
          05 ACCOUNT-ID      PIC X(12).
          05 PEAK-KWH        PIC 9(5).
          05 OFF-PEAK-KWH    PIC 9(5).
          05 SOLAR-CREDIT    PIC 9(5).

       01 RATES.
          05 PEAK-RATE       PIC 9V99 VALUE 0.25.
          05 OFF-PEAK-RATE   PIC 9V99 VALUE 0.12.
          05 SOLAR-BUYBACK   PIC 9V99 VALUE 0.10.

       01 AMOUNTS.
          05 PEAK-COST       PIC 9(5)V99.
          05 OFF-PEAK-COST   PIC 9(5)V99.
          05 SUB-TOTAL       PIC 9(5)V99.
          05 SOLAR-DEDUCT    PIC 9(5)V99.
          05 TOTAL-DUE       PIC S9(5)V99.

       01 D-OUT              PIC -$Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       BILLING-START.
           DISPLAY "--- GRID-CONNECT ENERGY BILLING ---".
           DISPLAY "Account ID: ".
           ACCEPT ACCOUNT-ID.
           DISPLAY "Peak Hours Usage (kWh): ".
           ACCEPT PEAK-KWH.
           DISPLAY "Off-Peak Hours Usage (kWh): ".
           ACCEPT OFF-PEAK-KWH.
           DISPLAY "Solar Generated Back to Grid (kWh): ".
           ACCEPT SOLAR-CREDIT.

           PERFORM COMPUTE-BILL.
           PERFORM PRINT-BILL.
           STOP RUN.

       COMPUTE-BILL.
           COMPUTE PEAK-COST = PEAK-KWH * PEAK-RATE.
           COMPUTE OFF-PEAK-COST = OFF-PEAK-KWH * OFF-PEAK-RATE.
           COMPUTE SUB-TOTAL = PEAK-COST + OFF-PEAK-COST.

           COMPUTE SOLAR-DEDUCT = SOLAR-CREDIT * SOLAR-BUYBACK.
           COMPUTE TOTAL-DUE = SUB-TOTAL - SOLAR-DEDUCT.

       PRINT-BILL.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "        MONTHLY ELECTRIC STATEMENT       "
           DISPLAY "========================================="
           DISPLAY "Account No: " ACCOUNT-ID
           DISPLAY "-----------------------------------------"
           MOVE PEAK-COST TO D-OUT.
           DISPLAY "Peak Usage (" PEAK-KWH " kWh):     " D-OUT.
           MOVE OFF-PEAK-COST TO D-OUT.
           DISPLAY "Off-Peak Usage (" OFF-PEAK-KWH " kWh): " D-OUT.
           DISPLAY "-----------------------------------------"
           MOVE SUB-TOTAL TO D-OUT.
           DISPLAY "Gross Energy Charge:      " D-OUT.
           MOVE SOLAR-DEDUCT TO D-OUT.
           DISPLAY "Solar Credit (" SOLAR-CREDIT " kWh): -" D-OUT.
           DISPLAY "-----------------------------------------"
           MOVE TOTAL-DUE TO D-OUT.
           IF TOTAL-DUE < 0
               DISPLAY "CREDIT APPLIED TO ACCT:   " D-OUT
           ELSE
               DISPLAY "TOTAL CURRENT CHARGES:    " D-OUT
           END-IF.
           DISPLAY "=========================================".
