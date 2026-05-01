       IDENTIFICATION DIVISION.
       PROGRAM-ID. PHONE-BILL.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ACCOUNT-INFO.
          05 PHONE-NUM       PIC 9(10).
          05 PLAN-TYPE       PIC X.
             88 BASIC-PLAN   VALUE 'B'.
             88 UNLIMITED    VALUE 'U'.
          
       01 USAGE-DATA.
          05 DATA-USED-GB    PIC 9(3)V99.
          05 INTL-MINUTES    PIC 9(4).
          
       01 FEES.
          05 BASE-CHARGE     PIC 9(3)V99 VALUE ZERO.
          05 OVERAGE-CHARGE  PIC 9(3)V99 VALUE ZERO.
          05 INTL-CHARGE     PIC 9(3)V99 VALUE ZERO.
          05 TAXES           PIC 9(2)V99 VALUE ZERO.
          05 TOTAL-BILL      PIC 9(4)V99 VALUE ZERO.

       01 DISP-NUM           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-BILLING.
           DISPLAY "--- TELECOM MONTHLY STATEMENT ---".
           DISPLAY "Phone Number: ".
           ACCEPT PHONE-NUM.
           DISPLAY "Plan (B=Basic 5GB $30, U=Unlimited $70): ".
           ACCEPT PLAN-TYPE.
           DISPLAY "Total Data Used (GB): ".
           ACCEPT DATA-USED-GB.
           DISPLAY "International Calling Minutes: ".
           ACCEPT INTL-MINUTES.

           PERFORM CALCULATE-BILL.
           PERFORM PRINT-BILL.
           STOP RUN.

       CALCULATE-BILL.
           EVALUATE TRUE
               WHEN BASIC-PLAN
                   MOVE 30.00 TO BASE-CHARGE
                   IF DATA-USED-GB > 5.00
                       COMPUTE OVERAGE-CHARGE = (DATA-USED-GB - 5.00) 
                                              * 10.00
                   END-IF
               WHEN UNLIMITED
                   MOVE 70.00 TO BASE-CHARGE
                   MOVE ZERO TO OVERAGE-CHARGE
               WHEN OTHER
                   MOVE 30.00 TO BASE-CHARGE
           END-EVALUATE.

           COMPUTE INTL-CHARGE = INTL-MINUTES * 0.25.

           COMPUTE TOTAL-BILL = BASE-CHARGE + OVERAGE-CHARGE 
                              + INTL-CHARGE.
           COMPUTE TAXES = TOTAL-BILL * 0.12.
           ADD TAXES TO TOTAL-BILL.

       PRINT-BILL.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "          MONTHLY INVOICE              "
           DISPLAY "======================================="
           DISPLAY "Mobile Number: " PHONE-NUM
           DISPLAY "---------------------------------------"
           MOVE BASE-CHARGE TO DISP-NUM.
           DISPLAY "Plan Base Charge:    " DISP-NUM.
           IF OVERAGE-CHARGE > 0
               MOVE OVERAGE-CHARGE TO DISP-NUM
               DISPLAY "Data Overage Fees:   " DISP-NUM
           END-IF.
           IF INTL-CHARGE > 0
               MOVE INTL-CHARGE TO DISP-NUM
               DISPLAY "Int'l Call Charges:  " DISP-NUM
           END-IF.
           DISPLAY "---------------------------------------"
           MOVE TAXES TO DISP-NUM.
           DISPLAY "Taxes & Surcharges:  " DISP-NUM.
           MOVE TOTAL-BILL TO DISP-NUM.
           DISPLAY "TOTAL AMOUNT DUE:    " DISP-NUM.
           DISPLAY "=======================================".
