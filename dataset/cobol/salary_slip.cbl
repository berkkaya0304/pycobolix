       IDENTIFICATION DIVISION.
       PROGRAM-ID. SALARY-SLIP.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 EMP-RECORD.
          05 EMP-NAME        PIC X(25).
          05 EMP-ID          PIC X(6).
          05 BASIC-PAY       PIC 9(6)V99.

       01 ALLOWANCES.
          05 HRA             PIC 9(5)V99.
          05 DA              PIC 9(5)V99.
          05 TRANSPORT       PIC 9(4)V99 VALUE 150.00.
          05 GROSS-SALARY    PIC 9(7)V99.

       01 DEDUCTIONS.
          05 PF              PIC 9(5)V99.
          05 TAX             PIC 9(5)V99.
          05 MEDICAL         PIC 9(4)V99 VALUE 50.00.
          05 TOTAL-DED       PIC 9(6)V99.

       01 NET-PAY            PIC 9(7)V99.
       01 FMT-VAL            PIC $Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       MAIN-PGM.
           DISPLAY "--- HR SALARY INVOICING ---".
           DISPLAY "Employee Name: ".
           ACCEPT EMP-NAME.
           DISPLAY "Employee ID: ".
           ACCEPT EMP-ID.
           DISPLAY "Basic Pay ($): ".
           ACCEPT BASIC-PAY.

           PERFORM CALC-SALARY.
           PERFORM PRINT-PAYSLIP.
           STOP RUN.

       CALC-SALARY.
           COMPUTE HRA = BASIC-PAY * 0.20.
           COMPUTE DA = BASIC-PAY * 0.10.

           COMPUTE GROSS-SALARY = BASIC-PAY + HRA + DA + TRANSPORT.

           COMPUTE PF = BASIC-PAY * 0.12.
           COMPUTE TAX = GROSS-SALARY * 0.05.

           COMPUTE TOTAL-DED = PF + TAX + MEDICAL.

           COMPUTE NET-PAY = GROSS-SALARY - TOTAL-DED.

       PRINT-PAYSLIP.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "             PAY SLIP SUMMARY           "
           DISPLAY "========================================"
           DISPLAY "Employee: " EMP-NAME " (ID: " EMP-ID ")"
           DISPLAY "----------------------------------------"
           DISPLAY "EARNINGS:"
           MOVE BASIC-PAY TO FMT-VAL. DISPLAY "  Basic Pay:  " FMT-VAL.
           MOVE HRA TO FMT-VAL.       DISPLAY "  HRA (20%):  " FMT-VAL.
           MOVE DA TO FMT-VAL.        DISPLAY "  DA (10%):   " FMT-VAL.
           MOVE TRANSPORT TO FMT-VAL. DISPLAY "  Transport:  " FMT-VAL.
           DISPLAY "----------------------------------------"
           MOVE GROSS-SALARY TO FMT-VAL.
           DISPLAY "GROSS PAY:    " FMT-VAL.
           DISPLAY "----------------------------------------"
           DISPLAY "DEDUCTIONS:"
           MOVE PF TO FMT-VAL.        DISPLAY "  PF (12% Base): " FMT-VAL.
           MOVE TAX TO FMT-VAL.       DISPLAY "  Income Tax:    " FMT-VAL.
           MOVE MEDICAL TO FMT-VAL.   DISPLAY "  Medical Ins:   " FMT-VAL.
           DISPLAY "----------------------------------------"
           MOVE TOTAL-DED TO FMT-VAL.
           DISPLAY "TOTAL DEDUCT: " FMT-VAL.
           DISPLAY "========================================"
           MOVE NET-PAY TO FMT-VAL.
           DISPLAY "NET PAY (TAKE HOME): " FMT-VAL.
           DISPLAY "========================================".
