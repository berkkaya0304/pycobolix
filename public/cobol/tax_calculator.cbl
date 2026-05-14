       IDENTIFICATION DIVISION.
       PROGRAM-ID. TAX-CALCULATOR.
       AUTHOR. A.


       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 TAXPAYER.
          05 SSN             PIC X(9).
          05 FULL-NAME       PIC X(30).
          05 GROSS-INCOME    PIC 9(7)V99.
          05 DEDUCTIONS      PIC 9(6)V99.
          05 DEPENDENTS      PIC 9(2).

       01 TAX-VARS.
          05 TAXABLE-INCOME  PIC S9(7)V99.
          05 DEPENDENT-DED   PIC 9(5)V99.
          05 TAX-OWED        PIC 9(7)V99 VALUE ZERO.

       01 FMT-VAL            PIC $Z,ZZZ,ZZ9.99.

       PROCEDURE DIVISION.
       START-PGM.
           DISPLAY "--- ANNUAL INCOME TAX CALCULATOR ---".
           DISPLAY "Taxpayer Name: ".
           ACCEPT FULL-NAME.
           DISPLAY "Gross Annual Income ($): ".
           ACCEPT GROSS-INCOME.
           DISPLAY "Itemized Deductions ($): ".
           ACCEPT DEDUCTIONS.
           DISPLAY "Number of Dependents ($2000 credit each): ".
           ACCEPT DEPENDENTS.

           PERFORM DO-CALCS.
           PERFORM SHOW-RETURN.
           STOP RUN.

       DO-CALCS.
           COMPUTE TAXABLE-INCOME = GROSS-INCOME - DEDUCTIONS.
           
           IF TAXABLE-INCOME < 0
               MOVE ZERO TO TAXABLE-INCOME
           END-IF.

           IF TAXABLE-INCOME <= 10000
               COMPUTE TAX-OWED = TAXABLE-INCOME * 0.10
           ELSE IF TAXABLE-INCOME <= 40000
               COMPUTE TAX-OWED = (10000 * 0.10) + 
                                  ((TAXABLE-INCOME - 10000) * 0.12)
           ELSE IF TAXABLE-INCOME <= 85000
               COMPUTE TAX-OWED = (10000 * 0.10) + (30000 * 0.12) + 
                                  ((TAXABLE-INCOME - 40000) * 0.22)
           ELSE
               COMPUTE TAX-OWED = (10000 * 0.10) + (30000 * 0.12) + 
                                  (45000 * 0.22) + 
                                  ((TAXABLE-INCOME - 85000) * 0.24)
           END-IF.

           COMPUTE DEPENDENT-DED = DEPENDENTS * 2000.00.
           SUBTRACT DEPENDENT-DED FROM TAX-OWED.
           
           IF TAX-OWED < 0
               MOVE ZERO TO TAX-OWED
           END-IF.

       SHOW-RETURN.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "        TAX RETURN ESTIMATE SUMMARY     "
           DISPLAY "========================================"
           DISPLAY "Taxpayer: " FULL-NAME
           DISPLAY "----------------------------------------"
           MOVE GROSS-INCOME TO FMT-VAL.
           DISPLAY "Gross Income:     " FMT-VAL.
           MOVE DEDUCTIONS TO FMT-VAL.
           DISPLAY "Deductions:      -" FMT-VAL.
           MOVE TAXABLE-INCOME TO FMT-VAL.
           DISPLAY "Taxable Income:   " FMT-VAL.
           DISPLAY "----------------------------------------"
           MOVE DEPENDENT-DED TO FMT-VAL.
           DISPLAY "Dependent Credit:-" FMT-VAL.
           MOVE TAX-OWED TO FMT-VAL.
           DISPLAY "TOTAL TAX OWED:   " FMT-VAL.
           DISPLAY "========================================".
