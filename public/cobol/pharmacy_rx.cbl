       IDENTIFICATION DIVISION.
       PROGRAM-ID. PHARMACY-RX.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 PATIENT-REC.
          05 PATIENT-NAME    PIC X(25).
          05 INSUR-PROVIDER  PIC X.
             88 HAS-INSURANCE VALUE 'Y'.
          05 MED-TYPE        PIC 9.
             88 GENERIC-MED  VALUE 1.
             88 BRAND-MED    VALUE 2.
             88 SPECIALTY    VALUE 3.
          05 REFILL-MONTHS   PIC 9(2) VALUE 1.

       01 COSTS.
          05 BASE-PRICE      PIC 9(4)V99 VALUE ZERO.
          05 COPAY-AMT       PIC 9(3)V99 VALUE ZERO.
          05 TOTAL-CHARGE    PIC 9(5)V99 VALUE ZERO.
          
       01 DISP-AMT           PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       APP-ENTRY.
           DISPLAY "--- CORNERSTONE PHARMACY RX ---".
           DISPLAY "Patient Name: ".
           ACCEPT PATIENT-NAME.
           DISPLAY "Type of Medication: ".
           DISPLAY "1=Generic ($25), 2=Brand ($150), 3=Specialty ($800)".
           ACCEPT MED-TYPE.
           DISPLAY "Does patient have insurance? (Y/N): ".
           ACCEPT INSUR-PROVIDER.
           DISPLAY "Number of months supply (1-12): ".
           ACCEPT REFILL-MONTHS.

           PERFORM CALC-RX.
           PERFORM PRINT-LABEL.
           STOP RUN.

       CALC-RX.
           EVALUATE TRUE
               WHEN GENERIC-MED
                   MOVE 25.00 TO BASE-PRICE
               WHEN BRAND-MED
                   MOVE 150.00 TO BASE-PRICE
               WHEN SPECIALTY
                   MOVE 800.00 TO BASE-PRICE
               WHEN OTHER
                   MOVE 25.00 TO BASE-PRICE
           END-EVALUATE.

           COMPUTE TOTAL-CHARGE = BASE-PRICE * REFILL-MONTHS.

           IF HAS-INSURANCE
               EVALUATE TRUE
                   WHEN GENERIC-MED
                       COMPUTE COPAY-AMT = 10.00 * REFILL-MONTHS
                   WHEN BRAND-MED
                       COMPUTE COPAY-AMT = 40.00 * REFILL-MONTHS
                   WHEN SPECIALTY
                       COMPUTE COPAY-AMT = 100.00 * REFILL-MONTHS
               END-EVALUATE
               
               IF COPAY-AMT > TOTAL-CHARGE
                   MOVE TOTAL-CHARGE TO COPAY-AMT
               END-IF
               
               MOVE COPAY-AMT TO TOTAL-CHARGE
           END-IF.

       PRINT-LABEL.
           DISPLAY " "
           DISPLAY "======================================="
           DISPLAY "         PRESCRIPTION LABEL            "
           DISPLAY "======================================="
           DISPLAY "Patient: " PATIENT-NAME
           DISPLAY "Supply:  " REFILL-MONTHS " Month(s)"
           DISPLAY "---------------------------------------"
           
           COMPUTE BASE-PRICE = BASE-PRICE * REFILL-MONTHS.
           MOVE BASE-PRICE TO DISP-AMT.
           DISPLAY "Retail Value:         " DISP-AMT.
           
           IF HAS-INSURANCE
               DISPLAY "Insurance Applied:    YES"
           ELSE
               DISPLAY "Insurance Applied:    NO"
           END-IF.
           DISPLAY "---------------------------------------"
           MOVE TOTAL-CHARGE TO DISP-AMT.
           DISPLAY "PATIENT RESPONSIBILITY: " DISP-AMT.
           DISPLAY "=======================================".
