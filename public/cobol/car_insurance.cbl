       IDENTIFICATION DIVISION.
       PROGRAM-ID. CAR-INSURANCE.
       AUTHOR. ANTIGRAVITY.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 APP-DATA.
          05 DRIVER-NAME     PIC X(25).
          05 DRIVER-AGE      PIC 9(3).
          05 CAR-TYPE        PIC 9.
             88 SEDAN        VALUE 1.
             88 SPORTS       VALUE 2.
             88 SUV          VALUE 3.
          05 PREV-ACCIDENTS  PIC 9(2).

       01 PREMIUM-CALCS.
          05 BASE-PREMIUM    PIC 9(4)V99 VALUE 600.00.
          05 AGE-RISK        PIC 9(3)V99 VALUE ZERO.
          05 CAR-RISK        PIC 9(3)V99 VALUE ZERO.
          05 ACCIDENT-RISK   PIC 9(4)V99 VALUE ZERO.
          05 TOTAL-ANNUAL    PIC 9(5)V99 VALUE ZERO.
          05 MONTHLY-PAY     PIC 9(4)V99 VALUE ZERO.

       01 DISP               PIC $Z,ZZ9.99.

       PROCEDURE DIVISION.
       START-QUOTE.
           DISPLAY "--- SAFE-DRIVE AUTO INSURANCE ---".
           DISPLAY "Driver Name: ".
           ACCEPT DRIVER-NAME.
           DISPLAY "Driver Age: ".
           ACCEPT DRIVER-AGE.
           DISPLAY "Vehicle (1=Sedan, 2=Sports Car, 3=SUV): ".
           ACCEPT CAR-TYPE.
           DISPLAY "Number of Accidents in last 3 years: ".
           ACCEPT PREV-ACCIDENTS.

           IF DRIVER-AGE < 25
               MOVE 300.00 TO AGE-RISK
           ELSE IF DRIVER-AGE > 65
               MOVE 150.00 TO AGE-RISK
           END-IF.

           EVALUATE TRUE
               WHEN SEDAN
                   MOVE 50.00 TO CAR-RISK
               WHEN SPORTS
                   MOVE 400.00 TO CAR-RISK
               WHEN SUV
                   MOVE 120.00 TO CAR-RISK
               WHEN OTHER
                   MOVE 50.00 TO CAR-RISK
           END-EVALUATE.

           IF PREV-ACCIDENTS > 0
               COMPUTE ACCIDENT-RISK = PREV-ACCIDENTS * 250.00
           END-IF.

           COMPUTE TOTAL-ANNUAL = BASE-PREMIUM + AGE-RISK 
                                + CAR-RISK + ACCIDENT-RISK.
           COMPUTE MONTHLY-PAY = TOTAL-ANNUAL / 12.

           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "         ANNUAL POLICY QUOTE            "
           DISPLAY "========================================"
           DISPLAY "Driver: " DRIVER-NAME
           DISPLAY "----------------------------------------"
           MOVE BASE-PREMIUM TO DISP.
           DISPLAY "Base Premium Rate:  " DISP.
           IF AGE-RISK > 0
               MOVE AGE-RISK TO DISP
               DISPLAY "Age Risk Factor:    " DISP
           END-IF.
           MOVE CAR-RISK TO DISP.
           DISPLAY "Vehicle Risk Class: " DISP.
           IF ACCIDENT-RISK > 0
               MOVE ACCIDENT-RISK TO DISP
               DISPLAY "Accident History:   " DISP
           END-IF.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-ANNUAL TO DISP.
           DISPLAY "TOTAL ANNUAL COST:  " DISP.
           MOVE MONTHLY-PAY TO DISP.
           DISPLAY "EST MONTHLY COST:   " DISP.
           DISPLAY "========================================".
           STOP RUN.
