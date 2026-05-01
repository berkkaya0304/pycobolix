       IDENTIFICATION DIVISION.
       PROGRAM-ID. REAL-ESTATE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PROPERTY-INFO.
          05 PROP-ADDRESS    PIC X(40).
          05 PROP-PRICE      PIC 9(7)V99.
          05 DOWN-PMT-PCT    PIC 9(2)V99.

       01 LOAN-DETAILS.
          05 DOWN-PMT-AMT    PIC 9(7)V99.
          05 LOAN-PRINCIPAL  PIC 9(7)V99.
          05 INT-RATE        PIC 9(2)V99 VALUE 5.50.
          05 LOAN-YEARS      PIC 9(2) VALUE 30.
          05 TOTAL-INT       PIC 9(8)V99.
          05 TOTAL-PAYBACK   PIC 9(8)V99.

       01 MONTHLY-CALCS.
          05 TOTAL-MONTHS    PIC 9(3).
          05 MONTHLY-PMT     PIC 9(5)V99.
          05 PMI-FEE        PIC 9(4)V99 VALUE ZERO.

       01 FMT-CURR           PIC $Z,ZZZ,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-MORTGAGE.
           DISPLAY "--- MORTGAGE CALCULATOR ---".
           DISPLAY "Property Address: ".
           ACCEPT PROP-ADDRESS.
           DISPLAY "Property Purchase Price ($): ".
           ACCEPT PROP-PRICE.
           DISPLAY "Down Payment Percentage (e.g., 20 for 20%): ".
           ACCEPT DOWN-PMT-PCT.
           DISPLAY "Interest Rate (e.g., 5.5 for 5.5%): ".
           ACCEPT INT-RATE.
           DISPLAY "Loan Term (Years): ".
           ACCEPT LOAN-YEARS.

           PERFORM PROCESS-LOAN.
           PERFORM PRINT-BREAKDOWN.
           STOP RUN.

       PROCESS-LOAN.
           COMPUTE DOWN-PMT-AMT = PROP-PRICE * (DOWN-PMT-PCT / 100).
           COMPUTE LOAN-PRINCIPAL = PROP-PRICE - DOWN-PMT-AMT.
           
           IF DOWN-PMT-PCT < 20
               COMPUTE PMI-FEE = (LOAN-PRINCIPAL * .01) / 12
               DISPLAY "*** WARNING: PMI applies (Down Payment < 20%) ***"
           END-IF.

           * Simplified flat interest calc for demonstration
           COMPUTE TOTAL-INT = LOAN-PRINCIPAL * (INT-RATE / 100) 
                             * LOAN-YEARS.
           COMPUTE TOTAL-PAYBACK = LOAN-PRINCIPAL + TOTAL-INT.
           COMPUTE TOTAL-MONTHS = LOAN-YEARS * 12.
           
           COMPUTE MONTHLY-PMT = (TOTAL-PAYBACK / TOTAL-MONTHS) + PMI-FEE.

       PRINT-BREAKDOWN.
           DISPLAY " "
           DISPLAY "============================================="
           DISPLAY "        MORTGAGE BREAKDOWN ESTIMATE          "
           DISPLAY "============================================="
           DISPLAY "Address: " PROP-ADDRESS.
           DISPLAY "---------------------------------------------"
           MOVE PROP-PRICE TO FMT-CURR.
           DISPLAY "Purchase Price:   " FMT-CURR.
           MOVE DOWN-PMT-AMT TO FMT-CURR.
           DISPLAY "Down Payment:     -" FMT-CURR.
           MOVE LOAN-PRINCIPAL TO FMT-CURR.
           DISPLAY "Loan Principal:   " FMT-CURR.
           DISPLAY "---------------------------------------------"
           MOVE TOTAL-INT TO FMT-CURR.
           DISPLAY "Total Interest:   " FMT-CURR.
           MOVE TOTAL-PAYBACK TO FMT-CURR.
           DISPLAY "Total Repayment:  " FMT-CURR.
           DISPLAY "---------------------------------------------"
           IF PMI-FEE > 0
               MOVE PMI-FEE TO FMT-CURR
               DISPLAY "Monthly PMI Fee:  " FMT-CURR
           END-IF.
           MOVE MONTHLY-PMT TO FMT-CURR.
           DISPLAY "EST. MONTHLY PMT: " FMT-CURR.
           DISPLAY "=============================================".
