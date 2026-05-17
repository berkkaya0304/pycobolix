       IDENTIFICATION DIVISION.
       PROGRAM-ID. CREDIT-CARD.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ACCOUNT-STATUS.
          05 CARD-NUMBER     PIC X(16).
          05 CARDHOLDER      PIC X(30).
          05 PREV-BALANCE    PIC 9(5)V99.
          05 NEW-CHARGES     PIC 9(5)V99.
          05 PAYMENTS-MADE   PIC 9(5)V99.

       01 CALCS.
          05 APR-RATE        PIC 9(2)V99 VALUE 19.99.
          05 UNPAID-BAL      PIC 9(6)V99.
          05 INTEREST-CHG    PIC 9(4)V99 VALUE ZERO.
          05 NEW-BALANCE     PIC 9(6)V99.
          05 MIN-PAYMENT     PIC 9(4)V99.

       01 DISP-V             PIC $ZZ,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "--- CREDIT CARD STATEMENT GEN ---".
           DISPLAY "Card Number: ".
           ACCEPT CARD-NUMBER.
           DISPLAY "Cardholder Name: ".
           ACCEPT CARDHOLDER.
           DISPLAY "Previous Statement Balance: ".
           ACCEPT PREV-BALANCE.
           DISPLAY "Payments Made This Cycle: ".
           ACCEPT PAYMENTS-MADE.
           DISPLAY "New Purchase Charges: ".
           ACCEPT NEW-CHARGES.

           PERFORM CALC-STATEMENT.
           PERFORM PRINT-STATEMENT.
           STOP RUN.

       CALC-STATEMENT.
           COMPUTE UNPAID-BAL = PREV-BALANCE - PAYMENTS-MADE.
           
           IF UNPAID-BAL > 0
               COMPUTE INTEREST-CHG = UNPAID-BAL * (APR-RATE / 100 / 12)
           END-IF.

           COMPUTE NEW-BALANCE = UNPAID-BAL + NEW-CHARGES 
                               + INTEREST-CHG.

           COMPUTE MIN-PAYMENT = NEW-BALANCE * 0.03.
           IF MIN-PAYMENT < 35.00 AND NEW-BALANCE >= 35.00
               MOVE 35.00 TO MIN-PAYMENT
           ELSE IF NEW-BALANCE < 35.00
               MOVE NEW-BALANCE TO MIN-PAYMENT
           END-IF.

       PRINT-STATEMENT.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "       MONTHLY ACCOUNT STATEMENT         "
           DISPLAY "========================================="
           DISPLAY "Card: **** **** **** " CARD-NUMBER(13:4)
           DISPLAY "Name: " CARDHOLDER
           DISPLAY "-----------------------------------------"
           MOVE PREV-BALANCE TO DISP-V.
           DISPLAY "Previous Balance:    " DISP-V.
           MOVE PAYMENTS-MADE TO DISP-V.
           DISPLAY "Payments / Credits: -" DISP-V.
           MOVE NEW-CHARGES TO DISP-V.
           DISPLAY "New Purchases:      +" DISP-V.
           MOVE INTEREST-CHG TO DISP-V.
           DISPLAY "Interest Charged:   +" DISP-V.
           DISPLAY "-----------------------------------------"
           MOVE NEW-BALANCE TO DISP-V.
           DISPLAY "NEW BALANCE:         " DISP-V.
           MOVE MIN-PAYMENT TO DISP-V.
           DISPLAY "MINIMUM PAYMENT DUE: " DISP-V.
           DISPLAY "=========================================".
