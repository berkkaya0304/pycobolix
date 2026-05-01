       IDENTIFICATION DIVISION.
       PROGRAM-ID. WATER-BILL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WATER-USAGE.
          05 CUST-NAME       PIC X(25).
          05 GALS-USED       PIC 9(6).
          05 SEWER-LINK      PIC X.
             88 HAS-SEWER    VALUE 'Y'.

       01 CHARGES.
          05 BASE-CONN-FEE   PIC 9(2)V99 VALUE 24.50.
          05 USAGE-FEE       PIC 9(4)V99 VALUE ZERO.
          05 SEWER-FEE       PIC 9(4)V99 VALUE ZERO.
          05 GRAND-TOTAL     PIC 9(5)V99 VALUE ZERO.

       01 F-AMT              PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-ENTRY.
           DISPLAY "--- MUNICIPAL WATER DEPT ---".
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Water usage for cycle (Gallons): ".
           ACCEPT GALS-USED.
           DISPLAY "Connected to City Sewer? (Y/N): ".
           ACCEPT SEWER-LINK.

           PERFORM PROCESS-BILL.
           PERFORM PRINT-INVOICE.
           STOP RUN.

       PROCESS-BILL.
           IF GALS-USED <= 5000
               COMPUTE USAGE-FEE = (GALS-USED / 1000) * 3.50
           ELSE IF GALS-USED <= 10000
               COMPUTE USAGE-FEE = (5000 / 1000 * 3.50) + 
                                   ((GALS-USED - 5000) / 1000 * 4.75)
           ELSE
               COMPUTE USAGE-FEE = (5000 / 1000 * 3.50) + 
                                   (5000 / 1000 * 4.75) +
                                   ((GALS-USED - 10000) / 1000 * 6.50)
           END-IF.

           IF HAS-SEWER
               COMPUTE SEWER-FEE = USAGE-FEE * 0.80
           END-IF.

           COMPUTE GRAND-TOTAL = BASE-CONN-FEE + USAGE-FEE + SEWER-FEE.

       PRINT-INVOICE.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "          WATER UTILITY BILL           "
           DISPLAY "======================================="
           DISPLAY "Account Name: " CUST-NAME
           DISPLAY "Consumption:  " GALS-USED " Gallons"
           DISPLAY "---------------------------------------"
           MOVE BASE-CONN-FEE TO F-AMT.
           DISPLAY "Base Connection Fee: " F-AMT.
           MOVE USAGE-FEE TO F-AMT.
           DISPLAY "Tiered Water Usage:  " F-AMT.
           
           IF HAS-SEWER
               MOVE SEWER-FEE TO F-AMT
               DISPLAY "Sewer & Wastewater:  " F-AMT
           END-IF.
           DISPLAY "---------------------------------------"
           MOVE GRAND-TOTAL TO F-AMT.
           DISPLAY "TOTAL AMOUNT DUE:    " F-AMT.
           DISPLAY "=======================================".
