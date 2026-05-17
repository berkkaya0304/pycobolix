       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL-SYSTEM.
       AUTHOR. A.

       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 EMP-DETAILS.
          05 EMP-ID          PIC 9(5).
          05 EMP-NAME        PIC X(20).
          05 HOURLY-RATE     PIC 9(4)V99.
          05 HOURS-WORKED    PIC 9(3).
          05 OVERTIME-HOURS  PIC 9(3).
       
       01 CALC-VARS.
          05 REGULAR-PAY     PIC 9(6)V99 VALUE ZERO.
          05 OVERTIME-PAY    PIC 9(6)V99 VALUE ZERO.
          05 GROSS-PAY       PIC 9(6)V99 VALUE ZERO.
          05 TAX-AMOUNT      PIC 9(6)V99 VALUE ZERO.
          05 NET-PAY         PIC 9(6)V99 VALUE ZERO.
          
       01 CONSTANTS.
          05 TAX-RATE        PIC V99 VALUE .15.
          05 OT-MULTIPLIER   PIC 9V9 VALUE 1.5.
          
       01 DISPLAY-VARS.
          05 DISP-GROSS      PIC $Z,ZZZ,ZZ9.99.
          05 DISP-TAX        PIC $Z,ZZZ,ZZ9.99.
          05 DISP-NET        PIC $Z,ZZZ,ZZ9.99.
          05 CONTINUE-FLAG   PIC X VALUE 'Y'.

       PROCEDURE DIVISION.
       MAIN-LOGIC.
           PERFORM UNTIL CONTINUE-FLAG = 'N' OR 'n'
               PERFORM GET-EMPLOYEE-DATA
               PERFORM CALCULATE-PAY
               PERFORM DISPLAY-RESULTS
               DISPLAY "Process another employee? (Y/N): "
               ACCEPT CONTINUE-FLAG
           END-PERFORM.
           DISPLAY "Exiting Payroll System.".
           STOP RUN.

       GET-EMPLOYEE-DATA.
           DISPLAY "--- EMPLOYEE PAYROLL ENTRY ---".
           DISPLAY "Enter Employee ID: ".
           ACCEPT EMP-ID.
           DISPLAY "Enter Employee Name: ".
           ACCEPT EMP-NAME.
           DISPLAY "Enter Hourly Rate: ".
           ACCEPT HOURLY-RATE.
           DISPLAY "Enter Hours Worked (Regular): ".
           ACCEPT HOURS-WORKED.
           DISPLAY "Enter Overtime Hours: ".
           ACCEPT OVERTIME-HOURS.

       CALCULATE-PAY.
           COMPUTE REGULAR-PAY = HOURLY-RATE * HOURS-WORKED.
           COMPUTE OVERTIME-PAY = HOURLY-RATE * OVERTIME-HOURS * 
                                  OT-MULTIPLIER.
           COMPUTE GROSS-PAY = REGULAR-PAY + OVERTIME-PAY.
           COMPUTE TAX-AMOUNT = GROSS-PAY * TAX-RATE.
           COMPUTE NET-PAY = GROSS-PAY - TAX-AMOUNT.

       DISPLAY-RESULTS.
           MOVE GROSS-PAY TO DISP-GROSS.
           MOVE TAX-AMOUNT TO DISP-TAX.
           MOVE NET-PAY TO DISP-NET.
           DISPLAY "---------------------------------".
           DISPLAY "PAYROLL SUMMARY FOR: " EMP-NAME.
           DISPLAY "ID: " EMP-ID.
           DISPLAY "Gross Pay:   " DISP-GROSS.
           DISPLAY "Tax Deduct:  " DISP-TAX.
           DISPLAY "Net Pay:     " DISP-NET.
           DISPLAY "---------------------------------".
