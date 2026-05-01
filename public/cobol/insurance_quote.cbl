       IDENTIFICATION DIVISION.
       PROGRAM-ID. INSURANCE-QUOTE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 DRIVER-INFO.
          05 D-NAME          PIC X(25).
          05 D-AGE           PIC 9(2).
          05 ACCIDENTS       PIC 9(2).
          05 CAR-VALUE       PIC 9(6)V99.

       01 PREMIUM-CALCS.
          05 BASE-PREMIUM    PIC 9(4)V99 VALUE 500.00.
          05 AGE-RISK        PIC 9(4)V99 VALUE ZERO.
          05 ACCIDENT-RISK   PIC 9(4)V99 VALUE ZERO.
          05 VALUE-INDEX     PIC 9(4)V99 VALUE ZERO.
          05 FINAL-QUOTE     PIC 9(5)V99 VALUE ZERO.
          05 MONTHLY-P       PIC 9(4)V99 VALUE ZERO.

       01 DISP-MONEY         PIC $Z,ZZZ.99.

       PROCEDURE DIVISION.
       START-SYSTEM.
           DISPLAY "--- SAFE DRIVE INSURANCE QUOTE ---".
           DISPLAY "Driver Name: ".
           ACCEPT D-NAME.
           DISPLAY "Driver Age: ".
           ACCEPT D-AGE.
           DISPLAY "Number of accidents in last 3 years: ".
           ACCEPT ACCIDENTS.
           DISPLAY "Current Vehicle Value ($): ".
           ACCEPT CAR-VALUE.

           PERFORM CALC-QUOTE.
           PERFORM ISSUE-QUOTE.
           STOP RUN.

       CALC-QUOTE.
           IF D-AGE < 25
               MOVE 300.00 TO AGE-RISK
           ELSE IF D-AGE > 65
               MOVE 150.00 TO AGE-RISK
           ELSE
               MOVE ZERO TO AGE-RISK
           END-IF.

           COMPUTE ACCIDENT-RISK = ACCIDENTS * 250.00.
           COMPUTE VALUE-INDEX = CAR-VALUE * 0.015.

           COMPUTE FINAL-QUOTE = BASE-PREMIUM + AGE-RISK 
                               + ACCIDENT-RISK + VALUE-INDEX.
                               
           COMPUTE MONTHLY-P = FINAL-QUOTE / 12.

       ISSUE-QUOTE.
           DISPLAY " "
           DISPLAY "========================================="
           DISPLAY "       COMPREHENSIVE AUTO POLICY         "
           DISPLAY "========================================="
           DISPLAY "Insured Name: " D-NAME " (Age: " D-AGE ")"
           DISPLAY "Vehicle Est: $" CAR-VALUE
           DISPLAY "-----------------------------------------"
           MOVE BASE-PREMIUM TO DISP-MONEY.
           DISPLAY "Base Premium:       " DISP-MONEY.
           MOVE VALUE-INDEX TO DISP-MONEY.
           DISPLAY "Value Adjustment:  +" DISP-MONEY.
           IF AGE-RISK > 0
               MOVE AGE-RISK TO DISP-MONEY
               DISPLAY "Age Surcharge:     +" DISP-MONEY
           END-IF.
           IF ACCIDENT-RISK > 0
               MOVE ACCIDENT-RISK TO DISP-MONEY
               DISPLAY "Accident Penalty:  +" DISP-MONEY
           END-IF.
           DISPLAY "-----------------------------------------"
           MOVE FINAL-QUOTE TO DISP-MONEY.
           DISPLAY "ANNUAL PREMIUM:     " DISP-MONEY.
           MOVE MONTHLY-P TO DISP-MONEY.
           DISPLAY "MONTHLY RATE:       " DISP-MONEY.
           DISPLAY "=========================================".
