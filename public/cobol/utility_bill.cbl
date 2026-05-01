       IDENTIFICATION DIVISION.
       PROGRAM-ID. UTILITY-BILL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ACCOUNT-INFO.
          05 ACCT-NUM        PIC 9(8).
          05 CUST-NAME       PIC X(30).

       01 USAGE-DATA.
          05 ELEC-KWH        PIC 9(5).
          05 WATER-GAL       PIC 9(5).

       01 BILL-CALCS.
          05 ELEC-BASE       PIC 9(3)V99 VALUE 20.00.
          05 ELEC-CHG        PIC 9(4)V99 VALUE ZERO.
          
          05 WATER-BASE      PIC 9(3)V99 VALUE 15.00.
          05 WATER-CHG       PIC 9(4)V99 VALUE ZERO.

          05 TOTAL-CHG       PIC 9(5)V99 VALUE ZERO.
          05 LATE-FEE        PIC 9(2)V99 VALUE 10.00.
          05 INCL-LATE       PIC X.
          05 FINAL-DUE       PIC 9(5)V99.

       01 DISP             PIC $ZZ,ZZ9.99.

       PROCEDURE DIVISION.
       MAINLINE.
           DISPLAY "--- CITY UTILITIES BILLING ---".
           DISPLAY "Account Number: ".
           ACCEPT ACCT-NUM.
           DISPLAY "Customer Name: ".
           ACCEPT CUST-NAME.
           DISPLAY "Electricity Used (kWh): ".
           ACCEPT ELEC-KWH.
           DISPLAY "Water Used (Gallons): ".
           ACCEPT WATER-GAL.
           DISPLAY "Apply late fee? (Y/N): ".
           ACCEPT INCL-LATE.

           PERFORM CALCULATE-CHARGES.
           PERFORM OUTPUT-INVOICE.
           STOP RUN.

       CALCULATE-CHARGES.
           IF ELEC-KWH <= 500
               COMPUTE ELEC-CHG = ELEC-KWH * 0.12
           ELSE
               COMPUTE ELEC-CHG = (500 * 0.12) 
                                + ((ELEC-KWH - 500) * 0.15)
           END-IF.

           COMPUTE WATER-CHG = (WATER-GAL / 100) * 0.25.

           COMPUTE TOTAL-CHG = ELEC-BASE + ELEC-CHG 
                             + WATER-BASE + WATER-CHG.

           IF INCL-LATE = 'Y' OR 'y'
               COMPUTE FINAL-DUE = TOTAL-CHG + LATE-FEE
           ELSE
               MOVE ZERO TO LATE-FEE
               COMPUTE FINAL-DUE = TOTAL-CHG
           END-IF.

       OUTPUT-INVOICE.
           DISPLAY " "
           DISPLAY "****************************************"
           DISPLAY "        MONTHLY UTILITY BILL            "
           DISPLAY "****************************************"
           DISPLAY "Account: " ACCT-NUM.
           DISPLAY "Name:    " CUST-NAME.
           DISPLAY "----------------------------------------"
           MOVE ELEC-BASE TO DISP.
           DISPLAY "ELEC Base Fee:       " DISP.
           MOVE ELEC-CHG TO DISP.
           DISPLAY "ELEC Usage Charge:   " DISP.
           DISPLAY "  (Usage: " ELEC-KWH " kWh)".
           DISPLAY "----------------------------------------"
           MOVE WATER-BASE TO DISP.
           DISPLAY "WATER Base Fee:      " DISP.
           MOVE WATER-CHG TO DISP.
           DISPLAY "WATER Usage Charge:  " DISP.
           DISPLAY "  (Usage: " WATER-GAL " gals)".
           DISPLAY "----------------------------------------"
           
           IF LATE-FEE > 0
               MOVE LATE-FEE TO DISP
               DISPLAY "Prior Bal Late Fee:  " DISP
           END-IF.
           
           MOVE FINAL-DUE TO DISP.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP.
           DISPLAY "****************************************".
